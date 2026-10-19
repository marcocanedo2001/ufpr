# DSLLM Aula 08 de 16 de outubro de 2026

Deisy. Tema: áudio, imagem e vídeos. O material da professora é identificado como **Aula 04**, embora a aula esteja numerada como 08 no cronograma geral.

O pacote pessoal de slides HTML e notebook foi identificado. As cópias ficam localmente em `material/originais/`, ignoradas no Git. O repositório público conserva referências e instruções, sem republicar os arquivos originais.

## Ambiente separado

Na raiz do repositório:

```powershell
conda env create -f DSLLM/aula08_2026-10-16_audio-imagem-videos/environment.yml
conda activate dsllm-multimodal
python -m ipykernel install --user --name dsllm-multimodal --display-name "Python (DSLLM Multimodal)"
jupyter lab
```

As dependências foram mapeadas pelos imports do notebook, mas a instalação completa e a execução multimodal não foram realizadas. Este ambiente não altera o `dsllm` anterior. Whisper inclui componentes de PyTorch; valide a instalação adequada ao seu sistema antes de usar GPU. Ollama, pesos dos modelos, mecanismo de voz do sistema, mídia e projeto completo da disciplina são requisitos externos. O ZIP de slides e notebook sozinho não contém todo o laboratório.

O notebook procura o projeto com `lectures/04-multimodal-toolkit`. Preserve esse projeto e seus caminhos: mover apenas o arquivo ipynb para esta pasta não reconstrói os dados. Para o notebook original, use o kernel preparado dentro do projeto completo disponibilizado pela disciplina.

## Ordem de estudo

1. Representação de imagens e perda de informação na redução de dimensão.
2. Matriz de confusão, sensibilidade, especificidade e acurácia balanceada.
3. Amostragem temporal de vídeo e limites da interpretação de diferenças RGB.
4. Áudio, taxa de amostragem, transcrição e WER.
5. Catálogo SQL, ferramentas e evidências da execução.
6. Busca semântica textual e revisão de respostas.

Fontes no Moodle: [slides Aula 04](https://moodle.c3sl.ufpr.br/mod/resource/view.php?id=66426) e [notebook Aula 04](https://moodle.c3sl.ufpr.br/mod/resource/view.php?id=66427). Slides originais em HTML, sem PDF original confirmado para essa aula. Para leitura em PDF, use o capítulo da apostila atualizada; isso não é um PDF original da professora.
