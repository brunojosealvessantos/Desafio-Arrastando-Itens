# Desafio Arrastando Itens
import pyautogui


class Bot:
    def __init__(self):
        pass

    def moverArquivos(self):
        for s in range(8):
            pyautogui.moveTo(216, 222, duration=1.5)
            pyautogui.dragTo(225, 620, button='left', duration=1)


bot = Bot()
bot.moverArquivos()
