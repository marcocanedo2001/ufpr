# Plano do Projeto: Identificador de Idioma por Frequência de Letras

## Resumo

- Criar um projeto dedicado e modular (separado dos exercícios), usando arquitetura `src`.
- Usar `letter_frequency.csv` como fonte de perfis de idioma.
- Expor execução por CLI com argumentos.
- Usar distância euclidiana como métrica principal e saída no formato pedido no enunciado.
- Incluir README específico do projeto e atualizar `environment.yml` com `requests`.

## Mudanças de Implementação

- Estruturar um novo diretório de projeto com pacote Python modular (`download`, `limpeza`, `frequencia`, `perfis`, `comparacao`, `cli`).
- Implementar fluxo ponta a ponta:
1. baixar texto da URL com `requests`;
2. remover tags HTML via regex simples e decodificar entidades;
3. normalizar (minúsculas, remover acentos com `unicodedata`, manter apenas `a-z`);
4. calcular frequência relativa por letra (`a-z`);
5. carregar perfis do CSV (separador `;`, remover `%` e `*`, considerar apenas letras `a-z`);
6. comparar com distância euclidiana e selecionar menor distância.
- Definir idiomas padrão do esqueleto: `Portuguese`, `German`, `Finnish`.
- Gerar mensagem final: `O texto está em [idioma] com grau de similaridade X`.
- Atualizar `environment.yml` para incluir `requests`.
- Criar README do projeto com instalação, comando de execução e exemplos.

## APIs/Interfaces Públicas

### Funções principais do pacote

1. `baixar_texto(url: str, timeout: int = 15) -> str`
2. `limpar_texto(texto_bruto: str, remover_acentos: bool = True) -> str`
3. `calcular_frequencia(texto_limpo: str) -> dict[str, float]`
4. `carregar_perfis_csv(caminho_csv: str, idiomas: list[str]) -> dict[str, dict[str, float]]`
5. `comparar_perfis(freq_texto: dict[str, float], perfis: dict[str, dict[str, float]]) -> tuple[str, float, dict[str, float]]`

### CLI

1. `--url` (obrigatório)
2. `--csv` (default: `letter_frequency.csv`)
3. `--langs` (default: `Portuguese,German,Finnish`)
4. `--timeout` (default: `15`)
5. `--top` para exibir ranking resumido (default: `3`)

## Plano de Testes (manual, sem pytest nesta etapa)

- URL em português: classificar como `Portuguese`.
- URL em alemão ou finlandês: classificar conforme idioma de referência.
- URL inválida/falha de conexão: erro amigável e término com código não zero.
- Conteúdo vazio após limpeza: mensagem clara de impossibilidade de classificar.
- CSV ausente/coluna de idioma não encontrada: erro descritivo.

## Premissas e Defaults

- Detecção baseada apenas em letras latinas `a-z` após normalização.
- Extração de texto HTML será propositalmente simples (regex), sem `BeautifulSoup`.
- Similaridade exibida será derivada da distância (ex.: `1 / (1 + distância)`), com valor formatado para leitura.
- Sem suíte automatizada nesta versão; validação inicial será por cenários manuais documentados.
