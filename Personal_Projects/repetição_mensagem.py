from time import sleep
import pyautogui

qtd = int(input('Digite a quantidade que deseja repetir: '))
msg = str(input('O que gostaria de repetir: '))

if '@' in msg:
    cnt = str(input('O que gostaria juntar a msg: '))

rep = 0
sleep(1.5)
while rep < qtd:
    pyautogui.write(msg)
    pyautogui.press('enter')
    if '@' in msg:
        
        pyautogui.write(cnt)
        pyautogui.press('enter')
    rep += 1
    
pyautogui.alert('Fim da repetição', 'Fim da repetição', 'sair')
