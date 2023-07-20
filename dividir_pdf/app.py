import math
from PyPDF2 import PdfWriter, PdfReader


def dividir_pdf(archivo, pag_por_parte):
    """
    Divide un archivo PDF en partes de pag_por_parte páginas.
    """
    with open(archivo, "rb") as file:
        inputpdf = PdfReader(file)
        cant_paginas = len(inputpdf.pages)

        for i in range(0, cant_paginas, pag_por_parte):
            output = PdfWriter()

            for j in range(i, min(i + pag_por_parte, cant_paginas)):
                output.add_page(inputpdf.pages[j])

            with open(f"./data/parte{i // pag_por_parte + 1}.pdf", "wb") as salida:
                output.write(salida)

        return f'{math.ceil(cant_paginas/pag_por_parte)} archivos creados.'


NUM_PAG_PARTE = 20
ARCHIVO = "./data/essential.pdf"

divididos = dividir_pdf(ARCHIVO, NUM_PAG_PARTE)
print(divididos)
