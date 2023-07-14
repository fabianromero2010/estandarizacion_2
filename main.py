import streamlit as st
import estandarizador
import csv
import pandas as pd
from PIL import Image

separador_campos = ';'
st.title("Aplicación Estandarización de teléfonos nacionales")

nombre_archivo = st.file_uploader("Selecciona un archivo", type=["txt"])

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

    # Mostrar el resultado en una tabla
    st.write("Resultado:")
    st.dataframe(df)

    # Crear botón para descargar archivo csv
    st.download_button('Download CSV', datos, file_name=name + '.csv')

else:
    st.warning("Por favor, selecciona un archivo para cargar.")

# Cargar y mostrar la imagen en la esquina superior derecha con tamaño proporcional
col1, col2 = st.beta_columns([1, 3])
with col1:
    st.empty()
with col2:
    image = Image.open("LogoAIO.jpeg")
    st.image(image, caption='Logo de la aplicación', use_column_width=True)
