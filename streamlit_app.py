import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos
df = pd.read_csv('/ruta/a/tu/archivo.csv')

# Título de la aplicación
st.title('Visualización de Datos de Películas')

# Selector de género
selected_genres = st.multiselect('Seleccione género(s)', options=df['Genre'].unique(), default=df['Genre'].unique()[0])

# Selector de año
selected_year = st.slider('Seleccione el año', min_value=int(df['Year'].min()), max_value=int(df['Year'].max()), value=int(df['Year'].min()))

# Filtrar datos basados en selecciones
filtered_df = df[(df['Year'] == selected_year) & df['Genre'].isin(selected_genres)]

# Crear y mostrar el gráfico
fig = px.scatter(filtered_df, x='Revenue (Millions)', y='Rating',
                 size='Votes', color='Genre', hover_name='Title',
                 log_x=True, size_max=60)

st.plotly_chart(fig)
