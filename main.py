import streamlit as st
import estandarizador
import csv
import pandas as pd

# Establecer el color de fondo para cada columna
st.markdown(
    """
    <style>
    .stColumnLeft {
        background-color: #8B0000;
        padding: 20px;
        color: white;
    }
    .stColumnRight {
        background-color: #800000;
        padding: 20px;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Dividir la página en dos columnas
column_left, column_right = st.beta_columns(2)

# Columna de la izquierda (column_left)
with column_left:
    st.image("LogoAIO.jpeg", caption='Logo de la aplicación', use_column_width=True)
    st.markdown("<h1 style='text-align: center;'>Cargar Archivo</h1>", unsafe_allow_html=True)
    nombre_archivo = st.file_uploader("Selecciona un archivo", type=["txt"])

# Columna de la derecha (column_right)
with column_right:
    st.title("Aplicación Estandarización de teléfonos nacionales")

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
