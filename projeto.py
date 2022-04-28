from pandas import read_csv  # pip install pandas

import dash  # pip install dash
import dash_core_components as dcc  # pip install dash-core-components
import dash_html_components as html  # pip install dash-html-components
from dash.dependencies import Input, Output

import plotly.express as px  # pip install plotly
import plotly.graph_objects as go

#Desmatamento nos continentes (Gráfico 1)
#os dados deste grafico foram retirados https://conexaoplaneta.com.br/blog/brasil-lidera-ranking-de-paises-com-maior-perda-florestal-na-ultima-decada/
tabela = read_csv('https://raw.githubusercontent.com/LORliveira/desmatamento/main/Desmatamento%20dos%20continente')
tabela_array = tabela.values

Ano1 = []
Ano2 = []
Ano3 = [] 
for i in tabela_array:
    if i[1] == '1990-2000':
        Ano1.append(i)
        if i[1] == '2000-2010':
          Ano2.append(i)
        if i[1] == '2010-2020':
          Ano3.append(i)
          
fig = px.bar(tabela_array, x = 0, y = 2, color = 1, width = 1700, height = 800, barmode='group', labels = {'0': 'Continente', '1' :'Ano', '2':'Desmatamento'}, title = 'Mudança nas áreas florestais por continente')
fig.update_layout(paper_bgcolor = '#dbffc9')
fig.update_layout(plot_bgcolor = '#bdffca')
fig.update_yaxes(title_font_family = 'Courier New', title = 'Ganho/Perda de área florestal por hectares', title_font_color = '#000000')
fig.update_xaxes(title_font_family = 'Arial', title = 'Continentes', title_font_color = '#000000')

#Desmatamento em países europeus (Gráfico 2)
#Os dados foram retirados desse link https://fra-data.fao.org/EU/fra2020/forestAreaChange/
df = read_csv('https://raw.githubusercontent.com/Dtcbsb/projeto/main/forestAreaChange.csv')
df_array = df.values
print("Vc quer os dados de quais anos?")
print("1 - 1990-2000\n2 - 2000-2010\n3 - 2010-2015\n4 - 2015-2020\n5 - Todos os Anos")
x = int(input())
vetor1 = [] 
if x == 1:
    for linha in df_array:
        if linha[1] == "1990-2000":
            vetor1.append(linha)
if x == 2:
    for linha in df_array:
        if linha[1] == "2000-2010":
            vetor1.append(linha)
if x == 3:
    for linha in df_array:
        if linha[1] == "2010-2015":
            vetor1.append(linha)
if x == 4:
    for linha in df_array:
        if linha[1] == "2015-2020":
            vetor1.append(linha)
if x ==5:
    vetor1=df_array
fig = go.Figure()
fig = px.bar(vetor1, x=1, y=2, color= 0, 
             labels= {'0':"Países",'1':"Ano", '2':"Área Desmatada em Hectares"},
             )
fig.update_layout(
font_color = 'white',
paper_bgcolor="#242424", 
plot_bgcolor="#242424",
title="Desmatamento na Europa",
)

#Desmatamento na América do Norte (Gráfico 3)
df2 = read_csv('https://raw.githubusercontent.com/filipe604/projeto/main/annual-change-forest-area%20(4).csv')
df2_array = df2.values
canada_d = []
unites_states_d = []
mexico_d = []

for linha in df2_array:
  if linha[0] == 'United States': 
    unites_states_d.append(linha[3])
  elif linha[0] == 'Mexico':
    mexico_d.append(linha[3])
  elif linha[0] == 'Canada':
    canada_d.append(linha[3])

paises = [canada_d ,unites_states_d , mexico_d]
anos = [1990, 2000, 2010, 2015]
px.bar( y=anos , x=paises ,barmode ='group', orientation='h' , title='Desflorestamento na América do Norte' , labels={'y':'Year' , 'value':'Net forest conversion', 'variable':'Paises' , 'wide_variable_0':'United States' , 'wide_variable_1':'Mexico' , 'wide_variable_2':'Canada'})

#Desmatamento por queimadas na Amazônia Brasileira (Gráfico 4)
#Fonte :https://www.kaggle.com/code/andreauxueamaya/deforestaci-n-en-amazonas-incendios-forestales/data?select=amazon.csv
df3_incendios = read_csv('https://raw.githubusercontent.com/2ez4calvin/graficos_teste/main/amazon.csv', encoding='latin-1') 

