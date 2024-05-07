#Los primeros comandos a den ser de lectura, para facilitar una mejor ejecucion de acciones por parte del bot.
#La Pantalla abra que leerla desde la mitad vertical superior para arriba.
# Captura una imagen de la mitad superior de la pantalla
import pyautogui
# Ingreso de los primeros comandos a ejecutar.
try:
    # Buscar la imagen dentro de la región de búsqueda
    posicion_imagen_1_tp = pyautogui.locateCenterOnScreen(('E:\Proyectos de codigos\Python\Testing at python things of an ai\PokeRogue.PNG'), confidence=0.75)

    # Verificar si se encontró la imagen
    if posicion_imagen_1_tp:
        print("Se encontró la imagen en la posición:", posicion_imagen_1_tp)
        print("Moviendose a la ubicacion...")
        pyautogui.moveTo(posicion_imagen_1_tp)
        pyautogui.click()
    else:
        print("No se encontró la imagen")
except pyautogui.ImageNotFoundException:
    print("No se encontró la imagen")
#Comenzando con un mew y un zigzagoon (con Recoger)
def ejecucionElegir():
    # Como ya se encuentra una partida guardada se utiliza la siguente sucesión...
    pyautogui.press('down')
    pyautogui.sleep(3)
    pyautogui.press('z')
    pyautogui.sleep(3)
    pyautogui.press('z')
    pyautogui.sleep(3)
    # Comienza a buscar a mew...
    pyautogui.press('right', presses=7, interval=0.5)
    pyautogui.sleep(3)
    pyautogui.press('down', presses=8, interval=0.5)
    pyautogui.sleep(3)
    pyautogui.press('z', presses=2, interval=0.5)
    pyautogui.sleep(3)
    #Lo encuentra y lo elije, procede a buscar al zigzagoon...
    pyautogui.press('left', presses=7, interval=0.5)
    pyautogui.sleep(3)
    pyautogui.press('up')
    pyautogui.sleep(3)
    pyautogui.press('down', presses=2, interval=0.5)
    pyautogui.sleep(3)
    pyautogui.press('right', presses=5, interval=0.5)
    pyautogui.sleep(3)
    pyautogui.press('z', presses=2, interval=0.5)
    pyautogui.sleep(3)
    #Objetivo logrado parcialmente, se podria mejorar.
ejecucionElegir()
# Definir las coordenadas de la región de búsqueda
x1, y1 = 117, 70  # Coordenadas de la esquina superior izquierda
x2, y2 = 1843, 543  # Coordenadas de la esquina inferior derecha


#Paso 1: leer la pantalla, indentificar si el pokemon que tenemos enfrente es shiny o no, si es shiny priorizar atraparlo, si no paso 2.
def EncuentroconShiny():
    try:
        # Buscar la imagen dentro de la región de búsqueda
        posicion_imagen_1_tp = pyautogui.locateCenterOnScreen('E:\Proyectos de codigos\Python\Testing at python things of an ai\Shiny.PNG', region=(x1, y1, x2 - x1, y2 - y1), confidence=0.75)
        # Verificar si se encontró la imagen
        if posicion_imagen_1_tp:
            print("Se encontraron las estrellas en la siguente ubicación:", posicion_imagen_1_tp)
        else:
            print("No se encontraron las estrellas")
    except pyautogui.ImageNotFoundException:
        print("No se encontraron las estrellas")
#Paso 2: identificar el tipo del pokemon que esta enfrente, revisar los movimientos, pasar por la tabla de tipos.

#Paso 3: Realizar el movimiento supereficaz o movimiento dentro del rango(efectivo), si el rango no es efectivo u superefectivo.

#Paso 4: evaluar la posibilidad de ejecutar la accion de cambiar o capturar al pokemon, pasar por ratio de captura.

#Paso 5: despues de llevar a cabo la accion de cambiar de pokemon, ejecutar paso 3 nuevamente.
