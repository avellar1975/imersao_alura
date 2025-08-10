# Imersão Dados com Python

# Links:
- [Guia de Mergulho](https://alura.tv/guiademergulhodadoscompython)
- [Plataforma Imersão](https://cursos.alura.com.br/imersao/imersao-dados-python)

# Fonte de dados:

https://www.ipeadata.gov.br/

## Produto Interno Bruto (PIB) (BM12_PIB12)
- Frequência: Mensal de 1990.01 até 2025.06
- Fonte: Banco Central do Brasil, Boletim, Seção Atividade Econômica (Bacen / Boletim / Ativ. Ec.)
- Unidade: R$ (milhões)
- Comentário: O Produto Interno Bruto (PIB) denominado como PIB mensal é um indicador com frequência mensal produzido pelo Banco Central do Brasil (BCB) para utilização no cálculo da relação entre agregados econômicos mensais (como dívida pública, saldo em transações correntes e saldo de crédito) e o PIB.Elaboração Bacen: estimativa é feita via interpolação dos valores trimestrais já divulgados ou dos projetados, não se tratatando de cálculo do PIB a partir de informações primárias. Nota: Este cálculo mensal é feito uma vez que o PIB calculado oficialmente no Brasil pelo IBGE, é divulgado com frequência trimestral, ao passo que várias informações econômicas compiladas pelo Banco Central são mensais. Mais informações: SGS- Sistema de Gerenciamento de Séries Temporais, Banco Central.
- Atualizado em: 11/07/2025
- dataset: `data/pib.csv`

## Índice nacional de preços ao consumidor amplo (IPCA) geral: taxa de variação (PRECOS12_IPCAG12)
- Frequência: Mensal de 1980.01 até 2025.06
- Fonte: Instituto Brasileiro de Geografia e Estatística, Sistema Nacional de Índices de Preços ao Consumidor (IBGE/SNIPC)
- Unidade: (% a.m.)
- Comentário: O Índice Nacional de Preços ao Consumidor Amplo (IPCA) mede a inflação de um conjunto de bens e serviços comercializados no varejo, referentes ao consumo pessoal das famílias, cujo rendimento varia entre 1 e 40 salários mínimos, visando uma cobertura de 90 % das famílias pertencentes as áreas urbanas de abrangência do Sistema Nacional de Índices de Preços ao Consumidor (SNIPC), qualquer que seja a fonte de rendimentos. É calculado a partir dos resultados dos índices regionais, utilizando-se a média aritmética ponderada e cuja a variável de ponderação é o Rendimento Familiar Monetário Disponível, tendo como fonte de informação a Pesquisa de Orçamentos Familiares - POF. O IPCA tem sido utilizado pelo Banco Central do Brasil como principal parâmetro de monitoramento do sistema de metas de inflação desde a implementação do sistema no ano de 1999. Nota: O índice de agosto de 1991, excepcionalmente, foi calculado pelo IBGE como média geométrica dos valores observados em julho e setembro. Por isso, as taxas de variação apresentadas para agosto e setembro de 1991 são iguais. Mais informações: Para compreender o INPC ; Indicadores IBGE ; Sistema Nacional de Índices de Preços ao Consumidor e "Contabilidade Social", Feijó & Ramos, 4ª ed. Revisada e Ampliada.
- Atualizado em: 10/07/2025
- dataset: `data/ipca.csv`

## Taxa de desocupação das pessoas de 14 anos ou mais de idade, na semana de referência - mensalizada (PNADC12_TDESOCM12)
- Frequência: Mensal de 2012.01 até 2025.05
- Fonte: Instituto de Pesquisa Econômica Aplicada
- Unidade: (%)
- Comentário: Percentual de pessoas desocupadas em relação às pessoas na força de trabalho na semana de referência. Percentual das pessoas economicamente ativas que estavam procurando trabalho. Elaboração IPEA: As séries mensalizadas são estimativas não oficiais referentes a meses exatos, baseadas nas séries correspondentes da fonte IBGE_PNAD Contínua e na identificação dos meses de 97,9% das observações disponíveis nos microdados públicos 2013-2019 da pesquisa, conforme descrito em nota técnica nº 62. Mais informações: Nota Técnica nº 62 - Valor Impreciso por mês exato: Microdados e Indicadores mensais baseados na PNAD CONTÍNUANotas metodológicas - PNAD Contínua e Glossário - PNAD Contínua - mensal.
- Atualizado em: 27/06/2025
- dataset: `data\desocupacao.csv`

# Análise, preparação e limpeza dos dados

- Procedimentos no arquivo `data\notebooks\analise_dados.ipynb`

# Criação de ambiente virtual

- Foi criado ambiente através do `pip -m venv .venv`
- Gerado o arquivo `requirements.txt` através de `pip freeze`

# Criação de arquivo tratado para ser utilizado no Dashboard

- Para garantir que o tipo parquet funcione precisa ser instalada a biblioteca: `pip install --upgrade pyarrow`

# Criação da interface do Dashboard no Streamlit 

- arquivo `app.py`
- comando local `streamlit run app.py`

# Publicação no site Streamlit
- Atualizar os arquivos no github
- Criar uma conta no site https://streamlit.io/
- Criar app vinculando ao repositório e ao arquivo `app.py`
- Meu exemplo foi publicado em https://imersao-alura-indicadores.streamlit.app/

