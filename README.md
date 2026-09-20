# Machine Learning — material complementar

Notebooks e experimentos do livro de **Rafael Kunst**, em português brasileiro.
O material conecta os fundamentos matemáticos à implementação e à interpretação dos resultados.

**Estado:** primeira versão do notebook piloto; demais notebooks em planejamento.
O manuscrito do livro não integra este repositório.

## Comece aqui

O piloto do Capítulo 2 aborda regressão linear, mínimos quadrados e descida do gradiente.
Usa somente NumPy e Matplotlib, com dados sintéticos gerados no próprio notebook. Não requer GPU.

- [Abrir o notebook](notebooks/capitulo02/01_regressao_linear_gradiente.ipynb)
- [Executar no Google Colab](https://colab.research.google.com/github/rkunst/LivroML/blob/main/notebooks/capitulo02/01_regressao_linear_gradiente.ipynb)
- [Instruções de execução](docs/execucao.md)

A execução em Colab ainda precisa ser verificada nessa plataforma.

## Organização por capítulo

| Capítulo | Tema | Material |
|---|---|---|
| [1](notebooks/capitulo01/README.md) | Introdução | Orientações; sem notebook previsto nesta etapa |
| [2](notebooks/capitulo02/README.md) | Fundamentos matemáticos | Piloto de regressão linear e gradiente |
| [3](notebooks/capitulo03/README.md) | Aprendizado supervisionado | Regressão; classificação comparativa — planejados |
| [4](notebooks/capitulo04/README.md) | Aprendizado não supervisionado | Três notebooks — planejados |
| [5](notebooks/capitulo05/README.md) | Deep Learning | Quatro notebooks — planejados |
| [6](notebooks/capitulo06/README.md) | Aprendizado por reforço | Tabulares; DQN; PPO — planejados |
| [7](notebooks/capitulo07/README.md) | Transferência e adaptação de domínio | Visão; linguagem — planejados |
| [8](notebooks/capitulo08/README.md) | LLMs e foundation models | Geração; adaptação; RAG e avaliação — planejados |
| [9](notebooks/capitulo09/README.md) | IA agêntica | Agente único; sistema multiagente — planejados |
| [10](notebooks/capitulo10/README.md) | IA explicável | Dois notebooks — planejados |
| [11](notebooks/capitulo11/README.md) | Desafios éticos | Auditoria de viés e equidade — planejado |

Os roteiros futuros serão conferidos com o texto de cada capítulo antes da implementação.
Pastas com um README de planejamento não contêm notebooks executáveis.

## Executar localmente

Use Python 3.12 em um ambiente virtual. Na raiz do repositório:

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m jupyterlab
```

Abra o notebook e execute todas as células em ordem, a partir de um kernel reiniciado.
Para validar os notebooks sem abrir o Jupyter:

```bash
python scripts/validar_notebooks.py
```

As cópias executadas ficam em `build/executed/`; os arquivos-fonte não são sobrescritos.
Os notebooks versionados ficam sem saídas para facilitar revisão e execução independente.

## Convenções e contribuição

- [Padrão didático dos notebooks](docs/padrao_notebooks.md)
- [Licenciamento e atribuição](docs/licenciamento.md)
- [Dados e fontes externas](dados/README.md)

Para relatar um erro, informe capítulo, notebook, célula, versões e como reproduzir o problema.
Não inclua credenciais nem dados pessoais em issues ou notebooks.

## Licenças

Código Python, scripts e células de código: **MIT**, conforme [LICENSE](LICENSE).
Textos didáticos originais, células Markdown e figuras originais: **CC BY 4.0**, conforme
[LICENSE-CONTENT.md](LICENSE-CONTENT.md). Materiais de terceiros mantêm suas licenças.
Essas permissões se aplicam ao material complementar identificado aqui, não ao manuscrito do livro.