#Passando os valores do dataframe para uma lista
df3_incendios = df3_incendios.values 

#Criando uma lista vazia para cada estado
Acre = []
Mato_Grosso = []
Amazonas = []
Rondonia = []
Roraima = []
Para = []
Tocantins = []
Amapa = []
Maranhao = []

#Criando um filtro apenas para os estados selecionados, que no caso são os estado da Amazonia Legal
C = 0 #Contador
while C < len(df3_incendios):
  X= df3_incendios[C] #Linha que a estrutura está
  if X[1] == "Pará":
    Para.append(X)
  elif X[1] == "Acre":
    Acre.append(X)
  elif X[1] == "Amapa":
    Amapa.append(X)
  elif X[1] == "Amazonas":
    Amazonas.append(X)
  elif X[1] == "Maranhao":
    Maranhao.append(X)
  elif X[1] == "Mato Grosso":
    Mato_Grosso.append(X)
  elif X[1] == "Rondonia":
    Rondonia.append(X)
  elif X[1] == "Roraima":
    Roraima.append(X)
  elif X[1] == "Tocantins":
    Tocantins.append(X)
  C = C + 1

#Jutando todos os estados para formar uma lista com todos os dados sobre queimadas dos estados legais da amazonia
array_EstadosLegaisAmazonia = Acre + Mato_Grosso + Amazonas + Rondonia + Roraima + Para + Tocantins + Amapa + Maranhao

#plotando o grafico
fig = px.line(array_EstadosLegaisAmazonia, x =0, y=3, color =0,labels=
        {'0': 'Ano',
        '3' :'Número de queimadas registradas ao longo do ano'
},
      title='Número de queimadas registradas na Amazonia Legal de 1998 a 2017')
              
fig.update_layout(
    autosize=True,
    font_color="black",
    title_font_color="black",
    paper_bgcolor="white", 
    )


#Desmatamento no Cerrado (Gráfico 5)
#fonte: http://terrabrasilis.dpi.inpe.br/app/dashboard/deforestation/biomes/cerrado/increments
dt = read_csv("https://raw.githubusercontent.com/Arthrok/cerrado/main/cerrado%20(2).csv")

tt1 = dt.values

v1 = [] 
v2 = []
v3 = []
v4 = []

#tt1 é uma matriz 33x3
#tt1[i][j], i = linha, j = coluna

#tt1[i][0] --> passa pelos estados
#tt1[i][1] --> passa pela área desmatada
#tt1[i][2] --> passa pelos anos

for i in range (len(tt1)): #33 linhas de dados
    v1.append(tt1[i][0]) #armazena os estados em v1
    if tt1[i][2] == 2021: #checa o ano
        v2.append(tt1[i][1]) #adiciona os valores do desmatamento em v2
    if tt1[i][2] == 2020:
        v3.append(tt1[i][1])
    if tt1[i][2] == 2019:
        v4.append(tt1[i][1])

fig = go.Figure()
fig.add_trace(go.Bar(
    x=v1,
    y=v2,
    name='2021',
    marker_color='#389fd6'
    
))
fig.add_trace(go.Bar(
    x=v1,
    y=v3,
    name='2020',
    marker_color='#adfc92'
))
fig.add_trace(go.Bar(
    x=v1,
    y=v4,
    name='2019',
    marker_color='#d6d138'
))

fig.update_layout(
  barmode='group', 
  xaxis_tickangle=-45,
  font_color = 'white',
  paper_bgcolor="#242424", 
  plot_bgcolor="#242424",
  title="Área de Desmatamento no Cerrado",
  xaxis_title="Estado",
  yaxis_title="Área Desmatada (Km2)",
)

# AQUI VEM AS DEFINIÇÕES DO CSS

# Inicializar o Dash na variável app
app= dash.Dash(__name__, title= 'Desmatamento ao redor do mundo' )

#Layout, pro gráfico aparecer
app.layout = html.Div(
#AQUI VAI RETORNAR OQ FOI COLOCADO NO CSS
)

#alterar os gráficos SE FIZERMOS
@app.callback()

if __name__ == "__main__":
  app.run_server(debug=True)
