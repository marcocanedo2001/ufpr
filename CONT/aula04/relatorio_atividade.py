"""Exportação do relatório da atividade de Engenharia de Contexto em RAG."""

from __future__ import annotations

from datetime import date
from pathlib import Path
import re

from markdown_it import MarkdownIt


def _numero_da_saida(texto: str, rotulo: str) -> str:
    padrao = rf"{re.escape(rotulo)}:\s*([0-9]+(?:[.,][0-9]+)?)"
    resultado = re.search(padrao, texto)
    return resultado.group(1) if resultado else "não registrado"


def _celula(valor: object) -> str:
    return str(valor).replace("|", "\\|").replace("\n", " ").strip()


def _trecho(texto: str, limite: int = 450) -> str:
    return _celula(re.sub(r"\s+", " ", texto).strip()[:limite])


def _validar(
    identificacao: dict,
    justificativa_escopo: str,
    alteracao_descricao: str,
    avaliacao_manual: dict,
    respostas_finais: dict,
    conclusao: str,
) -> None:
    faltantes = []

    for campo, valor in identificacao.items():
        if not str(valor).strip():
            faltantes.append(f"IDENTIFICACAO['{campo}']")

    if not justificativa_escopo.strip():
        faltantes.append("JUSTIFICATIVA_ESCOPO")
    if not alteracao_descricao.strip():
        faltantes.append("ALTERACAO_DESCRICAO")

    for configuracao, respostas in avaliacao_manual.items():
        for campo, valor in respostas.items():
            if not str(valor).strip():
                faltantes.append(
                    f"AVALIACAO_MANUAL['{configuracao}']['{campo}']"
                )

    for campo, valor in respostas_finais.items():
        if not str(valor).strip():
            faltantes.append(f"RESPOSTAS_FINAIS['{campo}']")

    if not conclusao.strip():
        faltantes.append("CONCLUSAO")

    if faltantes:
        lista = "\n- ".join(faltantes)
        raise ValueError(f"Preencha os campos obrigatórios:\n- {lista}")


def _tabela_baseline(resultados: dict) -> str:
    linhas = []

    for rank, (identificador, documento, metadata, distancia) in enumerate(
        zip(
            resultados["ids"][0],
            resultados["documents"][0],
            resultados["metadatas"][0],
            resultados["distances"][0],
        ),
        start=1,
    ):
        linhas.append(
            "| "
            f"{rank} | {_celula(identificador)} | "
            f"{_celula(metadata.get('arquivo'))} | "
            f"{metadata.get('pagina')} | "
            f"{_celula(metadata.get('escopo'))} | "
            f"{1 - distancia:.4f} | {_trecho(documento)} |"
        )

    return "\n".join(linhas)


def _tabela_ranking(candidatos: list) -> str:
    linhas = []

    for rank, candidato in enumerate(candidatos[:5], start=1):
        linhas.append(
            "| "
            f"{rank} | {_celula(candidato.id)} | "
            f"{_celula(candidato.metadata.get('arquivo'))} | "
            f"{candidato.metadata.get('pagina')} | "
            f"{_celula(candidato.metadata.get('escopo'))} | "
            f"{candidato.similaridade:.4f} | {_trecho(candidato.texto)} |"
        )

    return "\n".join(linhas)


def _contagens(etapas: dict[str, list]) -> str:
    return ", ".join(
        f"{nome}: {len(candidatos)}"
        for nome, candidatos in etapas.items()
    )


def _ids_candidatos(candidatos: list) -> str:
    """Lista IDs para tornar auditável o efeito de cada etapa."""
    if not candidatos:
        return "nenhum candidato"

    return ", ".join(_celula(candidato.id) for candidato in candidatos)


def _tabela_etapas_intermediarias(etapas: dict[str, list]) -> str:
    linhas = []

    for nome in ("fusão", "filtros", "deduplicação"):
        candidatos = etapas[nome]
        linhas.append(
            f"| {nome.capitalize()} | {len(candidatos)} | "
            f"{_ids_candidatos(candidatos)} |"
        )

    return "\n".join(linhas)


def _tabela_transformacoes(transformacoes: dict[str, list[str]]) -> str:
    linhas = []

    for tecnica, consultas in transformacoes.items():
        texto = "<br>".join(_celula(consulta) for consulta in consultas)
        linhas.append(f"| {tecnica} | {texto} |")

    return "\n".join(linhas)


