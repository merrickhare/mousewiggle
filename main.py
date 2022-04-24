import PySimpleGUI as pg
import pyautogui as pag



layout = [[pg.Text("Choose Interval"),pg.Radio("1 Second","Group1",key="radio1"),pg.Radio("3 Second","Group1",key="radio3"),pg.Radio("5 Second","Group1",key="radio5")],[pg.Button("Start",key="start_button"),pg.Button("Stop",key="stop_button")]]

window = pg.Window("Mouse Wiggler", layout=layout, size=(375,75))

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == pg.WIN_CLOSED or event == 'stop_button':
        break
   




