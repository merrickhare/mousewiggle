from optparse import Values
import PySimpleGUI as pg
import pyautogui as pag


def wiggle(intervalNumber):
    pag.move(100,100,intervalNumber)

pg.theme('Tan')
layout = [[pg.Text("Choose Interval"),pg.Radio("1 Second","Group1",key="radio1"),pg.Radio("3 Second","Group1",key="radio3"),pg.Radio("5 Second","Group1",key="radio5")],[pg.Button("Start",key="start_button"),pg.Button("Stop",key="stop_button")]]

window = pg.Window("Mouse Wiggler", layout=layout,icon="pointer.png", size=(375,75))

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

    

    

   
    



  
   




