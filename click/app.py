import time
import pyautogui


def hacer_clic_en_posicion(posicion_x, posicion_y, num_clics):
    """
    Función que hace clic en una posición específica de la pantalla
    """
    print('Iniciando...')
    time.sleep(5)

    for _ in range(num_clics):
        pyautogui.moveTo(posicion_x, posicion_y, duration=0.2)
        pyautogui.click()
        time.sleep(1)

    print('Hecho...!')


hacer_clic_en_posicion(777, 595, 1010)
