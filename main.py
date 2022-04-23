import pyautogui as PAG
import PySimpleGUI as pg


layout = [[pg.Text("Mouse Wiggle App")],[pg.Checkbox("Start",default=False,key="CheckOne")],[pg.Text("Interval")],[pg.Button("Close")]]

pg.Window("Mouse Wiggle",layout=layout,resizable=True).read()



