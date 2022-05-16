**Disclaimer**: O Contexto a seguir, é completamente fictício, a empresa, o contexto, as perguntas de negócio foram criadas apenas para o desenvolvimento do projeto, e se baseiam em um desafio do Kaggle.

# HEALTH INSURANCE CROSS SELL 

![image](https://user-images.githubusercontent.com/104724574/168601239-f561d08c-cfad-4226-ade7-4b6ec948cea8.png)

## Contexto de negócio
Indian Not Indigene Insurance Company é uma companhia indiana especializada na oferta de seguros de saúde e automóveis, sendo a maior player do mercado na megalopole de Mumbai. Com o intuito de aumentar suas erceitas anuais e criar um ecossiema maior de clientes, a diretoria passou a seguinte tarefa para o seu time de cientista de dados: Identificar clientes que já possuem o seguro de saúde da companhia e indicar quais deles teriam uma maior chance de aderirem ao seguro veicular visto que os recursos para a realização de contato e oferta sao limitados. Para auxliar a execução de tal projeto, previamente foi enviado junto com a renovação anual do seguro uma guia a qual os clientes responderam se no momento gostariam de adquirir algum seguro veicular e se ja posuiam algum.

## Dados
O conjunto de dados utilizado nesse projeto estão disponíveis na plataforma do Kaggle no endereço: https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction. O dataset possui os seguintes atributos:

O DataSet possui as seguintes informações.


**Id** - numero de identificação (ID) unico de cada estabelecimento

**Gender** -Genero do clientr.

**Age** - Idade do cliente.

**Driving_License** - 0: Clientes que não possuem CNH. 1: clientes que possuem CNH

**Region_Code** - Código unico da região do cliente.

**Previously_Insured** - 0: Clientes que não possuem seguro veicular. 1: clientes que possuem seguro veicular

**Vehicle_Age** -Idade do veiculo

**Vehicle_Damage** - 0: Clientes que não tiveram o veiculo danificado. 1: clientes que tiveram seus veiculos danificados

**Annual_Premium** - A taxa anual que o cliente terá que desembolçar

**PolicySalesChannel** - Código anonimo referente ao canal de contato e seus diferentes agentes

**Vintage** - Número de dias desde que o cliente contratou a empresa

**Response** - 0: Clientes que não possuem interesse em contratar seguro veicular. 1: clientes que possuem interesse em contratar seguro veicular


## Planejamento da solução baseado na metodologia CRISP

1. **Entendimento do negócio*** - Busca entender de forma mais profunda o real problema do negócio e definir os objetivos para a resolução do negócio. Neste caso especifico, foi decidido que o objetivo será a realização de um modelo de machine learning para a predição das vendas como as métricas afetam o fluxo de vendas e consequentemente a predição. Além disto, também foi definida hipóteses iniciais que deverão ser validadas através da exploração de dados.

2. **Coleta de dados** - Acesso a plataforma do Kaggle para download dos arquivos que serão usados.

3.**Limpeza dos dados** - Os dados são rigorosamente analisados para se verificar dados nulos (NA), outliers, transformação de tipo de variável e qualquer outra irregularidade visando assim criar um dataset mais coeso para a análise na próxima etapa.

4. **Exploração dos dados** - Nessa etapa os dados são analisados de forma isolada (univariada) e em conjunto (valoradas) buscando achar as variáveis que melhor se relacionam e causam maior impacto nas vendas. O uso de bibliotecas de Python que criam gráficos, como a Seaborn, auxilia na criação de um maior conhecimento e entendimento do comportamento dos dados. Nessa parte as hipoteses inicias tambem sao analisadas e ao somar o resultado de tal processo e o da analise das relaçoes das variaveis se é possivel gerar insights que axuliaram tanto nas seguintes etapas do projeto quanto para dar uma nova perspectiva da empresa para o time de negocios.  

5. **Preparação dos dados** - Visa transformar, balancear e regularizar os dados a fim de que incoerências não interfiram no resultado dos algoritmos de machine learning. 

6. **Feature Selection** - Nesta etapa o objetivo é identifiar as variáveis que causam mais impacto no modelo afim de criar o mais precisso possível

7. **Aplicação dos algoritmos de machine learning** . Com o auxílio da cross validation, os melhores modelos de machine learning foram selecionados, treinados e testados com partes diferentes do dataset. Nesta etapa foram escolhidos os algoritmos de machine learning que seriam usados e então os mesmos foram treinados com os dados. 

7. **Model Performance** - Apos a selecao do melhor mdoelo foi utilizado se é avaliada a capacidade de aprendizado do modelo em um novo conjunto de dados visando descobrir a real eficiência do mesmo.

8. **Deploy do modelo em produção** - O modelo foi colocado em produção no ambiente cloud Heroku para que as predições possam ser utilizadas através de requisições a uma API e possa ser facilmente acessado via bot do Telegram.

## MELHORES INSIGHTS

1. Clientes mais novos possuem maior propensão de querer contratar o seguro em decorrência da pouca experiência em dirigir

**Falso**, Clintes em meia idade ( dos 35-55) possuem maior interesse em contratar um seguro veicular

![image](https://user-images.githubusercontent.com/104724574/168607111-8ab591fa-95ee-49d0-ac6b-69d7eef69d7c.png)


2. Lojas com competidores mais próximos deveriam vender menos.

**Falso**, lojas com competidores nas proximidades tendem a vender mais

![image](https://user-images.githubusercontent.com/104724574/168181284-511ea1b6-b639-40ef-bcd2-a48766689190.png)

3. Lojas com promoções ativas por mais tempo vendem menos, depois de um certo periodo de promoção

**Falso**, lojas com promoções ativas a mais tempo vendem menos depois de certo período de tempo

![image](https://user-images.githubusercontent.com/104724574/168181165-766b0c05-d498-43ea-b788-bffb91011ef5.png)


4. Lojas deveriam vender mais ao longo dos anos.

**Falso**, o fluxo de vendas anuais estão em constante caimento

![image](https://user-images.githubusercontent.com/104724574/168180602-1b8ab372-a741-4650-81ef-8e8e16c91bc5.png)


##### OBS: Quando tal dataset foi publicado os dados de 2015 ainda não estavam fechado, entretanto é perceptivel a decaděcia do volume de vendas.

##Machine learning Models

Algoritmos utilizados para a predição foram:
 • Modelo e média 
 • Linear Regression
 • Linear Regression Regularized (Lasso)
 • Random Forest Regressor
 • XGBoost Regressor
 
 • MAE (Mean Absolute error) - Mostra o erro médio absoluto do modelo, tanto para mais quanto para menos.
 • MAPE (Mean Absolute percentage error) - Erro médio absoluto em percentual.
 • RMSE (Root mean squared error) - Erro médio absoluto quadrado, erro médio absoluto elevado ao quadrado. Não é a melhor métrica para uma análise de negócios, porém é muito util para avaliar a performance do modelo em si.
 
 ![image](https://user-images.githubusercontent.com/104724574/168181789-b3dfbf25-09e5-4846-8a4e-16e067a44a37.png)
 
 Após a aplicação do Cross Validation e Fine Tuning optei por usar o XGBoost como modelo base visto que era uma modelo mais leve e rápido em compração com o de Random Forest 

![image](https://user-images.githubusercontent.com/104724574/168182276-b8d2d989-bb04-4f74-9af6-23d765d9d8d6.png)

## Resultados
Apòs a tradução da performance do algoritmo de machine learning foi possivel demonstrar de maneira facil de se absorver qual seria o arrecadamento de cada loja no período estipulado

![image](https://user-images.githubusercontent.com/104724574/168182378-403c5159-bd52-4b5a-8f4b-6697f1ffd8e4.png)

## Modelo em produção
 
  •  A API foi hospedada na Cloud Heroku e pode ser acessada aprtir deste url: https://rossmann--sales--prediction.herokuapp.com/rossmann/predict
  
  • O bot Telegram esta disponivel atraves deste link: t.me/rossmann_week_prediction_bot
    Para a consulta individual e rápida de alguma predição, basta entrar em contato com o Bot pelo link acima e digitar o número da loja
    
 ![image](https://user-images.githubusercontent.com/104724574/168182928-58c7abf1-8f3e-4bb9-8699-b134f8604187.png)

 
 ## Conclusão
 
 Com o resultado deste projeto tivemos uma performance satisfatoria visto que o modelo, mesmo sendo simples, apresentou um baixo erro (em comparação com a grandeza de valores do fluxo de vendas).
