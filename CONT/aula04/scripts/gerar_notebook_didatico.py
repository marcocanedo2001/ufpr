"""Gera uma versão didática de genai.ipynb sem alterar o algoritmo-base."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


RAIZ = Path(__file__).resolve().parent.parent
ORIGINAL = RAIZ / "genai.ipynb"
DESTINO = RAIZ / "genai_didatico.ipynb"


def markdown(identificador: str, texto: str) -> dict:
    return {
        "cell_type": "markdown",
        "id": identificador,
        "metadata": {},
        "source": texto.strip() + "\n",
    }


def codigo(
    identificador: str,
    fonte: str,
    *,
    original: bool = False,
) -> dict:
    metadados = {"tags": ["codigo-original"]} if original else {}
    return {
        "cell_type": "code",
        "execution_count": None,
        "id": identificador,
        "metadata": metadados,
        "outputs": [],
        "source": fonte,
    }


def titulo_secao(fonte: str) -> str:
    linhas = fonte.splitlines()
    if len(linhas) < 2:
        raise ValueError("Bloco sem título de seção")
    return linhas[1].removeprefix("# ").strip()


notebook_original = json.loads(ORIGINAL.read_text(encoding="utf-8"))
celulas_originais = notebook_original["cells"]

if len(celulas_originais) != 4:
    raise RuntimeError(
        "O notebook original mudou: eram esperadas exatamente quatro células."
    )

instalacao = "".join(celulas_originais[0].get("source", []))
workspace = "".join(celulas_originais[1].get("source", []))
imports_configuracao = "".join(celulas_originais[2].get("source", []))
algoritmo = "".join(celulas_originais[3].get("source", []))

separador_principal = re.compile(
    r"(?m)(?=^# ={20,}\n# .+\n# ={20,}\n)"
)
partes_principais = separador_principal.split(algoritmo)
configuracao_parametros = partes_principais[0]
secoes = {titulo_secao(parte): parte for parte in partes_principais[1:]}

titulos_esperados = {
    "UTILITÁRIOS DE NORMALIZAÇÃO",
    "INGESTÃO: LEITURA, ESCOPO E METADADOS",
    "CHUNKING",
    "BANCO VETORIAL",
    "EMBEDDINGS E INDEXAÇÃO",
    "BUSCA VETORIAL BASELINE",
    "MAXIMAL MARGINAL RELEVANCE",
    "EXIBIÇÃO DO BASELINE",
    "AULA 2: ENGENHARIA DE CONTEXTO",
    "PROGRAMA PRINCIPAL",
}
if set(secoes) != titulos_esperados:
    raise RuntimeError(
        "As seções do notebook original mudaram; revise o gerador antes de continuar."
    )

separador_subsecao = re.compile(
    r"(?m)(?=^# -{20,}\n# .+\n# -{20,}\n)"
)
partes_contexto = separador_subsecao.split(
    secoes["AULA 2: ENGENHARIA DE CONTEXTO"]
)
base_contexto = partes_contexto[0]
subsecoes = {titulo_secao(parte): parte for parte in partes_contexto[1:]}

subtitulos_esperados = {
    "Pré-recuperação: ambiguidade e transformação de consultas",
    "Recuperação e fusão",
    "Pós-recuperação: filtros, deduplicação e reranking",
    "Compressão de contexto",
    "Contexto suficiente e decisão de resposta",
    "Exibição das transformações",
    "Pipeline final com medição de custo por etapa",
}
if set(subsecoes) != subtitulos_esperados:
    raise RuntimeError(
        "As subseções de engenharia de contexto mudaram; revise o gerador."
    )

chamada_main = '\n\nif __name__ == "__main__":\n    main()\n'
programa_principal = secoes["PROGRAMA PRINCIPAL"]
if chamada_main not in programa_principal:
    raise RuntimeError("Não foi possível separar a chamada opcional de main().")
definicao_main, invocacao_main = programa_principal.rsplit(chamada_main, 1)
invocacao_main = chamada_main.lstrip("\n") + invocacao_main

# Esta comparação protege contra alterações acidentais no código da professora.
reconstruido = "".join(
    [
        configuracao_parametros,
        secoes["UTILITÁRIOS DE NORMALIZAÇÃO"],
        secoes["INGESTÃO: LEITURA, ESCOPO E METADADOS"],
        secoes["CHUNKING"],
        secoes["BANCO VETORIAL"],
        secoes["EMBEDDINGS E INDEXAÇÃO"],
        secoes["BUSCA VETORIAL BASELINE"],
        secoes["MAXIMAL MARGINAL RELEVANCE"],
        secoes["EXIBIÇÃO DO BASELINE"],
        base_contexto,
        subsecoes[
            "Pré-recuperação: ambiguidade e transformação de consultas"
        ],
        subsecoes["Recuperação e fusão"],
        subsecoes[
            "Pós-recuperação: filtros, deduplicação e reranking"
        ],
        subsecoes["Compressão de contexto"],
        subsecoes["Contexto suficiente e decisão de resposta"],
        subsecoes["Exibição das transformações"],
        subsecoes["Pipeline final com medição de custo por etapa"],
        definicao_main,
        chamada_main,
    ]
)
if reconstruido != algoritmo:
    raise RuntimeError("A separação das células alteraria o código original.")

hash_algoritmo = hashlib.sha256(algoritmo.encode("utf-8")).hexdigest()

celulas = [
    markdown(
        "titulo",
        r"""
