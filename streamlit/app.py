import pandas as pd
import streamlit as st  
import plotly_express as px

#crear pagina
st.set_page_config(page_title=  "dashboard",
                     page_icon=':bar_chart:',
                     layout= 'wide')

#cargar el dataset
df = pd.read_parquet(r'.\rawdatacompañeros\VgasElect.parquet')

#deploy el dataset

###st.dataframe(df) #este es para ver el dataset antes de filtros
#para mostrar el data ser con lso filtros, este debe ir despues de los filtros

# deploy select o models

st.sidebar.header('filtro')

make= st.sidebar.selectbox( # el filtro del motor kw con espacio no lo considera.
    "selecciona el tipo de motor:", # texto
    options=df['Make'].unique(), # dato a filtrar
    #default=df['Make'].unique()
)
# Filtrar modelos basados en la selección de Make
filtered_models = df[df['Make'] == make]['Model'].unique()

# Filtro del Model
modelo = st.sidebar.selectbox(
    "Selecciona el modelo:",
    options=filtered_models,
    #default=filtered_models no se ocupa en selectbox
)


# mostrar solo lo seleccionado

df_selection= df.query(
        "Make == @make & Model == @modelo  "  
        #para agregar otro filtro se pone "& DatasetColumn == @funcion"
)

#________________________________________ numero de vehiculos en flota
# Cuadro de texto para ingresar un número
numero = st.sidebar.number_input(
    "Número de vehículos:",
    min_value=0,  # valor mínimo permitido
    max_value=1000,  # valor máximo permitido
    value=1  # valor predeterminado
)

# Mostrar el número ingresado
st.write(f"El número ingresado es: {numero}")


#________________________________________ MAIN PAGE____________________________
st.dataframe(df_selection) # mostrar e dataset con filtros
#top KPIs

co2=int(df_selection['CO2 rating'].iloc[0])
leaf_rating= ':seedling:'* co2

emision= df_selection["CO2_g/km_x"].iloc[0]
tipoVehiculo= df_selection["VClass"].iloc[0]

#Columnas

left_column, right_column, middle_column = st.columns(3)

with middle_column:
    st.subheader(f'nivel de CO2:{co2}')
    st.subheader(f'{leaf_rating} ' )

with left_column:
    st.subheader(f'emision de CO2 por galon/km')
    st.subheader(f'{emision} ' )

with right_column:
    st.subheader(f'tipo de vehiculo')
    st.subheader(f"{tipoVehiculo}"  )

st.markdown('**********')
