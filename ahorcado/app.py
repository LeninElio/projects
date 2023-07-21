import os
import imprime


def limpiar_consola():
    '''
    Limpiar la consola.
    '''
    os.system('cls' if os.name == 'nt' else 'clear')


def juego_ahorcado(palabra):
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
        letra = str(input('Ingresa una letra: '))

        if letra.lower() == 'aa':
            print('Asi que has elegido el camino de la rendición.')
            break

        if letra.lower() in ingresados:
            print('Ya has usado esa letra.')
            continue

        ingresados.add(letra.lower())
        if letra.lower() in palabra:
            for i, _ in enumerate(palabra):
                if palabra[i] == letra.lower():
                    tamano_palabra[i] = letra.upper()
        else:
            errores += 1

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


PALABRA = str(input('Ingresa la palabra secreta: '))
juego_ahorcado(PALABRA)
