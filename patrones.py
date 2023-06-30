import re
from itertools import product
import diccionarios

indicativos_paises = diccionarios.get_indicativos_paises()
codigos_area_colombia = diccionarios.get_codigos_area_colombia()
prefijos_indicativos_area = diccionarios.get_prefijos_indicativos_area()
indicativos_internacionales = diccionarios.get_indicativos_internacionales()
prefijos_celulares_colombia = diccionarios.get_prefijos_celulares_colombia()
prefijos_fijo_celular = diccionarios.get_prefijos_fijo_celular()

def verificar_patron(cadena, patron):
    busqueda = re.search(patron, cadena)
    if busqueda:
        return busqueda.groups()
    else:
        return None


def extraer_componentes_telefono(cadena):
    arreglo_componentes_telefono = [None, None, None]
    for indicativo_pais, codigo_area_colombia in product(indicativos_paises.values(), codigos_area_colombia.values()):
        patron1 = r'^({})({})(\d{{7}}$)'.format(re.escape(indicativo_pais), re.escape(codigo_area_colombia))
        componentes1 = verificar_patron(cadena, patron1)
        if componentes1 is not None:
            arreglo_componentes_telefono[0] = componentes1[0]
            arreglo_componentes_telefono[1] = componentes1[1]
            arreglo_componentes_telefono[2] = componentes1[2]
            return arreglo_componentes_telefono

    for indicativo_pais, indicativo_internacional, codigo_area_colombia in product(indicativos_paises.values(),
                                                                                   indicativos_internacionales.values(),
                                                                                   codigos_area_colombia.values()):
        patron2 = r'^({}){}({})(\d{{7}}$)'.format(re.escape(indicativo_pais), re.escape(indicativo_internacional),
                                                 re.escape(codigo_area_colombia))
        componentes2 = verificar_patron(cadena, patron2)
        if componentes2 is not None:
            arreglo_componentes_telefono[0] = componentes2[0]
            arreglo_componentes_telefono[1] = componentes2[1]
            arreglo_componentes_telefono[2] = componentes2[2]
            return arreglo_componentes_telefono

    for indicativo_pais, prefijo_indicativo_area, codigo_area_colombia in product(indicativos_paises.values(),
                                                                                  prefijos_indicativos_area.values(),
                                                                                  codigos_area_colombia.values()):
        patron3 = r'^({}){}({})(\d{{7}}$)'.format(re.escape(indicativo_pais), re.escape(prefijo_indicativo_area),
                                                 re.escape(codigo_area_colombia))
        componentes3 = verificar_patron(cadena, patron3)
        if componentes3 is not None:
            arreglo_componentes_telefono[0] = componentes3[0]
            arreglo_componentes_telefono[1] = componentes3[1]
            arreglo_componentes_telefono[2] = componentes3[2]
            return arreglo_componentes_telefono

        for codigo_area_colombia in codigos_area_colombia.values():
            patron4 = r'^({})(\d{{7}}$)'.format(re.escape(codigo_area_colombia))
            componentes4 = verificar_patron(cadena, patron4)
            if componentes4 is not None:
                arreglo_componentes_telefono[0] = '57'
                arreglo_componentes_telefono[1] = componentes4[0]
                arreglo_componentes_telefono[2] = componentes4[1]

                return arreglo_componentes_telefono

        for prefijo_indicativo_area, codigo_area_colombia in product(prefijos_indicativos_area.values(),
                                                                     codigos_area_colombia.values()):
            patron5 = r'^{}({})(\d{{7}}$)'.format(re.escape(prefijo_indicativo_area), re.escape(codigo_area_colombia))
            componentes5 = verificar_patron(cadena, patron5)
            if componentes5 is not None:
                arreglo_componentes_telefono[0] = '57'
                arreglo_componentes_telefono[1] = componentes5[0]
                arreglo_componentes_telefono[2] = componentes5[1]
                return arreglo_componentes_telefono

    return None



def extraer_componentes_celular(cadena):
    arreglo_componentes_celular = [None, None]
    for indicativo_pais, prefijo_celular_colombia in product(indicativos_paises.values(), prefijos_celulares_colombia.values()):
        patron1 = r'^({})({}\d{{7}}$)'.format(re.escape(indicativo_pais), re.escape(prefijo_celular_colombia))
        componentes1 = verificar_patron(cadena, patron1)
        if componentes1 is not None:
            arreglo_componentes_celular[0] = componentes1[0]
            arreglo_componentes_celular[1] = componentes1[1]
            return arreglo_componentes_celular

    for indicativo_pais, prefijo_fijo_celular, prefijo_celular_colombia in product(indicativos_paises.values(),
                                                                                   prefijos_fijo_celular.values(),
                                                                                   prefijos_celulares_colombia.values()):
        patron2 = r'^({}){}({}\d{{7}}$)'.format(re.escape(indicativo_pais), re.escape(prefijo_fijo_celular),
                                                 re.escape(prefijo_celular_colombia))
        componentes2 = verificar_patron(cadena, patron2)
        if componentes2 is not None:
            arreglo_componentes_celular[0] = componentes2[0]
            arreglo_componentes_celular[1] = componentes2[1]
            return arreglo_componentes_celular

    for prefijo_celular_colombia in prefijos_celulares_colombia.values():
        patron3 = r'^({}\d{{7}}$)'.format(re.escape(prefijo_celular_colombia))
        componentes3 = verificar_patron(cadena, patron3)
        if componentes3 is not None:
            arreglo_componentes_celular[0] = '57'
            arreglo_componentes_celular[1] = componentes3[0]
            return arreglo_componentes_celular

    for indicativo_pais, prefijo_indicativo_area, codigo_area_colombia in product(indicativos_paises.values(),
                                                                                  prefijos_indicativos_area.values(),
                                                                                  codigos_area_colombia.values()):
        patron3 = r'^({}){}({})(\d{{7}}$)'.format(re.escape(indicativo_pais), re.escape(prefijo_indicativo_area),
                                                 re.escape(codigo_area_colombia))
        componentes3 = verificar_patron(cadena, patron3)
        if componentes3 is not None:
            arreglo_componentes_telefono[0] = componentes3[0]
            arreglo_componentes_telefono[1] = componentes3[1]
            arreglo_componentes_telefono[2] = componentes3[2]
            return arreglo_componentes_telefono



    return None





