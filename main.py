import streamlit as st
import estandarizador
import csv
import pandas as pd

# Establecer el color de fondo para la parte derecha
st.markdown(
    """
    <style>
    .main {
        background-color: #A0522D;
        padding: 20px;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Barra lateral (sidebar)
st.sidebar.image("LogoAIO.jpeg", caption='ALL IN ONE', use_column_width=True)
st.sidebar.markdown("<h1 style='text-align: center; color: white;'>Aqui cargue el Archivo</h1>", unsafe_allow_html=True)
nombre_archivo = st.sidebar.file_uploader("Selecciona un archivo", type=["txt"])

# Dividir la parte derecha en columnas
col1, col2 = st.columns(2)

# Contenedor principal
col1.markdown("<div class='main'>", unsafe_allow_html=True)

# Mostrar el título en la parte principal
col1.markdown("<h1 style='color: white;'>Aplicación Estandarización de teléfonos nacionales</h1>", unsafe_allow_html=True)

Dataframe1 = {
    "cadenas": [],
    "tipo": [],
    "indicativos_pais": [],
    "indicativos_area": [],
    "telefonos": []
}

if nombre_archivo is not None:
    contenido = nombre_archivo.read().decode("utf-8")  # Leer el contenido del archivo
    name = nombre_archivo.name.split('.')[0]

    datos = "CADENA;TIPO;INDICATIVO_PAIS;INDICATIVO_AREA;TELEFONO" + '\r\n'
    lector_csv = csv.reader(contenido.splitlines())

    for fila in lector_csv:
        linea = fila[0]  # Obtener el primer elemento de la fila como la línea a procesar
        resultado = estandarizador.estandarizar(linea)  # Obtener el resultado como una lista
        Dataframe1["cadenas"].append(linea)
        Dataframe1["tipo"].append(resultado[0])
        Dataframe1["indicativos_pais"].append(resultado[1])
        Dataframe1["indicativos_area"].append(resultado[2])
        Dataframe1["telefonos"].append(resultado[3])

        resultado_str = linea + ";" + ";".join(str(item) for item in resultado)  # Convertir cada elemento en una cadena de texto
        datos += resultado_str + '\r\n'

    # Crear un DataFrame con los resultados
    df = pd.DataFrame(Dataframe1)

    # Mostrar el resultado en una tabla en la columna derecha
    col2.title("Resultado:")
    col2.dataframe(df)

    # Crear botón para descargar archivo csv en la columna derecha
    col2.download_button('Download CSV', datos, file_name=name + '.csv')

else:
    st.warning("Por favor, selecciona un archivo para cargar.")

# Cerrar el contenedor principal
col1.markdown("</div>", unsafe_allow_html=True)
