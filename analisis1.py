import PySimpleGUI as sg
import csv
from functions import *
from analizarDataset1 import *
from test import *

def start():
    """
    Lanza la ejecución de la ventana del menú inicial
    """
    window = loop()
    window.close()



#VENTANA DE ANALISIS DE DATOS DEL DATASET DE VIDEOJUEGOS
def loop():
    """
    Loop de la ventana de menú que capta los eventos al apretar las opciones
    """

    #Construye y configura la ventana con su respectivo layout, y la guarda en la variable window
    window = sg.Window('Analizar el DATASET UNO').Layout([
                [sg.Text('Elija algún criterio', size=(30,1), font=("Sawasdee", 25), justification= 'center',key='-text-')],
                [sg.Button('Los veinte videojuegos mas vendidos',key='-criterio1-')],
                [sg.Button('Los videojuegos menos vendidos',key='-criterio2-')],
                [sg.Button('SALIR',key='-exit-')],
                [sg.Image(key='-IMAGE-')],  
                ])

    #Path del dataset de videojuegos
    path = 'C:/Users/EXO/Desktop/Facu/FACULTAD/Seminario de Lenguajes - Python/trabajo individual/Datasets/DatasetVideojuegos.csv'

    while True:
        event, values = window.read()

        #Si el usuario clickea en salir
        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-","salir","Salir"):
            break

        #Si el usuario clickea el dataset 1
        if event == '-criterio1-':
            listaProcesada = analizar_dataset1(0,path)
            print(listaProcesada)

        #Si el usuario clickea el dataset 2
        if event == "-criterio2-":
            listaProcesada = analizar_dataset1(1,path)
            print(listaProcesada)


    return window