# Engenharia de Contexto em RAG — versão didática

Este notebook deriva do `genai.ipynb` fornecido pela professora e adiciona duas
camadas de apoio:

1. explicações dos conceitos apresentados em `aula_2.pdf`;
2. um roteiro para coletar as evidências solicitadas em `Atividade.pdf`.

O algoritmo-base foi preservado. As células marcadas com a tag
`codigo-original` contêm literalmente o código da professora, apenas dividido
pelos títulos que já existiam no arquivo. A chamada interativa `main()` foi
movida para uma célula opcional no final, porque ela abre um laço de perguntas e
interromperia o roteiro guiado.

> O notebook orienta a execução, mas não escolhe a pergunta, não preenche a
> análise e não conclui qual configuração é melhor. Essas decisões fazem parte
> da atividade.
""",
    ),
    markdown(
        "mapa-atividade",
        r"""
## O que precisa aparecer na entrega

O relatório deve acompanhar uma mesma pergunta em três configurações:

| Etapa | O que executar | O que registrar |
|---|---|---|
| Baseline | Busca por similaridade | Top-3, escopo, tokens, latência e suficiência do top-1 |
| Avançado | Pipeline completo | Consultas geradas, candidatos, filtros, deduplicação, reranking, tokens e decisão |
| Alterado | Uma modificação controlada | A mesma medição para permitir comparação justa |

Ao final, compare relevância, ruído, redundância, adequação do escopo, custo em
tokens, latência e suficiência. Uma métrica isolada não prova que o contexto
melhorou: reduzir tokens, por exemplo, pode remover uma condição importante.
""",
    ),
    markdown(
        "ambiente",
        r"""
## 1. Ambiente

Use o kernel **Python (aula04)**. A instalação abaixo lê o arquivo
`requirements.txt` do workspace. Normalmente ela só confirma pacotes que já
estão instalados no ambiente virtual.
""",
    ),
    codigo("instalacao", instalacao, original=True),
    markdown(
        "workspace-explicacao",
        r"""
### Diretório de trabalho

Os caminhos do notebook são relativos. Portanto, o Jupyter deve estar aberto
na pasta `CONT/aula04`. A célula seguinte mostra o diretório efetivamente usado.
""",
    ),
    codigo("workspace", workspace, original=True),
    markdown(
        "cache-embeddings-explicacao",
        r"""
### Cache local do modelo de embeddings

O modelo de embeddings já foi baixado para este ambiente. A próxima célula
impede consultas desnecessárias à internet durante o carregamento; ela não
altera o modelo nem o algoritmo de recuperação. Se o notebook for aberto em
outro computador sem o modelo em cache, defina `HF_HUB_OFFLINE = "0"` uma vez
para permitir o download inicial.
""",
    ),
    codigo(
        "cache-embeddings",
        '''import os

# Reutiliza o modelo já armazenado em ~/.cache/huggingface.
# Isso evita que um novo kernel fique aguardando uma consulta de rede.
os.environ["HF_HUB_OFFLINE"] = "1"

print("Modelo de embeddings: uso do cache local ativado.")
''',
    ),
    markdown(
        "dados-explicacao",
        r"""
### Documentos usados na recuperação

A pasta `documentos/` contém três fontes com papéis diferentes:

- regulamento de estágio → escopo `estagio`;
- PPC do curso → escopo `curso`;
- ficha de Banco de Dados (CI1218) → escopo `disciplina`.

Essa distinção é central para perguntas ambíguas. “Frequência mínima”, por
exemplo, pode significar regras diferentes dependendo da fonte consultada.
""",
    ),
    codigo("imports-caminhos", imports_configuracao, original=True),
    markdown(
        "parametros-explicacao",
        r"""
## 2. Parâmetros do experimento

Estes valores controlam o comportamento observado na atividade:

- `TAMANHO_CHUNK` e `OVERLAP_CHUNK`: quantidade de caracteres por trecho e
  repetição entre trechos vizinhos;
- `TOP_K`: quantidade final de resultados;
- `MODO_BUSCA`: similaridade pura ou MMR no fluxo baseline interativo;
- `FETCH_K_MMR` e `LAMBDA_MMR`: candidatos e equilíbrio entre relevância e
  diversidade no MMR;
- `RECRIAR_COLECAO`: recria ou reutiliza o índice persistente;
- `LIMITE_TOKENS_CONTEXTO`: orçamento aproximado enviado ao LLM;
- `LIMIAR_SIMILARIDADE`: remove candidatos abaixo do score definido.

Na primeira indexação, mantenha `RECRIAR_COLECAO = True`. Depois, use `False`
para evitar reconstruir a coleção a cada execução. Para o experimento alterado,
mude uma variável por vez; isso permite atribuir o efeito à decisão correta.
""",
    ),
    codigo(
        "parametros-originais",
        configuracao_parametros,
        original=True,
    ),
    markdown(
        "normalizacao-explicacao",
        r"""
## 3. Normalização

As funções abaixo removem diferenças superficiais — maiúsculas, acentos,
espaços e quebras de linha — antes de comparar termos. Isso não produz
embeddings e não muda o significado semântico; apenas torna regras como
“estágio” versus “estagio” previsíveis.
""",
    ),
    codigo(
        "normalizacao",
        secoes["UTILITÁRIOS DE NORMALIZAÇÃO"],
        original=True,
    ),
    markdown(
        "ingestao-explicacao",
        r"""
