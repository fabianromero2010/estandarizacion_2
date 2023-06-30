import re

indicativos_paises = {"COLOMBIA": "57"}
prefijos_celulares_colombia = {
"1":"300",
"2":"301",
"3":"302",
"4":"303",
"5":"304",
"6":"305",
"7":"306",
"8":"307",
"9":"308",
"10":"310",
"11":"311",
"12":"312",
"13":"313",
"14":"314",
"15":"315",
"16":"316",
"17":"317",
"18":"318",
"19":"319",
"20":"320",
"21":"321",
"22":"322",
"23":"323",
"24":"324",
"25":"325",
"26":"350"
    }

prefijos_fijo_celular = {"1":"03"}

codigos_area_colombia = {
        "Amazonas": "8",
        "Antioquia": "4",
        "Arauca": "7",
        "Atlántico": "5",
        "Bogotá D.C.": "1",
        "Bolívar": "5",
        "Boyacá": "8",
        "Caldas": "6",
        "Caquetá": "8",
        "Casanare": "8",
        "Cauca": "2",
        "Cesar": "5",
        "Chocó": "4",
        "Córdoba": "4",
        "Cundinamarca": "1",
        "Guainía": "8",
        "Guaviare": "8",
        "Huila": "8",
        "La Guajira": "5",
        "Magdalena": "5",
        "Meta": "8",
        "Nariño": "2",
        "Norte de Santander": "7",
        "Putumayo": "8",
        "Quindío": "6",
        "Risaralda": "6",
        "San Andrés y Providencia": "8",
        "Santander": "7",
        "Sucre": "5",
        "Tolima": "8",
        "Valle del Cauca": "2",
        "Vaupés": "8",
        "Vichada": "8"
    }

prefijos_indicativos_area = {"1":"60"}

indicativos_internacionales = {"1":"05","2":"005","3":"07","4":"007","5":"09","6":"009"}

def get_indicativos_paises():
        return indicativos_paises


def get_prefijos_fijo_celular():
        return prefijos_fijo_celular

def get_codigos_area_colombia():
        return codigos_area_colombia

def get_prefijos_indicativos_area():
        return prefijos_indicativos_area

def get_prefijos_celulares_colombia():
        return prefijos_celulares_colombia

def get_indicativos_internacionales():
        return indicativos_internacionales



