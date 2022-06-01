**Disclaimer**: O Contexto a seguir, é completamente fictício, a empresa, e os as perguntas de negócio foram criadas apenas para o desenvolvimento do projeto, e se baseiam em um desafio do Kaggle.

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


2. Homens causam mais acidentes.

**Verdadeiro**, homens em média  envolvem em mais acidentes

![image](https://user-images.githubusercontent.com/104724574/168803996-dcad1b20-37b3-4769-b95d-3b330da85c86.png)

3. Pessoas com veículos mais novos tendem a serem mais propícias a contratar um seguro veicular

**FALSO**, pessoas com veículos acima de 2 anos serão mais propicias para a contratação de seguro veicular

![image](https://user-images.githubusercontent.com/104724574/168929476-1f607a84-2f54-4526-9036-fdc2bfe298ac.png)


## Machine learning Models

Algoritmos utilizados para a predição foram:

 • KNN
 
 • Logistic Regression
 
 • Extra Trees
 
 • Decision Tree
 
 • XGBoost Regressor


 
 Após a analise dos resultados, optei por usar o Logistic Regression como modelo base visto que era uma modelo mais leve os de Decision Tree e ja entrega um resultado satisfatorio
 
![image](https://user-images.githubusercontent.com/104724574/168929674-ed39c541-f2c5-4a7b-be76-be2b6dfe4c8d.png)

## Resultados
Com base no modelo de machine learning aplicado, foi possivel conceber que, na base em questao com 76 mil clientes, ao se realizar 28120 ligações, respectivo a cerca de 36% dos clientes totais, seria possível cobrir 80% dos clientes potencialmente interessados de acordo com o perfil criado pelo algoritmo.

![edit](https://user-images.githubusercontent.com/104724574/168930878-165d8d68-2bb0-40e4-a650-e23ed767891b.png)


## Modelo em produção
 
  •  A API foi hospedada na Cloud Heroku e pode ser acessada aprtir deste url: https://insurance--cross--sell.herokuapp.com/predict

 
 ## Conclusão
 
 Com o resultado deste projeto tivemos uma performance satisfatoria visto que o modelo, mesmo sendo simples, apresentou uma solução mais inteligente ofertar produtos com maior chance de exito do que apenas ligar aleatoriamente para os 76000 clientes