## 4. Ingestão, escopo e metadados

Cada PDF é lido página a página. O texto extraído recebe dois metadados:
`escopo` e `tipo_documento`. O código prioriza o nome do arquivo, uma fonte
controlada, e usa o conteúdo inicial da página apenas como fallback.

Esse desenho combina recuperação semântica com regras simbólicas. O embedding
indica proximidade de significado; o metadado impede que uma regra de estágio
seja tratada como regra de disciplina apenas porque as frases são parecidas.
""",
    ),
    codigo(
        "ingestao",
        secoes["INGESTÃO: LEITURA, ESCOPO E METADADOS"],
        original=True,
    ),
    markdown(
        "chunking-explicacao",
        r"""
## 5. Chunking

O documento é dividido em janelas de caracteres com sobreposição. Chunks muito
grandes preservam mais contexto, mas gastam tokens e podem misturar assuntos;
chunks pequenos são específicos, porém podem separar uma regra de sua condição.
O overlap reduz cortes abruptos ao custo de aumentar redundância.
""",
    ),
    codigo("chunking", secoes["CHUNKING"], original=True),
    markdown(
        "chroma-explicacao",
        r"""
## 6. Banco vetorial

O ChromaDB persiste os vetores em `chroma_db/`. A coleção usa distância de
cosseno. Com embeddings normalizados, valores mais próximos representam maior
similaridade semântica. Recriar a coleção é útil quando documentos, chunks ou
metadados mudam; reutilizá-la reduz o custo das execuções seguintes.
""",
    ),
    codigo("banco-vetorial", secoes["BANCO VETORIAL"], original=True),
    markdown(
        "embeddings-explicacao",
        r"""
## 7. Embeddings e indexação

`SentenceTransformer` transforma cada chunk em um vetor. A indexação é feita
em lotes e grava simultaneamente ID, vetor, texto e metadados. O modelo usado é
multilíngue, adequado aos documentos e perguntas em português.

O embedding ajuda a localizar texto semanticamente relacionado, mas não garante
que o trecho contenha a resposta. Essa diferença entre relevância e suficiência
será medida no exercício.
""",
    ),
    codigo(
        "embeddings-indexacao",
        secoes["EMBEDDINGS E INDEXAÇÃO"],
        original=True,
    ),
    markdown(
        "baseline-explicacao",
        r"""
## 8. Baseline: busca por similaridade

O baseline codifica a pergunta, recupera os `k` vetores mais próximos e pode
aplicar um filtro de escopo. Ele serve como referência simples: qualquer ganho
do pipeline avançado deve ser comparado a este resultado, incluindo o custo
adicional.

Para cada execução, observe top-1, suficiência, escopo, redundância, ruído,
latência e tokens. “Relacionado” não significa necessariamente “capaz de
responder”.
""",
    ),
    codigo(
        "busca-baseline",
        secoes["BUSCA VETORIAL BASELINE"],
        original=True,
    ),
    markdown(
        "mmr-explicacao",
        r"""
## 9. MMR: relevância com diversidade

O Maximal Marginal Relevance seleciona resultados equilibrando dois objetivos:

$$\text{MMR}=\lambda\,\text{relevância}-(1-\lambda)\,\text{redundância}$$

Com `lambda` próximo de 1, a relevância domina. Valores menores favorecem
diversidade. MMR pode reduzir chunks repetidos, mas um resultado diferente não é
automaticamente melhor: ele ainda precisa conter evidência útil.

Importante para a atividade: `LAMBDA_MMR` afeta `buscar_mmr`. O pipeline
avançado usa múltiplas buscas por similaridade e RRF; portanto, alterar somente
`LAMBDA_MMR` não modifica `responder_com_contexto`.
""",
    ),
    codigo(
        "busca-mmr",
        secoes["MAXIMAL MARGINAL RELEVANCE"],
        original=True,
    ),
    markdown(
        "exibicao-baseline-explicacao",
        r"""
### Leitura dos resultados do baseline

A distância de cosseno é convertida em similaridade aproximada por
`1 - distancia`. Além do número, examine texto, arquivo, página e escopo. A
evidência correta precisa ser rastreável até uma fonte adequada.
""",
    ),
    codigo(
        "exibicao-baseline",
        secoes["EXIBIÇÃO DO BASELINE"],
        original=True,
    ),
    markdown(
        "engenharia-contexto-visao",
        r"""
## 10. Engenharia de contexto: visão geral

O pipeline avançado não é apenas uma busca maior. Cada etapa responde a uma
pergunta diferente:

`ambiguidade → transformação → recuperação → fusão → filtros → deduplicação → reranking → compressão → suficiência → ação`

- recuperação encontra candidatos relacionados;
- filtros excluem candidatos incompatíveis;
- reranking altera a ordem;
- compressão escolhe o conteúdo que cabe no orçamento;
- suficiência decide se existe evidência para responder.

Misturar essas funções dificulta descobrir por que o resultado melhorou ou
piorou. O experimento deve registrar o efeito de cada decisão.
""",
    ),
    codigo("tipos-e-tokens", base_contexto, original=True),
    markdown(
        "pre-recuperacao-explicacao",
        r"""
### 10.1 Antes da recuperação

- **Detecção de ambiguidade:** impede assumir um escopo quando a pergunta aceita
  interpretações diferentes.