def gerar_relatorio(
    *,
    identificacao: dict,
    pergunta: str,
    escopo: str,
    justificativa_escopo: str,
    alteracao_descricao: str,
    avaliacao_manual: dict,
    respostas_finais: dict,
    conclusao: str,
    resultado_baseline: dict,
    tokens_baseline: int,
    etapas_avancado: dict[str, list],
    saida_avancada: str,
    etapas_alterado: dict[str, list],
    saida_alterada: str,
    consultas: list[str],
    transformacoes_consulta: dict[str, list[str]],
    pasta_saida: Path = Path("relatorios"),
) -> tuple[Path, Path]:
    """Cria versões Markdown e HTML do relatório preenchido."""
    _validar(
        identificacao,
        justificativa_escopo,
        alteracao_descricao,
        avaliacao_manual,
        respostas_finais,
        conclusao,
    )

    avaliacao_baseline = avaliacao_manual["baseline"]
    avaliacao_avancado = avaliacao_manual["avancado"]
    avaliacao_alterado = avaliacao_manual["alterado"]

    latencia_baseline = f"{resultado_baseline['latencia_ms']:.2f} ms"
    tokens_avancado = _numero_da_saida(
        saida_avancada,
        "Tokens aproximados do contexto",
    )
    latencia_avancado = (
        _numero_da_saida(saida_avancada, "Latencia total aproximada")
        + " ms"
    )
    tokens_alterado = _numero_da_saida(
        saida_alterada,
        "Tokens aproximados do contexto",
    )
    latencia_alterado = (
        _numero_da_saida(saida_alterada, "Latencia total aproximada")
        + " ms"
    )
    lista_consultas = "\n".join(
        f"{indice}. {consulta}"
        for indice, consulta in enumerate(consultas, start=1)
    )

    relatorio = f"""# Relatório — Engenharia de Contexto em RAG

## Identificação

- **Aluno(a):** {identificacao['nome']}
- **Turma:** {identificacao['turma']}
- **Data:** {date.today().strftime('%d/%m/%Y')}

## 1. Pergunta e escopo

- **Pergunta:** {pergunta}
- **Escopo esperado:** {escopo}
- **Justificativa:** {justificativa_escopo}

## 2. Pipeline baseline

Foi utilizada busca por similaridade sem filtro de escopo. Foram recuperados
{len(resultado_baseline['ids'][0])} candidatos, com {tokens_baseline} tokens
aproximados e latência de {latencia_baseline}.

| Rank | ID | Arquivo | Página | Escopo | Similaridade | Trecho |
|---:|---|---|---:|---|---:|---|
{_tabela_baseline(resultado_baseline)}

**Avaliação:** top-1 correto: {avaliacao_baseline['top1_correto']}; escopo
correto: {avaliacao_baseline['escopo_correto']}; há ruído:
{avaliacao_baseline['ha_ruido']}; contexto suficiente:
{avaliacao_baseline['contexto_suficiente']}.

**Observações:** {avaliacao_baseline['observacoes']}

**Redundância:** {avaliacao_baseline['redundancia']}

## 3. Pipeline avançado

### 3.1 Consultas geradas

| Técnica | Consulta(s) produzida(s) antes da deduplicação |
|---|---|
{_tabela_transformacoes(transformacoes_consulta)}

Após a deduplicação, foram executadas as seguintes consultas únicas:

{lista_consultas}

### 3.2 Resultados intermediários

Contagens — {_contagens(etapas_avancado)}.

| Etapa | Candidatos | IDs resultantes |
|---|---:|---|
{_tabela_etapas_intermediarias(etapas_avancado)}

| Rank após reranking | ID | Arquivo | Página | Escopo | Similaridade | Trecho |
|---:|---|---|---:|---|---:|---|
{_tabela_ranking(etapas_avancado['reranking'])}

O contexto final contém aproximadamente {tokens_avancado} tokens e a execução
teve latência total aproximada de {latencia_avancado}.

**Avaliação:** top-1 correto: {avaliacao_avancado['top1_correto']}; escopo
correto: {avaliacao_avancado['escopo_correto']}; há ruído:
{avaliacao_avancado['ha_ruido']}; contexto suficiente:
{avaliacao_avancado['contexto_suficiente']}.

**Observações:** {avaliacao_avancado['observacoes']}

**Redundância:** {avaliacao_avancado['redundancia']}

### 3.3 Saída completa do pipeline

```text
{saida_avancada}
```

## 4. Alteração experimental

**Alteração realizada:** {alteracao_descricao}

Contagens — {_contagens(etapas_alterado)}.

| Etapa | Candidatos | IDs resultantes |
|---|---:|---|
{_tabela_etapas_intermediarias(etapas_alterado)}

| Rank após reranking | ID | Arquivo | Página | Escopo | Similaridade | Trecho |
|---:|---|---|---:|---|---:|---|
{_tabela_ranking(etapas_alterado['reranking'])}

O contexto alterado contém aproximadamente {tokens_alterado} tokens e a
execução teve latência total aproximada de {latencia_alterado}.

**Avaliação:** top-1 correto: {avaliacao_alterado['top1_correto']}; escopo
correto: {avaliacao_alterado['escopo_correto']}; há ruído:
{avaliacao_alterado['ha_ruido']}; contexto suficiente:
{avaliacao_alterado['contexto_suficiente']}.

**Observações:** {avaliacao_alterado['observacoes']}

**Redundância:** {avaliacao_alterado['redundancia']}

### 4.1 Saída completa do pipeline alterado

```text
{saida_alterada}
```

## 5. Comparação

| Critério | Baseline | Avançado | Alterado |
|---|---:|---:|---:|
| Top-1 correto? | {_celula(avaliacao_baseline['top1_correto'])} | {_celula(avaliacao_avancado['top1_correto'])} | {_celula(avaliacao_alterado['top1_correto'])} |
| Escopo correto? | {_celula(avaliacao_baseline['escopo_correto'])} | {_celula(avaliacao_avancado['escopo_correto'])} | {_celula(avaliacao_alterado['escopo_correto'])} |
| Candidatos recuperados (top-k) | {len(resultado_baseline['ids'][0])} | — | — |
| Candidatos após fusão | — | {len(etapas_avancado['fusão'])} | {len(etapas_alterado['fusão'])} |
| Candidatos após filtros | — | {len(etapas_avancado['filtros'])} | {len(etapas_alterado['filtros'])} |
| Tokens aproximados | {tokens_baseline} | {tokens_avancado} | {tokens_alterado} |
| Latência | {latencia_baseline} | {latencia_avancado} | {latencia_alterado} |
| Há ruído? | {_celula(avaliacao_baseline['ha_ruido'])} | {_celula(avaliacao_avancado['ha_ruido'])} | {_celula(avaliacao_alterado['ha_ruido'])} |
| Há redundância? | {_celula(avaliacao_baseline['redundancia'])} | {_celula(avaliacao_avancado['redundancia'])} | {_celula(avaliacao_alterado['redundancia'])} |
| Contexto suficiente? | {_celula(avaliacao_baseline['contexto_suficiente'])} | {_celula(avaliacao_avancado['contexto_suficiente'])} | {_celula(avaliacao_alterado['contexto_suficiente'])} |

**Limites da medição:** as latências são observações de execuções individuais,
sem repetições suficientes para demonstrar ganho de velocidade. O baseline mede
a recuperação, enquanto o avançado inclui etapas adicionais. A diferença entre
avançado e alterado não pode ser atribuída à redução do orçamento: a busca
ocorre antes da compressão. O ganho observado é a redução do contexto com
preservação da evidência. Os tokens são estimativas didáticas, não contagens de
um tokenizer nem medidas de custo efetivamente cobrado por um LLM.

**Síntese qualitativa:**

- **Baseline:** {avaliacao_baseline['observacoes']}
- **Avançado:** {avaliacao_avancado['observacoes']}
- **Alterado:** {avaliacao_alterado['observacoes']}

## 6. Análise final

### 6.1 O pipeline avançado recuperou contexto melhor que o baseline?

{respostas_finais['pipeline_melhor']}

### 6.2 Qual etapa teve maior influência sobre o resultado?

{respostas_finais['etapa_influente']}

### 6.3 Alguma técnica eliminou evidência útil ou introduziu ruído?

{respostas_finais['evidencia_ou_ruido']}

### 6.4 Qual configuração seria usada em uma aplicação real?

{respostas_finais['configuracao_real']}

### 6.5 Qual contexto seria enviado ao LLM e por quê?

{respostas_finais['contexto_para_llm']}

## 7. Conclusão

{conclusao}
"""

    pasta_saida.mkdir(parents=True, exist_ok=True)
    caminho_markdown = pasta_saida / "relatorio_atividade_rag.md"
    caminho_html = pasta_saida / "relatorio_atividade_rag.html"
    caminho_markdown.write_text(relatorio, encoding="utf-8")

    corpo_html = (
        MarkdownIt("commonmark", {"html": False})
        .enable("table")
        .render(relatorio)
    )
    documento_html = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Relatório — Engenharia de Contexto em RAG</title>
<style>
body {{ font-family: Arial, sans-serif; line-height: 1.5; max-width: 1100px;
       margin: 40px auto; padding: 0 24px; color: #1f2937; }}
h1, h2, h3 {{ color: #17365d; }}
table {{ border-collapse: collapse; width: 100%; margin: 18px 0; }}
th, td {{ border: 1px solid #9ca3af; padding: 8px; vertical-align: top; }}
th {{ background: #eaf0f8; }}
pre {{ white-space: pre-wrap; background: #f4f4f5; padding: 14px;
       border-radius: 6px; }}
code {{ font-family: Consolas, monospace; }}
@media print {{ body {{ margin: 0; max-width: none; }} }}
</style>
</head>
<body>
{corpo_html}
</body>
</html>
"""
    caminho_html.write_text(documento_html, encoding="utf-8")

    return caminho_markdown.resolve(), caminho_html.resolve()
