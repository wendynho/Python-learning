import pyautogui
import time


#Automatizando um processo simples de envio de email para uma empresa fantasma. utilizando o PYAUTOGUI
#Automating a basic email sending process to a ghost company. Using PYAUTOGUI library

print(pyautogui.position())
pyautogui.hotkey ("win")
pyautogui.write ("Edge")    
pyautogui.press ("enter")
pyautogui.write ("https://www.google.com.br/")
pyautogui.press ("enter")

time.sleep(5)
pyautogui.click(x=1169, y=99)
time.sleep(2)

pyautogui.PAUSE = 2

pyautogui.click(x=118, y=163)
pyautogui.write ("wendelbmf22@gmail.com")
pyautogui.press ("enter")
pyautogui.press ("tab") 
pyautogui.typewrite ("Planilha atualizada")

pyautogui.PAUSE = 2

pyautogui.click(x=830, y=724)
