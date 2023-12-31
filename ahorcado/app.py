import os
import imprime


def limpiar_consola():
    '''
    Limpiar la consola.
    '''
    os.system('cls' if os.name == 'nt' else 'clear')


def juego_ahorcado(palabra, nivel=1):
    """
    Programando el juego del ahorcado.
    """
    limpiar_consola()
    print('Adivina la palabra:')
    tamano_palabra = [' _ ' for _ in palabra]
    print(''.join(tamano_palabra))
    print()
    errores = 0
    ingresados = set()

    while True:
        letra = str(input('Ingresa una letra: ')).lower()

        if letra == 'salir':
            print('Así que has elegido el camino de la rendición.')
            break

        if letra in ingresados and nivel == 1:
            print('Ya has usado esa letra.')
            continue

        if letra in palabra and letra not in ingresados:
            for i, _ in enumerate(palabra):
                if palabra[i] == letra:
                    tamano_palabra[i] = letra.upper()
        else:
            errores += 1

        ingresados.add(letra)
        palabla_actual = ''.join(tamano_palabra)
        print(palabla_actual)
        print(imprime.grafico[errores])
        print()

        if errores == 8:
            print('JAJA, Perdiste...!')
            break

        if palabra == palabla_actual.lower():
            print('Felicidades, has adivinado la palabra !!!')
            break


PALABRA = str(input('Ingresa la palabra secreta: ')).lower()
juego_ahorcado(PALABRA, 2)
