from optparse import Values
import PySimpleGUI as pg
import pyautogui as pag
from time import sleep


def wiggle(intervalNumber,numberOfLoops):
    sleep(2)
    for loops in numberOfLoops:
        pag.move(100,100)
        sleep(intervalNumber)
        pag.move(-100,-100)

pg.theme('Tan')
layout = [[pg.Text("Interval between wiggle"),pg.Radio("1 Second","Group1",key="radio1"),pg.Radio("3 Second","Group1",key="radio3"),pg.Radio("5 Second","Group1",key="radio5")],[pg.Text("Run for?"),pg.Radio("5 Minutes", "Group2",key="radio6"),pg.Radio("10 Minutes", "Group2",key="raido7"),pg.Radio("unlimited","Group2",key="radio8")],[pg.Button("Start",key="start_button"),pg.Button("Stop",key="stop_button")]]

window = pg.Window("Mouse Wiggler", layout=layout,icon="pointer.png", size=(400,90))

while True:  # Event Loop
    event, values = window.read()
    print(event, values)

    if event == pg.WIN_CLOSED or event == 'stop_button':
        break
    elif event == 'start_button' and values["radio1"] == True:
        wiggle(1.0)
    elif event == 'start_button' and values["radio3"] == True:
        wiggle(3.0)
    elif event == 'start_button' and values["radio5"] == True:
        wiggle(5.0)

    

    

   
    



  
   




