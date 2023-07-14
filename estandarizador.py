import re
import diccionarios
import patrones

def limpiar_cadena(cadena):
    digitos = re.sub(r'\D', '', cadena)
    return digitos

def eliminar_ceros_izquierda(cadena:str):
    return cadena.lstrip("0")

def concatenar_componentes_telefono(indicativo_pais :str,indicativo_area:str,telefono:str) -> str:
    return indicativo_pais + ' ' + indicativo_area + ' ' + telefono

def concatenar_componentes_celular(indicativo_pais :str,celular:str) -> str:
    return indicativo_pais + ' ' + celular


def limpiar_entrada(cadena):

    lista_componentes = cadena.split()
    entrada_limpia = ''

    if len(lista_componentes) == 3:
        indicativo_pais = lista_componentes[0]
        indicativo_pais = limpiar_cadena(indicativo_pais)
        indicativo_pais = eliminar_ceros_izquierda(indicativo_pais)

        indicativo_area = lista_componentes[1]
        indicativo_area = limpiar_cadena(indicativo_area)

        numero = lista_componentes[2]
        numero = limpiar_cadena(numero)
        numero = eliminar_ceros_izquierda(numero)

        entrada_limpia = indicativo_pais + indicativo_area + numero

        return entrada_limpia

    if len(lista_componentes) == 2:
        indicativo_pais = lista_componentes[0]
        indicativo_pais = limpiar_cadena(indicativo_pais)
        indicativo_pais = eliminar_ceros_izquierda(indicativo_pais)

        numero = lista_componentes[1]
        numero = limpiar_cadena(numero)
        numero = eliminar_ceros_izquierda(numero)

        entrada_limpia = indicativo_pais + numero
        return entrada_limpia

    if len(lista_componentes) == 1:
        entrada_limpia = lista_componentes[0]
        entrada_limpia = limpiar_cadena(entrada_limpia)
        entrada_limpia = eliminar_ceros_izquierda(entrada_limpia)
        return entrada_limpia
    if len(lista_componentes) > 3:
        entrada_limpia = ''
        for componente in lista_componentes:
            componente = limpiar_cadena(componente)
            componente = eliminar_ceros_izquierda(componente)
            entrada_limpia = entrada_limpia + componente
        return entrada_limpia
    return entrada_limpia




def estandarizar(cadena_estandarizar:str):
    arreglo_estandarizacion = [None, '', '',cadena_estandarizar]
    entrada_limpia = limpiar_entrada(cadena_estandarizar)
    componentes_telefono = patrones.extraer_componentes_telefono(entrada_limpia)

    if componentes_telefono is not None:
        arreglo_estandarizacion[0] = 'Telefono'
        arreglo_estandarizacion[1] = componentes_telefono[0]
        arreglo_estandarizacion[2] = componentes_telefono[1]
        arreglo_estandarizacion[3] = componentes_telefono[2]
        return arreglo_estandarizacion

    componentes_celular = patrones.extraer_componentes_celular(entrada_limpia)

    if componentes_celular is not None:
        arreglo_estandarizacion[0] = 'Celular'
        arreglo_estandarizacion[1] = componentes_celular[0]
        arreglo_estandarizacion[3] = componentes_celular[1]
        return arreglo_estandarizacion

    return arreglo_estandarizacion
