import os
import shutil


carpeta = r"./data/duplicado/"

tipos = {
    '.docx': 'Word',
    '.xlsx': 'Excel',
    '.pptx': 'PowerPoint',
    '.pdf': 'PDF',
    '.txt': 'Texto'
}

for extension in tipos.values():
    if not os.path.exists(carpeta + extension):
        os.mkdir(carpeta + extension)

for archivo in os.listdir(carpeta):
    extension = os.path.splitext(archivo)[1]
    if extension in tipos:
        print(f"El archivo {archivo} fue movido a: {tipos[extension]}")
        shutil.move(f'{carpeta}{archivo}', f'{carpeta}{tipos[extension]}/{archivo}')
