import PySimpleGUI as pg
import pyautogui as pag



layout = [[pg.Text("Choose Interval")],[pg.Radio("1 Second","Group1")],[pg.Radio("3 Second","Group1")],[pg.Radio("5 Second","Group1")],[[pg.Button("Start",key="start_button")],[pg.Button("Stop",key="stop_button")]]]

pg.Window("Mouse Wiggle",layout=layout,resizable=True,size=(300,175)).read()