- **Rewrite:** reformula a pergunta de acordo com o escopo informado.
- **Expansão:** cria variações lexicais da mesma intenção.
- **Step-back:** formula uma questão mais geral para buscar contexto conceitual.
- **HyDE:** cria um trecho hipotético parecido com a resposta esperada e o usa
  somente para recuperar documentos. O texto hipotético não é evidência e não
  deve aparecer como fonte da resposta.

Essas técnicas podem aumentar cobertura, mas também custo e ruído. Por isso as
consultas geradas devem ser registradas na atividade.
""",
    ),
    codigo(
        "pre-recuperacao",
        subsecoes[
            "Pré-recuperação: ambiguidade e transformação de consultas"
        ],
        original=True,
    ),
    markdown(
        "fusao-explicacao",
        r"""
### 10.2 Recuperação e fusão por RRF

Cada variação da consulta produz um ranking. O Reciprocal Rank Fusion soma
contribuições baseadas na posição de cada chunk. Um item bem colocado em várias
listas ganha força sem exigir que scores de consultas diferentes sejam
diretamente comparáveis.
""",
    ),
    codigo(
        "recuperacao-fusao",
        subsecoes["Recuperação e fusão"],
        original=True,
    ),
    markdown(
        "pos-recuperacao-explicacao",
        r"""
### 10.3 Filtros, deduplicação e reranking

O filtro de escopo funciona como defesa adicional. O limiar elimina candidatos
fracos. A deduplicação remove textos idênticos ou muito sobrepostos. Por fim, o
reranker combina similaridade vetorial, cobertura lexical e bônus de metadados.

Cada etapa traz um risco: um limiar alto pode apagar evidência útil; uma
deduplicação agressiva pode confundir trechos complementares; um reranker
lexical pode favorecer repetição de palavras em vez de significado.
""",
    ),
    codigo(
        "pos-recuperacao",
        subsecoes[
            "Pós-recuperação: filtros, deduplicação e reranking"
        ],
        original=True,
    ),
    markdown(
        "compressao-explicacao",
        r"""
### 10.4 Compressão e orçamento de contexto

O contexto disputa a janela do modelo com instruções, histórico, pergunta,
metadados e espaço para a resposta. A compressão extrativa mantém sentenças
relacionadas à pergunta até o orçamento definido.

Ao reduzir texto, preserve cinco elementos: valor, escopo, condição, exceção e
fonte. Um contexto menor pode ter custo melhor e confiabilidade pior se perder
qualquer um deles.
""",
    ),
    codigo(
        "compressao",
        subsecoes["Compressão de contexto"],
        original=True,
    ),
    markdown(
        "suficiencia-explicacao",
        r"""
### 10.5 Suficiência e decisão

O pipeline verifica se o contexto cobre os termos centrais. Perguntas
quantitativas também exigem número ou percentual explícito. Dependendo do caso,
a ação segura pode ser esclarecer, buscar novamente, abster-se ou responder.

Na atividade, não avalie suficiência apenas pelo score: leia o trecho e confirme
se ele sustenta a resposta sem conhecimento externo.
""",
    ),
    codigo(
        "suficiencia",
        subsecoes["Contexto suficiente e decisão de resposta"],
        original=True,
    ),
    markdown(
        "consultas-explicacao",
        r"""
### 10.6 Consultas geradas

Esta função torna visíveis as transformações feitas antes da recuperação. Copie
essas consultas para o relatório: elas ajudam a explicar aumento de cobertura,
ruído ou latência.
""",
    ),
    codigo(
        "exibicao-transformacoes",
        subsecoes["Exibição das transformações"],
        original=True,
    ),
    markdown(
        "pipeline-final-explicacao",
        r"""
### 10.7 Pipeline avançado completo

`responder_com_contexto` encadeia as etapas anteriores e mede seus tempos. O
resultado final inclui contagens intermediárias, tokens, decisão e o prompt que
seria enviado ao LLM. Ele não chama uma API de LLM; o foco da aula é avaliar a
qualidade do contexto construído.
""",
    ),
    codigo(
        "pipeline-final",
        subsecoes["Pipeline final com medição de custo por etapa"],
        original=True,
    ),
    markdown(
        "main-explicacao",
        r"""
## 11. Programa interativo original

A função `main()` carrega PDFs, cria chunks, instancia o modelo, prepara a
coleção e abre o terminal interativo. A definição permanece abaixo, mas sua
chamada foi deixada no final do notebook. Para a atividade, use primeiro o
roteiro guiado, que mantém as variáveis acessíveis entre as células.
""",
    ),
    codigo("definicao-main", definicao_main, original=True),
    markdown(
        "atividade-titulo",
        r"""
# Roteiro guiado da atividade

Execute esta parte depois de executar todas as definições anteriores. Use a
mesma pergunta nas três configurações. Isso evita comparar resultados causados
por perguntas diferentes.
""",
    ),
    markdown(
        "atividade-pergunta-explicacao",
        r"""
## A. Defina pergunta e escopo

