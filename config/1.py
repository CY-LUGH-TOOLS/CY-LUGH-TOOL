import time
import threading
import pyautogui
import os
import keyboard
def x():
    while True:
        pyautogui.press('1')
        pyautogui.press('enter')
        time.sleep(1)

def y(): ## Tranca ao aperta q
    while True:
        if keyboard.is_pressed('q'):
            os._exit(0)
threading.Thread(target=y).start() ## Roda duas funções ao mesmo tempo      

pyautogui.hotkey('winleft', '1') ## Acessa o bloco de notas
threading.Thread(target=x).start() ## Roda duas funções ao mesmo tempo