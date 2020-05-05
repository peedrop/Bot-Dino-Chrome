import time
import pyautogui
from PIL import ImageGrab

X = 460.0  # x2 = +100)
Y = 570    # y2 = +80)

def capturarTela():
    tela = ImageGrab.grab() 
    return tela

def detectarCor(tela):
    auxCor = tela.getpixel((int(X), Y))
    for m in range(int(X), int(X+100)):
        for n in range (Y, Y+80):
            cor = tela.getpixel((m, n))
            if cor != auxCor:
                return True
            else:
                auxCor = cor

def pular():
    global X
    pyautogui.press("up") 
    X += 0.4

print("Iniciando em 3 segundos...")
time.sleep(3)

while True:
    tela = capturarTela()
    if detectarCor(tela):
        pular() 



