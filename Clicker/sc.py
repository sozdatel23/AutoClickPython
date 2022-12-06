# cd C://PythonDoc/sc
from tkinter import *
import pyautogui
import os

def click_button():
	tkbutton.config(background="#555", foreground="white")
	
window = Tk()
window.title("Кликер НМО")
window.geometry("800x500")

tkbutton = Button(text = "Старт", command = click_button)
tkbutton.place(height=30, width=70, x = 700, y = 20, anchor = "c")

window.mainloop()

files = os.listdir("buttons")
count = 0 #счет нажатий, для контроля
while True:
	for f in files:
		picture = "buttons/" + f
		activ_control = False
		button = pyautogui.locateOnScreen(picture, confidence = 0.85)

		if button:
			pyautogui.sleep(2)
			pyautogui.click(button, duration=0.2) #duration возможно надо убрать
			if picture == "buttons/but1.png" or picture == "buttons/but3.png":
				print("Кнопка Подтверждения активирована")
			else:
				activ_control = True
				count += 1
				print("Кнопка Закрытия активирована")
				print("!!!Пройден " + str(count) + " контроль!!!\n")
			pyautogui.sleep(2)

# Функция нажатия
def click():
    pyautogui.mouseDown()
    time.sleep(0.01)
    pyautogui.mouseUp()

