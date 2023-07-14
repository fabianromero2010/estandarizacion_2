import streamlit as st
import estandarizador
import csv
import pandas as pd
from PIL import Image

# Establecer el color de fondo para la parte derecha
st.markdown(
    """
    <style>
    .main {
        background-color: #8B0000;
        padding: 20px;
        color: white;
    }
    .image-container {
        display: flex;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Barra lateral (sidebar)
st.sidebar.image("LogoAIO.jpeg", caption='ALL IN ONE',  width=100)
st.sidebar.markdown("<h1 style='text-align: center; color: white;'>Aqui cargue el Archivo</h1>", unsafe_allow_html=True)
nombre_archivo = st.sidebar.file_uploader("Selecciona un archivo", type=["txt"])

# Contenedor principal
st.markdown("<div class='main'>", unsafe_allow_html=True)

# Mostrar el título y la imagen en la parte principal
st.markdown("<h1 style='color: white;'>Aplicación para la Estandarización de teléfonos nacionales</h1>", unsafe_allow_html=True)

# Alinear la imagen a la derecha en la parte principal
image = Image.open("LogoSETI.jpeg")
st.markdown("<div class='image-container'>", unsafe_allow_html=True)
st.image(image, caption='SETI', width=50)
st.markdown("</div>", unsafe_allow_html=True)

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

        if len(resultado) >= 4:
            Dataframe1["indicativos_area"].append(resultado[2])
            Dataframe1["telefonos"].append(resultado[3])
        else:
            Dataframe1["indicativos_area"].append(None)
            Dataframe1["telefonos"].append(None)

        resultado_str = linea + ";" + ";".join(str(item) for item in resultado)  # Convertir cada elemento en una cadena de texto
        datos += resultado_str + '\r\n'

    # Crear un DataFrame con los resultados
    df = pd.DataFrame(Dataframe1)

    # Mostrar el resultado en una tabla en la parte principal
    st.title("Resultado:")
    st.dataframe(df)

    # Crear botón para descargar archivo csv en la parte principal
    st.download_button('Download CSV', datos, file_name=name + '.csv')

else:
    st.warning("Por favor, selecciona un archivo para cargar.")

# Cerrar el contenedor principal
st.markdown("</div>", unsafe_allow_html=True)
