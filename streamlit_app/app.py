import pandas as pd
import streamlit as st
import numpy as np  
# import plotly_express as px
from datetime import timedelta
import pyarrow

#crear pagina
st.set_page_config(page_title=  "Modelo de simulación",
                     page_icon=':bar_chart:',
                     layout= 'wide')

# Define los colores de la paleta
color1 = "#224040"
color2 = "#63A687"
color3 = "#7ABF9F"
color4 = "#E9F2EB"
color5 = "#8C8372"

# Funciones del Modelo de Machine Learning
#Función resumen, provee un resumen del conjunto de datos simulados, genera un unico DataFrame con el promedio de
#de cada una de las variables de interés.
def resumen(dfs):
    resultados = []
    no = 0
    for j in dfs:
        res = {"interacion": no,"trip_time":timedelta(minutes=j['trip_time'].sum()),
            "trip_time_mean":timedelta(minutes=j['trip_time'].mean()),
            "wait_time":j['wait_time'].sum(),
            "wait_time_mean":j['wait_time'].mean(),
            "trip_distance":j['trip_distance'].sum(),"trip_mean":j['trip_distance'].mean(),
            "total_amount":j['total_amount'].sum(),"amount_mean":j['total_amount'].mean(), 
            "CO_emission_total": j['CO2_emission'].sum(), "CO2_emmision_avg":j['CO2_emission'].mean(),
            "Profit": j['Utilidad'].sum()}
        resultados.append(res)
        no += 1
    return pd.DataFrame(resultados).describe()
    with col1:
        # Content for the first (narrower) column goes here
        st.write("Ingrese el inventario de sus vehiculos")


    with col2:
        # Content for the second (wider) column goes here
        st.write("Aca se muestra el resultado de la simulacion de la Huella de carbono")
        # Fill with image placeholder with full width and height
        st.image("https://via.placeholder.com/800x400", use_column_width=True, caption="Image Placeholder")
        

    



#Función interpolación empata los datos especificos del vehiculo seleccionado y devuelve genera costos y emisiones 
#de CO2. 



def interpolacion(Modelo:str, Año:int, electrico:bool,dfs:list,hour_0,hour_f):
    lista = []
    if electrico:
        filtro = electric[(electric['Model'] == Modelo) & (electric['Model year'] == Año)].reset_index()
        co2 = filtro['CO2 emissions (g/km)'].iloc[0]
        Mantenimiento = 550
        costo_gas = 0.151 * filtro['City (kWh/100 km)'].iloc[0] / 62
    else:
        filtro = fuel[(fuel['Model'] == Modelo) & (fuel['Year'] == Año)].reset_index()
        co2 = filtro['co2'].iloc[0]
        Mantenimiento = filtro['Costo_mant_anual'].iloc[0]
        costo_gas = filtro['Costo_gasolina_galon'].iloc[0]
    for i in dfs:
        i = i[(i['Hour_0'] >= hour_0) & (i['Hour_0'] <= hour_f)]
        i['CO2_emission'] = i['trip_distance'] * co2 * 1.609
        i['Mantenimiento_anual'] = Mantenimiento
        i['Costo_comb'] = i['trip_distance'] * costo_gas
        i['Utilidad'] = i['total_amount'] - i['Costo_comb'] - i['Mantenimiento_anual'] / (365 * i['trip_distance'].sum())
        lista.append(i)
    return resumen(lista)


#cargar el dataset
dfs = []
for i in range(1,1001):
    df = pd.read_parquet(f'streamlit_app/Data_sim/{i}.parquet')
    dfs.append(df)

electric = pd.read_parquet('streamlit_app/Data_sim/df_final_electrico01.parquet')
fuel = pd.read_parquet('streamlit_app/Data_sim/Eda_fuel_vehicles.parquet')
# df = pd.read_parquet('Data_sim/VgasElect.parquet')

#Generando lista de vehiculos
electric_model = electric[['Make','Model','Model year']]
fuel_model = fuel[['Manufacturer','Model','Year']].rename(columns={'Manufacturer':'Make','Year':'Model year'})
df = pd.concat([fuel_model, electric_model], axis=0).sort_values(by='Make', ascending=True)

# Filtros
st.sidebar.header('Seleccione un Vehiculo')

make= st.sidebar.selectbox( # el filtro del motor kw con espacio no lo considera.
    "Elija una marca:", # texto
    options = df['Make'].unique(), # dato a filtrar
    #default=df['Make'].unique()
)
# Filtrar modelos basados en la selección de Make
filtered_models = df[df['Make'] == make]['Model'].unique()

# Filtro del Model
modelo = st.sidebar.selectbox(
    "Selecciona un modelo:",
    options=filtered_models,
    #default=filtered_models no se ocupa en selectbox
)


# mostrar solo lo seleccionado


df_selection= electric.query(
        "Make == @make & Model == @modelo  "  
        #para agregar otro filtro se pone "& DatasetColumn == @funcion"
)

#________________________________________ numero de vehiculos en flota
# Cuadro de texto para ingresar un número
numero = st.sidebar.number_input(
    "Número de vehículos del mismo modelo:",
    min_value=0,  # valor mínimo permitido
    max_value=1000,  # valor máximo permitido
    value=1  # valor predeterminado
)

