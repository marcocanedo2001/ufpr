# FLLM — índice de aulas

Organização local em 17/10/2026. O cronograma é uma previsão: suas datas não comprovam quando cada arquivo foi ministrado. Datas nos novos nomes vêm da previsão apenas quando número e tema locais concordam; FLLM/aula01 também tem confirmação explícita no README.

## Cronograma oficial

| Aula | Data prevista | Professor | Tema / ressalva |
| --- | --- | --- | --- |
| 1 | 2026-03-20 | Luiz | Introdução a ML |
| 2 | 2026-04-11 | Luiz | Redes neurais |
| 3 | 2026-04-18 | Luiz | Representação |
| 4 | 2026-05-30 | Luiz | Transformers |
| 5 | 2026-06-12 | Anderson | Aprendizado de LLMs |
| 6 | 2026-06-13 | Anderson | Customização e RLHF |
| 7 | 2026-09-12 | Paulo | Tipos e ecossistema de LLMs |
| 8 | 2026-09-26 | Paulo | Fine tuning com Hugging Face |

[Fonte oficial](https://docs.google.com/spreadsheets/d/1l8SJOTVv6wWNRoyQdA2cZInqnQPGGV35299P12j4uCw/edit?gid=762817580#gid=762817580). As divergências entre abas foram mantidas, sem inventar reposições ou aulas ausentes.

## Projetos e materiais locais

| Diretório atual | Conteúdo identificado | Associação e limites |
| --- | --- | --- | --- |
| [aula01_2026-03-20_introducao-aprendizado-maquina](aula01_2026-03-20_introducao-aprendizado-maquina/) | Introdução a ML e laboratório de métricas | README confirma 20/03/2026, Luiz, em concordância com o cronograma. |
| [aula02_2026-04-11_redes-neurais](aula02_2026-04-11_redes-neurais/) | Redes neurais e perceptron | Número, PDF RedesNeurais1 e notebook de redes concordam com 11/04; data usada no nome é a prevista. |
| [aula07](aula07/) | Redes siamesas e MNIST | Diverge de tipos/ecossistema de LLMs previsto para aula07. Não renumerada para outra aula por inferência. |
| [aula08_2026-09-26_fine-tuning-modelos](aula08_2026-09-26_fine-tuning-modelos/) | Especialização de modelos pré-treinados, LFW e Llama | Número e materiais sobre ajuste de modelos pré-treinados concordam com fine tuning de 26/09; data usada no nome é a prevista. Alias antigo preserva o ambiente. Este projeto e seu alias continuam apenas locais, pois não eram rastreados antes da organização. |

As exclusões preexistentes de arquivos em `aula05/` foram preservadas; a pasta não foi recriada. `aula07` mantém nome e conteúdo apesar da divergência temática.

## Compatibilidade

Aliases simbólicos, sem cópias duplicadas:

| Caminho antigo | Destino | Motivo |
| --- | --- | --- |
| `aula01_introducao_aprendizado_maquina` | `aula01_2026-03-20_introducao-aprendizado-maquina` | referência no notebook original preservado |
| `aula08` | `aula08_2026-09-26_fine-tuning-modelos` | ambiente .venv com caminhos absolutos gerados; alias somente local, sem publicação |

## Preservação

Projetos, dados, arquivos ignorados, ambientes e trabalhos pessoais foram preservados. Nenhum notebook ou projeto foi executado e nenhuma dependência foi instalada. As pastas ambíguas permanecem nos nomes originais, com data local não confirmada.

Backup recuperável e manifesto privado: `../organizacao_2026-10-17/`. A documentação de caminhos foi ajustada apenas onde necessário; notebooks, ambientes e dependências não foram reescritos. A publicação da organização inclui somente movimentações de conteúdo previamente rastreado e documentação. Materiais locais novos, ambientes e backups permanecem fora do Git público.
