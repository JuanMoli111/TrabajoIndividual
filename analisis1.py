import PySimpleGUI as sg
import csv
from analizarDataset1 import *
from test import *
import json

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
                [sg.Button('Los veinte videojuegos mejor calificados',key='-criterio1-')],
                [sg.Button('Los veinte videojuegos peor calificados',key='-criterio2-')],
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

        #Si el usuario clickea el criterio 1
        if event == '-criterio1-':

            #Genera la lista de datos del csv con la funcion analizar dataset1
            lista = analizar_dataset1(path)

            #Lista generada:
            # [0] = NOMBRE VIDEOJUEGO , [1] = PUNTAJE CRITICA


            #Ordena la lista por puntaje calificado por la crítica
            lista = sorted(lista, key = lambda x : x[1],reverse = True)

            #Crear el dicc que se usara para cargar datos al json
            data = {}
            data['info_videojuegos'] = list()


            #Informa los primeros 20 elementos (20 juegos MEJOR CALIFICADOS)
            i = 1
            for elem in lista[:20]:
                print(str(i) + ": " + str(elem[0]))

                d = {   
                    'nombre' : elem[0],
                    'puntaje': elem[1]
                }   

                data['info_videojuegos'].append(d)
                i += 1
            
            #Path para el archivo json que contendrá los nombres de los videojuegos mejor calificados
            path_json = 'C:/Users/EXO/Desktop/Facu/FACULTAD/Seminario de Lenguajes - Python/trabajo individual/data1crit1.json'

            #Abrir o crear el json, y agregar data
            try:
                with open(path_json,'x') as json_file:
                    json.dump(data, json_file, indent=4)
                sg.popup("Se ha creado un archivo json con los nombre de los 20 videojuegos mejor calificados")
            except FileExistsError:
                sg.popup("Ya se creó el json del analisis del dataset")


        #Si el usuario clickea el criterio 2
        if event == "-criterio2-":
            #Genera la lista de datos del csv con la funcion analizar dataset1
            lista = analizar_dataset1(path)
            #Lista generada:
            # [0] = NOMBRE VIDEOJUEGO ,[1] = PUNTAJE CRITICA


            #Ordenar la lista por puntaje d la critica
            lista = sorted(lista, key = lambda x : x[1],reverse = False)
            
            #Crear el dicc que se usara para cargar datos al json
            data = {}
            data['info_videojuegos'] = list()

            #Informar los primeros 20 elementos (20 juegos PEOR calificados)
            i = 1
            for elem in lista[:20]:
                print(str(i) + ": " + str(elem[0]))

                d = {   
                    'nombre' : elem[0],
                    'puntaje': elem[1]
                }   

                data['info_videojuegos'].append(d)
                i += 1
            
            #Path para el archivo json que contendrá los nombres de los videojuegos peor calificados
            path_json = 'C:/Users/EXO/Desktop/Facu/FACULTAD/Seminario de Lenguajes - Python/trabajo individual/data1crit2.json'

            #Abrir o crear el json, y agregar data
            try:
                with open(path_json,'x') as json_file:
                    json.dump(data, json_file, indent=4)
                sg.popup("Se ha creado un archivo json con los nombre de los 20 videojuegos peor calificados")
            except FileExistsError:
                sg.popup("Ya se creó el json del analisis del dataset")


    return window

