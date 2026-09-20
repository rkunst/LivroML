# Padrão didático dos notebooks

Cada notebook deve conter:

1. Título, capítulo, objetivos, pré-requisitos e tempo estimado.
2. Origem dos dados, recursos necessários e instruções de execução.
3. Conceito matemático antes da implementação, com notação coerente com o livro.
4. Células curtas, comentários em português e nomes descritivos.
5. Experimento reproduzível, com semente e versões registradas.
6. Gráficos com unidades, títulos e legendas; cores não devem ser a única distinção.
7. Interpretação dos resultados, hipóteses e limitações.
8. Atividades complementares e referências.
9. Identificação das licenças do código e do conteúdo.

As atividades do notebook complementam os exercícios do capítulo e não alteram
sua numeração. Soluções comentadas selecionadas serão organizadas posteriormente.

Execute o notebook inteiro com kernel novo antes de propor uma alteração.
Use verificações numéricas quando ajudarem a detectar erros matemáticos ou de implementação.
Evite caminhos absolutos, instalações automáticas, dependência de células executadas
fora de ordem e downloads silenciosos. Documente custos e requisitos quando existirem.

Nas tarefas preditivas, ajuste transformações e modelos apenas com dados de treino;
reserve validação e teste conforme o protocolo do capítulo. Um experimento de
otimização sobre uma amostra fixa deve deixar claro que não mede generalização.
