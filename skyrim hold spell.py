import pyautogui as pag
import time
import keyboard

delay = 2

print("This will spend as long as you want casting a spell to level it up")
ui = input("-: ")
print("Starting in 10 seconds")
time.sleep(10)

while True:
    pag.mouseDown(button='right')
    time.sleep(delay)
    pag.mouseUp(button='right')
    time.sleep(1)
    if keyboard.is_pressed('q'):
        break 
        
print("Done.")
