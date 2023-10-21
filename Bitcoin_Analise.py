import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go  # Correção aqui

# Para ler os dados da planilha:
Base_Dados = pd.read_excel('E:\\Bitcoin analise\\Dados_Bitcoin (2).xlsx')

# Para verificar os dados:
print(Base_Dados.head(10))  # Use 'print' para exibir os dados no console

# Defina o índice
Base_Dados.set_index('Date', inplace=True)

# Gráfico de Linhas
fig = px.line(Base_Dados, y='Close')

# Plotar
fig.show()

# Gráfico 2 - Com média móvel - A diferença é que com este eu consigo costumizar muito mais:

# Gerar médias móveis
Media_Movel = Base_Dados['Close'].rolling(5).mean()
Media_Tendencia = Base_Dados['Close'].rolling(30).mean()

# Criar Dashboard

# Criando uma Figura
Figura = go.Figure()  

# Adicionando o primeiro eixo
Figura.add_trace(
    go.Scatter(  
        x=Base_Dados.index,
        y=Base_Dados['Close'], 
        mode='lines',
        name='Fechamento',
        line=dict(color='#ff7f0e'),  
        opacity=0.5,
    )
)

# Adicionando a média
Figura.add_trace(
    go.Scatter( 
        x=Base_Dados.index,
        y=Media_Movel,
        mode='lines',
        name='Média Móvel',
        line=dict(color='#d62728'),  
        opacity=0.5,
    )
)

# Média por tendência 
Figura.add_trace(
    go.Scatter(  
        x=Base_Dados.index,
        y=Media_Tendencia,
        mode='lines',
        name='Tendência',
        line=dict(color='#2ca02c'), 
    )
)

# Ajustes no layout
Figura.update_layout(

    # Título
    title='Análise do fechamento Bitcoin',
    # Tamanho
    title_font_size=20, 

    # Ajustando eixo x
    xaxis=dict(
        title='Período Histórico',
        title_font_size=14,  
        tickfont_size=10,
    ),

    # Ajustando eixo y
    yaxis=dict(
        title='Preço fechamento ($)',
        title_font_size=14,  
        tickfont_size=10,
    ),

    # Parâmetros para Legenda
    legend=dict(
        y=1,
        x=1,
        bgcolor='rgba(255, 255, 255, 0.5)', 
        bordercolor='rgba(255, 255, 255, 0.5)' 
    )

)

# Plotar o segundo gráfico
Figura.show()
