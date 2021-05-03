import PySimpleGUI as sg
import os.path
import csv
import analisis1
from functions import *


def start():
    """
    Lanza la ejecución de la ventana del menú inicial
    """
    window = loop()
    window.close()


def loop():
    """
    Loop de la ventana de menú que capta los eventos al apretar las opciones
    """

    #Construye y configura la ventana con su respectivo layout, y la guarda en la variable window
    window = sg.Window('DataAnalysis').Layout([
                [sg.Text('Que datos analizamos?', size=(30,1), font=("Sawasdee", 25), justification= 'center')],
                [sg.Button('Dataset1',key='-data1-')],
                [sg.Button('Marcas de auto mas compradas',key='-data2-')],
                [sg.Button('SALIR',key='-exit-')],
                [sg.Image(key='-IMAGE-')],
                [sg.Text('Resize to'), sg.In(key='-W-', size=(5,1)), sg.In(key='-H-', size=(5,1))]  
                ])


    path = 'C:/Users/EXO/Desktop/Facu/FACULTAD/Seminario de Lenguajes - Python/trabajo individual/Datasets/DatasetAutos-Logos/Logos'

    while True:
        event, values = window.read()

        #Si el usuario clickea en salir
        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-","salir","Salir"):
            break

        #Si el usuario clickea el dataset 1
        if event == '-data1-':

            window.hide()
            analisis1.start()
            window.un_hide()

        #Si el usuario clickea el dataset 2
        if event == "-data2-":

            #PENDIENTE: CREAR VENTANA DE ANALISIS DEL DATASET 2
            window.hide()
            analisis1.start()
            window.un_hide()

    return window

