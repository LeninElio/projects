import datetime
import pandas as pd
from faker import Faker


falso = Faker()


def datos_falsos(cantidad=10):
    """
    Genera datos falsos y los guarda en un archivo csv.
    """
    datos = (
        (
            falso.name(), falso.last_name(),
            falso.email(), falso.phone_number()
        )
        for _ in range(cantidad)
    )

    fecha = datetime.datetime.now().strftime("%d%m%Y_%H%M%S")
    columnas = ['nombre', 'apellido', 'email', 'telefono']

    fakeframe = pd.DataFrame(datos, columns=columnas)
    fakeframe.to_csv(f'./data/{fecha}.csv', index=False)

    return f'Archivo {fecha} creado con {cantidad} datos.'


if __name__ == '__main__':
    generar = datos_falsos(30)
    print(generar)