Escolha uma pergunta diferente das já demonstradas em aula e que possa ser
respondida pelos documentos. Preencha também a justificativa em texto. O
escopo deve ser exatamente `curso`, `disciplina` ou `estagio`.
""",
    ),
    codigo(
        "atividade-pergunta",
        '''PERGUNTA_ATIVIDADE = (
    "Qual é a carga horária do estágio obrigatório e que exigência sobre a "
    "conclusão das disciplinas básicas deve ser cumprida para realizá-lo?"
)  # Preencha sem copiar uma pergunta já executada em aula.
ESCOPO_ATIVIDADE = "estagio"  # Troque por: "curso", "disciplina" ou "estagio".
JUSTIFICATIVA_ESCOPO = (
    "A pergunta trata das regras e da carga horária do estágio obrigatório. "
    "Essas informações pertencem ao regulamento de estágio, portanto o "
    "escopo esperado é estagio."
)  # Explique por que esse documento/escopo é o adequado.

if not PERGUNTA_ATIVIDADE.strip():
    raise ValueError("Preencha PERGUNTA_ATIVIDADE antes de continuar.")

validar_escopo(ESCOPO_ATIVIDADE)

if ESCOPO_ATIVIDADE is None:
    raise ValueError("Defina o escopo esperado para a atividade.")

print(f"Pergunta: {PERGUNTA_ATIVIDADE}")
print(f"Escopo esperado: {ESCOPO_ATIVIDADE}")
print(f"Justificativa: {JUSTIFICATIVA_ESCOPO}")
''',
    ),
    markdown(
        "atividade-preparo-explicacao",
        r"""
## B. Prepare o índice uma única vez

Esta célula usa as mesmas funções e parâmetros do `main()`. Depois da primeira
indexação bem-sucedida, você pode definir `RECRIAR_COLECAO = False` e reutilizar
o banco. O download inicial do modelo exige internet.
""",
    ),
    codigo(
        "atividade-preparo",
        '''paginas_atividade = carregar_pdfs(PASTA_DOCUMENTOS)
chunks_atividade = preparar_chunks(paginas_atividade)

modelo_atividade = SentenceTransformer(MODELO_EMBEDDING)
colecao_atividade = criar_colecao(recriar=RECRIAR_COLECAO)

if RECRIAR_COLECAO or colecao_atividade.count() == 0:
    indexar_chunks(
        colecao_atividade,
        modelo_atividade,
        chunks_atividade,
    )

print(f"Páginas: {len(paginas_atividade)}")
print(f"Chunks: {len(chunks_atividade)}")
print(f"Registros na coleção: {colecao_atividade.count()}")
''',
    ),
    markdown(
        "atividade-baseline-explicacao",
        r"""
## C. Execute o baseline

O enunciado pede busca por similaridade. Por isso esta célula chama `buscar`,
não `buscar_mmr`. Guarde os três resultados e julgue manualmente se o top-1
contém evidência suficiente.
""",
    ),
    codigo(
        "atividade-baseline",
        '''resultado_baseline_atividade = buscar(
    colecao_atividade,
    modelo_atividade,
    PERGUNTA_ATIVIDADE,
    k=TOP_K,
    escopo=None,
)

imprimir_resultados(resultado_baseline_atividade)

print(
    "Tokens aproximados: ",
    estimar_tokens_resultados(resultado_baseline_atividade),
)
print(
    "Latência da recuperação: "
    f"{resultado_baseline_atividade['latencia_ms']:.2f} ms"
)
print(
    "Escopos recuperados: ",
    [
        metadata.get("escopo")
        for metadata in resultado_baseline_atividade["metadatas"][0]
    ],
)
''',
    ),
    markdown(
        "instrumentacao-explicacao",
        r"""
## D. Observe as etapas do pipeline avançado

A função auxiliar abaixo não substitui nem modifica o pipeline. Ela apenas chama
as funções existentes na mesma ordem e devolve cópias das listas intermediárias,
permitindo registrar candidatos, filtros, deduplicação e reranking.
""",
    ),
    codigo(
        "instrumentacao",
        '''def observar_etapas_pipeline(
    collection,
    modelo: SentenceTransformer,
    pergunta: str,
    escopo: str | None,
) -> dict[str, list[ResultadoChunk]]:
    """Expõe resultados intermediários sem alterar as funções do pipeline."""
    apos_fusao = multi_busca(
        collection,
        modelo,
        pergunta,
        escopo=escopo,
        k=4,
    )
    apos_filtro_escopo = filtrar_por_escopo(apos_fusao, escopo)
    apos_filtros = filtrar_por_score(
        apos_filtro_escopo,
        minimo=LIMIAR_SIMILARIDADE,
    )
    apos_deduplicacao = deduplicar(apos_filtros)
    apos_reranking = rerank_lexical(pergunta, apos_deduplicacao)

    return {
        "fusão": apos_fusao,
        "filtros": apos_filtros,
        "deduplicação": apos_deduplicacao,
        "reranking": apos_reranking,
    }


def imprimir_etapas_pipeline(etapas: dict[str, list[ResultadoChunk]]) -> None:
    for nome, candidatos in etapas.items():
        print("\\n" + "=" * 80)
        print(f"Etapa: {nome} | candidatos: {len(candidatos)}")
        for posicao, candidato in enumerate(candidatos, start=1):
            print(
                f"{posicao}. {candidato.id} | "
                f"similaridade={candidato.similaridade:.4f} | "
                f"escopo={candidato.metadata.get('escopo')} | "
                f"arquivo={candidato.metadata.get('arquivo')}"
            )
''',
    ),
    codigo(
        "atividade-etapas",
        '''etapas_atividade = observar_etapas_pipeline(
    colecao_atividade,
    modelo_atividade,
    PERGUNTA_ATIVIDADE,
    ESCOPO_ATIVIDADE,
)

imprimir_etapas_pipeline(etapas_atividade)
''',
    ),
    markdown(
        "atividade-avancado-explicacao",
        r"""
