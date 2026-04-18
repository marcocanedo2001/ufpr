# Projeto (Esqueleto): Identificador de Idioma por Frequência de Letras

Este diretório contém apenas o **esqueleto** do projeto, com assinaturas de funções e comentários `TODO`.

## Estrutura

```text
identificador_idioma/
├── README.md
├── run.py
└── src/
    └── identificador_idioma/
        ├── __init__.py
        ├── __main__.py
        ├── cli.py
        ├── comparacao.py
        ├── download.py
        ├── frequencia.py
        ├── limpeza.py
        └── perfis.py
```

## APIs esperadas

- `baixar_texto(url: str, timeout: int = 15) -> str`
- `limpar_texto(texto_bruto: str, remover_acentos: bool = True) -> str`
- `calcular_frequencia(texto_limpo: str) -> dict[str, float]`
- `carregar_perfis_csv(caminho_csv: str, idiomas: list[str]) -> dict[str, dict[str, float]]`
- `comparar_perfis(freq_texto: dict[str, float], perfis: dict[str, dict[str, float]]) -> tuple[str, float, dict[str, float]]`

## CLI prevista

Argumentos já definidos no `cli.py`:

- `--url` (obrigatório)
- `--csv` (default: `letter_frequency.csv`)
- `--langs` (default: `Portuguese,German,Finnish`)
- `--timeout` (default: `15`)
- `--top` (default: `3`)

## O que falta implementar

1. Download com `requests` e tratamento de erros de rede/URL.
2. Limpeza de HTML, normalização e remoção de acentos.
3. Cálculo de frequência relativa das letras `a-z`.
4. Leitura e parsing do CSV de perfis linguísticos.
5. Comparação por distância euclidiana e conversão para similaridade.
6. Fluxo completo da CLI e saída final no formato:
   - `O texto está em [idioma] com grau de similaridade X`

## Execução (ainda não funcional)

Este é um scaffold. Ao executar, o programa levantará `NotImplementedError` até os TODOs serem implementados.

Exemplo de comando final esperado:

```bash
python identificador_idioma/run.py --url "https://pt.wikipedia.org/wiki/Brasil"
```
