# Executar os notebooks

## Ambiente local

O ambiente de referência usa Python 3.12. Crie um ambiente virtual e instale
`requirements.txt` conforme o README. Execute `python -m jupyterlab` na raiz.

Reinicie o kernel e execute todas as células em ordem. Alterar uma célula antiga
sem executar novamente as dependentes pode produzir resultados inconsistentes.
O piloto informa versões, fixa a semente e gera seus próprios dados.

`requirements.txt` fixa as versões das bibliotecas do piloto e do executor de notebooks;
para a interface JupyterLab, permite a faixa 4.4 até antes da versão 5.
Não é um lock completo das dependências transitivas. Diferenças entre plataformas e bibliotecas numéricas
podem causar pequenas variações de ponto flutuante.

## Google Colab

Abra o link no README ou faça upload do `.ipynb`. Use um ambiente de CPU.
O piloto não depende de arquivos do repositório nem de serviços externos.
Se necessário, instale as duas dependências em uma célula adicional:

```python
%pip install numpy==2.3.5 matplotlib==3.10.8
```

Se o Colab solicitar, reinicie a sessão após a instalação. A interface e o ambiente
do Colab podem mudar; o link de abertura não constitui confirmação de execução
nessa plataforma. Compare as versões impressas pelo notebook com as documentadas.

## Verificação automática local

```bash
python scripts/validar_notebooks.py
```

O comando valida o formato e executa cada notebook com kernel novo, com limite de
120 segundos por célula. Erros interrompem o processo. Os resultados são gravados
em `build/executed/`, preservando o diretório de cada capítulo.

Esse protocolo é adequado ao piloto leve. Notebooks futuros com GPU, modelos
grandes ou serviços externos precisarão de instruções e ambientes específicos.
As dependências desses capítulos serão adicionadas quando forem implementados.