## E. Execute o pipeline avançado

Registre as consultas, as contagens, os tokens, a latência, a decisão e o
contexto final. Não conclua apenas pelo número de candidatos: leia as fontes e
verifique se o contexto preserva valores, condições, exceções e escopo.
""",
    ),
    codigo(
        "atividade-avancado",
        '''imprimir_consultas_geradas(
    PERGUNTA_ATIVIDADE,
    ESCOPO_ATIVIDADE,
)

saida_avancada_atividade = responder_com_contexto(
    colecao_atividade,
    modelo_atividade,
    PERGUNTA_ATIVIDADE,
    escopo=ESCOPO_ATIVIDADE,
)

print(saida_avancada_atividade)
''',
    ),
    markdown(
        "atividade-consultas-explicacao",
        r"""
### Registro das transformações de consulta

O enunciado pede observar *rewrite*, expansão, *step-back* e HyDE. A célula
seguinte registra o resultado de cada técnica **antes** da deduplicação. Em
perguntas para as quais uma técnica não possui regra específica, ela pode
devolver a própria pergunta original; isso também é um resultado válido e deve
ser relatado.
""",
    ),
    codigo(
        "atividade-transformacoes-consulta",
        '''TRANSFORMACOES_CONSULTA = {
    "Consulta original": [PERGUNTA_ATIVIDADE],
    "Rewrite": [
        reescrever_consulta(PERGUNTA_ATIVIDADE, escopo=ESCOPO_ATIVIDADE)
    ],
    "Expansão": expandir_consulta(
        PERGUNTA_ATIVIDADE,
        escopo=ESCOPO_ATIVIDADE,
    ),
    "Step-back": [
        step_back(PERGUNTA_ATIVIDADE, escopo=ESCOPO_ATIVIDADE)
    ],
    "HyDE controlado": [
        hyde_controlado(PERGUNTA_ATIVIDADE, escopo=ESCOPO_ATIVIDADE)
    ],
}

CONSULTAS_UNICAS = gerar_consultas(
    PERGUNTA_ATIVIDADE,
    escopo=ESCOPO_ATIVIDADE,
)

for tecnica, consultas in TRANSFORMACOES_CONSULTA.items():
    print(f"{tecnica}: {consultas}")

print("\\nConsultas únicas após deduplicação:")
for indice, consulta in enumerate(CONSULTAS_UNICAS, start=1):
    print(f"{indice}. {consulta}")
''',
    ),
    markdown(
        "atividade-alteracao-explicacao",
        r"""
## F. Faça uma alteração controlada

Escolha apenas uma mudança. As opções mais diretas, sem redefinir funções, são:

- `LIMIAR_SIMILARIDADE = 0.40`;
- `LIMITE_TOKENS_CONTEXTO = 300`;
- executar com e sem `ESCOPO_ATIVIDADE`.

Também é possível testar `LAMBDA_MMR`, mas isso deve ser feito chamando
`buscar_mmr`; essa variável não participa do pipeline avançado atual. Remover
reranking ou deduplicação exige alterar a composição do pipeline e deve ser
documentado explicitamente.

Na célula seguinte, descreva e aplique uma única alteração. Os valores originais
ficam guardados para restauração.
""",
    ),
    codigo(
        "atividade-alteracao-config",
        '''VALORES_ORIGINAIS = {
    "LIMIAR_SIMILARIDADE": LIMIAR_SIMILARIDADE,
    "LIMITE_TOKENS_CONTEXTO": LIMITE_TOKENS_CONTEXTO,
    "LAMBDA_MMR": LAMBDA_MMR,
}

ALTERACAO_DESCRICAO = (
    "Redução do orçamento máximo de contexto de 700 para 200 tokens, "
    "mantendo todas as demais configurações."
)  # Descreva a única alteração escolhida.
ESCOPO_EXPERIMENTO = ESCOPO_ATIVIDADE

# Escolha somente UMA opção e remova o comentário da linha correspondente:
# LIMIAR_SIMILARIDADE = 0.40
LIMITE_TOKENS_CONTEXTO = 200
# ESCOPO_EXPERIMENTO = None

if not ALTERACAO_DESCRICAO.strip():
    raise ValueError(
        "Descreva e aplique uma alteração antes de executar o experimento."
    )

print(f"Alteração escolhida: {ALTERACAO_DESCRICAO}")
''',
    ),
    codigo(
        "atividade-alteracao-execucao",
        '''etapas_alteradas = observar_etapas_pipeline(
    colecao_atividade,
    modelo_atividade,
    PERGUNTA_ATIVIDADE,
    ESCOPO_EXPERIMENTO,
)
imprimir_etapas_pipeline(etapas_alteradas)

saida_alterada_atividade = responder_com_contexto(
    colecao_atividade,
    modelo_atividade,
    PERGUNTA_ATIVIDADE,
    escopo=ESCOPO_EXPERIMENTO,
)
print(saida_alterada_atividade)
''',
    ),
    markdown(
        "atividade-restauracao-explicacao",
        r"""
### Restaurar parâmetros

