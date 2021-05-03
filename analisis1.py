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

            #Genera la lista de datos del csv con la funcion analizar dataset1
            lista = analizar_dataset1(path)
            #Ordena la lista por puntaje calificado por la crítica
            lista = sorted(lista, key = lambda x : x[1],reverse = True)

            #Informa los primeros 20 elementos (20 juegos MEJOR CALIFICADOS)
            i = 1
            for elem in lista[:20]:
                print(str(i) + ": " + str(elem))
                i += 1

            #PENDIENTE: CARGAR INFO AL JSON


        #Si el usuario clickea el dataset 2
        if event == "-criterio2-":
            #Genera la lista de datos del csv con la funcion analizar dataset1
            lista = analizar_dataset1(path)

            #Ordenar la lista por puntaje d la critica
            lista = sorted(lista, key = lambda x : x[1],reverse = False)
            
        
            #Informar los primeros 20 elementos (20 juegos PEOR calificados)
            i = 1
            for elem in lista[:20]:
                print(str(i) + ": " + str(elem))
                i += 1
            
            #PENDIENTE: CARGAR INFO AL JSON
            print("LOS VEINTE JUEGOS PEOR CALIFICADOS POR LA CRITICA")



    return window