# Mostrar el número ingresado
st.title("El Baile de los Taxis: Un Análisis de la Coreografía Urbana de los diversos fabricantes de automotores")
st.write(f"La simulación se realizará con un total de {numero} unidades del modelo:")


#________________________________________ MAIN PAGE____________________________
# Selección de vehiculo
try:
    df_selected = electric[(electric['Make'] == make) & (electric['Model'] == modelo)]
    df_selected = df_selected[df_selected['Model year'] == np.random.choice(df_selected['Model year'])]
    elec = True
    año = df_selected['Model year'].iloc[0]
    st.dataframe(df_selected[['Make','Model','Model year']]) # mostrar e dataset con filtros
except:
    df_selected = fuel[(fuel['Manufacturer'] == make) & (fuel['Model'] == modelo)]
    df_selected = df_selected[df_selected['Year'] == np.random.choice(df_selected['Year'])]
    elec = False
    año = df_selected['Year'].iloc[0]
    st.dataframe(df_selected[['Manufacturer','Model','Year']]) # mostrar e dataset con filtros
# Simulación
st.write("La simulación para un día de trabajo nos proporciona la siguiente información")
sim = interpolacion(modelo,año,elec,dfs,timedelta(hours=5, minutes=0), timedelta(hours=18, minutes=0))

# co2=int(df_selection['CO2 rating'].iloc[0])
# leaf_rating= ':seedling:'* co2

# emision= df_selection["CO2_g/km_x"].iloc[0]
# tipoVehiculo= df_selection["VClass"].iloc[0]

#Columnas

left_column, right_column, middle_column = st.columns(3)

with middle_column:
#     st.subheader(f'nivel de CO2:{co2}')
#     st.subheader(f'{leaf_rating} ' )
    # st.info(f"Distancia recorrida por el taxi: ****")
    # Crea una tarjeta rectangular con los colores de fondo
    st.markdown(
        f"""
        <div style="background-color: {color1}; padding: 10px; border-radius: 10px;">
            <center><h2 style="color: {color4};">Emisiones totales</h2></center>
            <center><h2 style="color: {color4};">de CO2</h2></center>
            <center><p style="color: {color5};">{numero * sim['CO_emission_total']['mean'] / 1000:.2f} Kg</p></center>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.divider()
    st.markdown(
        f"""
        <div style="background-color: {color1}; padding: 10px; border-radius: 10px;">
            <center><h2 style="color: {color4};">Emisiones promedio por servicio</h2></center>
            <center><p style="color: {color5};">{numero * sim['CO2_emmision_avg']['mean'] / 1000:.2f} Kg </p></center>
        </div>
        """,
        unsafe_allow_html=True
    )

with left_column:
    # st.info(f"Distancia recorrida por el taxi: ****")
    # Crea una tarjeta rectangular con los colores de fondo
    st.markdown(
        f"""
        <div style="background-color: {color1}; padding: 10px; border-radius: 10px;">
            <center><h2 style="color: {color4};">Distancia</h2></center>
            <center><h2 style="color: {color4};">Recorrida</h2></center>
            <center><p style="color: {color5};">{numero * sim['trip_distance']['mean']:.2f} Millas</p></center>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.divider()
    st.markdown(
        f"""
        <div style="background-color: {color1}; padding: 10px; border-radius: 10px;">
            <center><h2 style="color: {color4};">Distancia promedio por servicio</h2></center>
            <center><p style="color: {color5};">{numero * sim['trip_mean']['mean']:.2f} Millas</p></center>
        </div>
        """,
        unsafe_allow_html=True
    )
#     st.subheader(f'emision de CO2 por galon/km')
#     st.subheader(f'{emision} ' )

with right_column:
#     st.subheader(f'tipo de vehiculo')
#     st.subheader(f"{tipoVehiculo}"  )
    # st.info(f"Distancia recorrida por el taxi: ****")
    # Crea una tarjeta rectangular con los colores de fondo
    st.markdown(
        f"""
        <div style="background-color: {color1}; padding: 10px; border-radius: 10px;">
            <center><h2 style="color: {color4};">Ingreso</h2></center>
            <center><h2 style="color: {color4};">Diario</h2></center>
            <center><p style="color: {color5};">$ {numero * sim['total_amount']['mean']:.2f}</p></center>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.divider()
    
    st.markdown(
        f"""
        <div style="background-color: {color1}; padding: 10px; border-radius: 10px;">
            <center><h2 style="color: {color4};">Utilidades</h2></center>
            <center><h2 style="color: {color4};">💵💰💳</h2></center>
            <center><p style="color: {color5};">$ {numero * sim['Profit']['mean']:.2f}</p></center>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.divider()
    
    st.markdown(
        f"""
        <div style="background-color: {color1}; padding: 10px; border-radius: 10px;">
            <center><h2 style="color: {color4};">Ingreso por viaje</h2></center>
            <center><p style="color: {color5};">$ {numero * sim['amount_mean']['mean']:.2f}</p></center>
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()
st.write("Otras estadisticas de las variables analizadas")
st.dataframe(sim)
st.markdown('**********')