Execute após coletar os resultados alterados. Isso evita que uma nova execução
do baseline ou avançado use configurações diferentes sem você perceber.
""",
    ),
    codigo(
        "atividade-restauracao",
        '''LIMIAR_SIMILARIDADE = VALORES_ORIGINAIS["LIMIAR_SIMILARIDADE"]
LIMITE_TOKENS_CONTEXTO = VALORES_ORIGINAIS["LIMITE_TOKENS_CONTEXTO"]
LAMBDA_MMR = VALORES_ORIGINAIS["LAMBDA_MMR"]

print("Parâmetros originais restaurados.")
''',
    ),
    markdown(
        "atividade-tabela",
        r"""
## G. Tabela comparativa — preencher com os resultados observados

| Critério | Baseline | Avançado | Alterado |
|---|---:|---:|---:|
| Top-1 correto? | _preencher_ | _preencher_ | _preencher_ |
| Escopo correto? | _preencher_ | _preencher_ | _preencher_ |
| Quantidade de candidatos | _preencher_ | _preencher_ | _preencher_ |
| Tokens aproximados | _preencher_ | _preencher_ | _preencher_ |
| Latência | _preencher_ | _preencher_ | _preencher_ |
| Há ruído? | _preencher_ | _preencher_ | _preencher_ |
| Contexto suficiente? | _preencher_ | _preencher_ | _preencher_ |

Use números quando existirem, mas justifique avaliações qualitativas como
“correto”, “ruído” e “suficiente” citando arquivo, página e trecho.
""",
    ),
    markdown(
        "atividade-analise",
        r"""
## H. Preencha a análise qualitativa

As métricas numéricas serão coletadas automaticamente. Complete os campos
abaixo com sua leitura das fontes e dos trechos. Respostas como “sim” ou “não”
devem ser justificadas nas observações e na análise final.

O gerador interrompe a exportação se algum campo obrigatório ficar vazio. Isso
evita produzir acidentalmente um relatório incompleto.
""",
    ),
    codigo(
        "atividade-respostas",
        '''IDENTIFICACAO = {
    "nome": "Marco Antônio Mazza Canedo dos Santos",
    "turma": "MBA GenAi",
}

AVALIACAO_MANUAL = {
    "baseline": {
        "top1_correto": "Sim",
        "escopo_correto": "Não",
        "ha_ruido": "Sim; trechos adicionais sobre TCC",
        "redundancia": (
            "Sim; a informação de 220 horas aparece em mais de um resultado"
        ),
        "contexto_suficiente": "Sim",
        "observacoes": (
            "O primeiro resultado, PPC-do-Curso-de-Ciencia-da-Computação.pdf "
            "p. 24, informa as 220 horas e a conclusão das disciplinas básicas. "
            "O metadado curso difere do escopo esperado estagio, mas o PPC "
            "contém evidência pertinente. O ruído está nos trechos adicionais "
            "sobre TCC, não na classificação do documento em si."
        ),
    },
    "avancado": {
        "top1_correto": "Sim",
        "escopo_correto": "Sim",
        "ha_ruido": "Sim",
        "redundancia": (
            "Sim; as 220 horas aparecem no Art. 14 e novamente no trecho "
            "sobre validação de PET"
        ),
        "contexto_suficiente": "Sim",
        "observacoes": (
            "A busca com escopo estagio recuperou o regulamento. O trecho "
            "dos Art. 14 e 15 já era o primeiro após a fusão e o reranking "
            "manteve essa posição. O contexto, "
            "porém, inclui trechos sobre estágio não obrigatório, validação de "
            "PET e procedimentos gerais que não respondem diretamente à pergunta."
        ),
    },
    "alterado": {
        "top1_correto": "Sim",
        "escopo_correto": "Sim",
        "ha_ruido": "Não",
        "redundancia": "Não",
        "contexto_suficiente": "Sim",
        "observacoes": (
            "Com orçamento de 200 tokens, o contexto caiu de 598 para 132 tokens. "
            "Apenas o trecho do regulamento de estágio p. 3 permaneceu e ele "
            "contém tanto a carga horária de 220 horas quanto a exigência de "
            "conclusão das disciplinas básicas."
        ),
    },
}

RESPOSTAS_FINAIS = {
    "pipeline_melhor": (
        "Parcialmente. O baseline já recuperou uma resposta correta no top-1 e "
        "teve menor latência. O avançado melhorou a adequação do escopo ao usar "
        "o regulamento de estágio, mas introduziu trechos sobre estágio não "
        "obrigatório, PET e procedimentos gerais. A melhoria inequívoca ocorreu "
        "somente após limitar o contexto a 200 tokens."
    ),
    "etapa_influente": (
        "A redução do orçamento foi a alteração controlada que demonstrou "
        "melhoria na seleção final: preservou a resposta e retirou trechos "
        "desnecessários. O escopo restringiu a busca ao regulamento, mas o "
        "reranking apenas manteve o trecho dos Art. 14 e 15 no top-1, posição "
        "que ele já ocupava após a fusão. Não foram isolados experimentalmente "
        "os efeitos de todas as demais etapas."
    ),
    "evidencia_ou_ruido": (
        "As consultas adicionais recuperaram ruído, como estágio não obrigatório "
        "e validação de PET. A redução para 200 tokens não eliminou evidência útil "
        "nesta pergunta, pois o primeiro trecho contém os dois fatos necessários; "
        "em perguntas mais amplas, o mesmo limite poderia omitir informação relevante."
    ),
    "configuracao_real": (
        "Usaria o pipeline avançado com escopo estagio, expansão de consulta, "
        "fusão RRF, reranking e orçamento de 200 tokens para esta pergunta. Em "
        "produção, o orçamento deve ser calibrado por tipo de pergunta, pois 200 "
        "tokens pode ser insuficiente para respostas que exigem várias regras."
    ),
    "contexto_para_llm": (
        "Enviaria somente 2024-regulamento-estagio.pdf p. 3, Art. 14 e Art. 15. "
        "O trecho afirma diretamente que o estágio obrigatório tem 220 horas e "
        "deve ser realizado após a conclusão das disciplinas básicas da grade."
    ),
}

CONCLUSAO = (
    "A configuração avançada com escopo estagio, reranking e orçamento de 200 "
    "tokens produziu o contexto mais conciso e suficiente entre as três "
    "configurações comparadas, para a formulação final desta pergunta. Ela preservou a regra "
    "correta do regulamento de estágio e reduziu o contexto de 598 para 132 "
    "tokens. Antes da compressão, o avançado melhorou o escopo, mas não foi "
    "inequivocamente melhor que o baseline, pois trouxe ruído e maior latência. "
    "Os trade-offs foram maior complexidade e latência que o baseline, "
    "além do risco de um orçamento pequeno omitir evidências em perguntas mais "
    "amplas. Neste caso, o contexto final é suficiente porque o Art. 14 e o Art. "
    "15 da página 3 respondem integralmente à carga horária e ao pré-requisito. "
    "A pergunta foi refinada durante os testes exploratórios; outra formulação "
    "chegou a rebaixar o trecho correto e o limite de 200 tokens excluiu a "
    "resposta. O resultado final não demonstra que esse orçamento seja ótimo "
    "ou robusto para outras formulações."
)
''',
    ),
    markdown(
        "relatorio-explicacao",
        r"""
