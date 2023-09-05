import os
import filecmp
from tipos import tipos_de_archivo


def revisar_carpeta(carpeta):
    """
    Enlista los archivos de una carpeta y los clasifica por tipo.
    """
    archivos_por_extension = {'desconocido': 0}
    for archivo in os.listdir(carpeta):
        extension = os.path.splitext(archivo)[1]
        desconocidos = [j for i in tipos_de_archivo.values() for j in i]
        for item, valores in tipos_de_archivo.items():

            if item not in archivos_por_extension:
                archivos_por_extension[item] = 0

            if extension in valores:
                archivos_por_extension[item] += 1

        if extension not in desconocidos:
            archivos_por_extension['desconocido'] += 1

    return archivos_por_extension


def buscar_duplicados(carpeta):
    """
    Busca archivos duplicados en una carpeta.
    """
    archivos_por_extension = {}
    for archivo in os.listdir(carpeta):
        extension = os.path.splitext(archivo)[1]
        if extension not in archivos_por_extension:
            archivos_por_extension[extension] = []
        archivos_por_extension[extension].append(os.path.join(carpeta, archivo))

    for extension, archivos in archivos_por_extension.items():
        if len(archivos) == 1:
            continue

        eliminar = []
        for i, _ in enumerate(archivos):
            for j in range(i+1, len(archivos)):
                if filecmp.cmp(archivos[i], archivos[j]):
                    eliminar.append(archivos[j])

    print(archivos_por_extension)
    return set(eliminar)


def eliminar_duplicados(eliminar):
    """
    Elimina los archivos duplicados.
    """
    for archivo in set(eliminar):
        os.remove(archivo)
        print(f"Eliminado archivo duplicado: {archivo}")



CARPETA = r"./data/duplicado/"
# print(revisar_carpeta(CARPETA))
print(buscar_duplicados(CARPETA))
# print(eliminar_duplicados(buscar_duplicados(CARPETA)))
