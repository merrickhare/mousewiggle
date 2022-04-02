import pyautogui as PAG
from tkinter import *
import threading



def wiggleMouse():
  threading.Timer(5.0, wiggleMouse).start()
  PAG.move(30,40)

wiggleMouse( )



