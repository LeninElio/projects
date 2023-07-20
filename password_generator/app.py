import string
import random


def generador(tamano=15):
    """
    Generador de contraseña, por defecto el tamaño es 15.
    """
    try:
        tamano = int(tamano)
        if tamano >= 15:
            caracteres = string.ascii_letters + string.digits + string.punctuation
            password = (random.choice(caracteres) for _ in range(tamano))
            return f"Password: {''.join(password)}"
        return 'El tamaño de la contraseña debe mayor a 15.'
    except ValueError:
        return 'El tamaño de la contraseña debe ser un número.'


if __name__ == '__main__':
    PASSWORD = generador(23)
    print(PASSWORD)
