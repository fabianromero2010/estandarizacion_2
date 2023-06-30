import estandarizador
import csv

nombre_archivo = r"https://github.com/Alejandra-byte-pixel/estandarizacion/blob/main/telefonos.csv"

with open(nombre_archivo, "r") as archivo:
    datos = ""

    lector_csv = csv.reader(archivo)
    for fila in lector_csv:
        linea = fila[0]  # Obtener el primer elemento de la fila como la línea a procesar
        resultado = estandarizador.estandarizar(linea)  # Obtener el resultado como una lista
        resultado_str = " ".join(resultado)  # Convertir la lista en una cadena de texto separada por espacios
        datos += linea + '---->' + resultado_str + '\n'

ruta_archivo = r"https://github.com/Alejandra-byte-pixel/estandarizacion/blob/main/estandarizadotelefonos.txt"
with open(ruta_archivo, "w") as archivo_salida:
    archivo_salida.write(datos)

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
