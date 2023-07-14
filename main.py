import streamlit as st
import estandarizador
import csv
import pandas as pd

separador_campos = ';'
st.title("Aplicación Estandarización de telefonos nacionales")

nombre_archivo = st.file_uploader("Selecciona un archivo", type=["txt"])

Dataframe1 = {"cadenas": [],
    "tipo":[],
    "indicativos_pais": [],
    "indicativos_area": [],
    "telefonos":[]
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

    #Crear botón para descargar archivo csv
    st.download_button('Download CSV', datos,file_name=name + '.csv')

else:
    st.warning("Por favor, selecciona un archivo para cargar.")




#for n in columna:




#telefonos_prueba = ['+57 1 8142072','+057 074 8974921','57 03 3105632465','(+57)5 5395527',
#                   '(057) 601 6381800','(57) 3203022796','057 095 5395527','+57 03 3132709532',
#                   '956663772','+5733108303929','057 1 20682834','0000057 1 000006898987','3006809521','3545560674','12068283','6012068283','6013006809521','3122803876','0576013008957','000057 ','601 3101453079','5760120682873']


#    for fila in lector_csv:
#       columna = fila[0]
#        # Haz algo con el valor de la columna
#        print(columna)

# Opción 2: Abriendo y leyendo el archivo directamente
#nombre_archivo = "telefonos.txt"  # Reemplaza con el nombre de tu archivo

#with open(nombre_archivo, "r") as archivo:
#   for linea in archivo:
#       columna = linea.strip()
#       # Haz algo con el valor de la columna
#        print(columna)



#for n in telefonos_prueba:
#   print(n + '---->',estandarizador.estandarizar(n))
