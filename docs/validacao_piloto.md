# Validação da primeira versão

Ambiente utilizado: Python 3.12.14, NumPy 2.3.5 e Matplotlib 3.10.8.

- Formato do notebook validado com nbformat 5.11.1.
- Dez células de código executadas em ordem, em um novo processo Python.
- Gradiente analítico comparado com diferenças finitas: verificação aprovada.
- Descida do gradiente comparada com `numpy.linalg.lstsq`: diferença de parâmetros
  aproximadamente `9.91e-10`, após 156 atualizações.
- Custo final `J` aproximadamente `8.123759`; MSE de ajuste aproximadamente `16.247519`.
- Três figuras geradas e inspecionadas.

O ambiente de validação bloqueou a abertura de sockets pelo kernel Jupyter, tanto
em TCP quanto em IPC. Por isso, a execução das células foi feita diretamente em
Python, com Matplotlib em modo não interativo. Não se confirmou aqui a execução
ponta a ponta pelo script `scripts/validar_notebooks.py` com kernel Jupyter.
Também permanece pendente a execução na plataforma Google Colab.

As células do piloto são Python puro e não usam comandos especiais do IPython.
Os arquivos de revisão e gráficos gerados não são versionados; as fontes do
notebook permanecem sem saídas. O script de validação mantém a execução convencional
via nbclient para ambientes que permitem iniciar o kernel.