## I. Gere o relatório para entrega

A próxima célula reúne identificação, pergunta, resultados, consultas,
contagens, tokens, latências, tabela comparativa, análise e conclusão.

Serão criados dois arquivos em `relatorios/`:

- `relatorio_atividade_rag.md`, fácil de editar;
- `relatorio_atividade_rag.html`, pronto para envio ou para abrir no navegador
  e converter em PDF por **Imprimir → Salvar como PDF**.
""",
    ),
    codigo(
        "gerador-relatorio",
        '''from relatorio_atividade import gerar_relatorio

arquivo_md, arquivo_html = gerar_relatorio(
    identificacao=IDENTIFICACAO,
    pergunta=PERGUNTA_ATIVIDADE,
    escopo=ESCOPO_ATIVIDADE,
    justificativa_escopo=JUSTIFICATIVA_ESCOPO,
    alteracao_descricao=ALTERACAO_DESCRICAO,
    avaliacao_manual=AVALIACAO_MANUAL,
    respostas_finais=RESPOSTAS_FINAIS,
    conclusao=CONCLUSAO,
    resultado_baseline=resultado_baseline_atividade,
    tokens_baseline=estimar_tokens_resultados(
        resultado_baseline_atividade
    ),
    etapas_avancado=etapas_atividade,
    saida_avancada=saida_avancada_atividade,
    etapas_alterado=etapas_alteradas,
    saida_alterada=saida_alterada_atividade,
    consultas=CONSULTAS_UNICAS,
    transformacoes_consulta=TRANSFORMACOES_CONSULTA,
)

print(f"Relatório Markdown: {arquivo_md}")
print(f"Relatório HTML: {arquivo_html}")
print("Para PDF: abra o HTML e use Imprimir → Salvar como PDF.")
''',
    ),
    markdown(
        "atividade-checklist",
        r"""
### Checklist antes de enviar

- mesma pergunta nas três configurações;
- apenas uma alteração experimental por comparação;
- consultas geradas registradas;
- resultados ligados a arquivo e página;
- latência e tokens comparados com as mesmas condições;
- respostas qualitativas justificadas com evidências;
- conclusão discute trade-offs, não apenas a melhor métrica;
- HTML ou PDF aberto e revisado antes do envio.
""",
    ),
    markdown(
        "modo-interativo-explicacao",
        r"""
## Opcional: modo interativo original

Execute esta célula somente se quiser usar o menu da professora. Digite `sair`
para encerrar. Ela contém a chamada original que foi separada da definição de
`main()`.
""",
    ),
    codigo("invocacao-main", invocacao_main, original=True),
]

notebook_didatico = {
    "cells": celulas,
    "metadata": {
        "kernelspec": {
            "display_name": "Python (aula04)",
            "language": "python",
            "name": "aula04",
        },
        "language_info": {
            "name": "python",
            "version": "3.12",
        },
        "didactic_derivation": {
            "source": ORIGINAL.name,
            "algorithm_sha256": hash_algoritmo,
            "original_code_tag": "codigo-original",
        },
    },
    "nbformat": 4,
    "nbformat_minor": 5,
}

DESTINO.write_text(
    json.dumps(notebook_didatico, ensure_ascii=False, indent=1) + "\n",
    encoding="utf-8",
)

print(f"Gerado: {DESTINO}")
print(f"Células: {len(celulas)}")
print(f"SHA-256 do algoritmo original: {hash_algoritmo}")
