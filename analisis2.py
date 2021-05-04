import PySimpleGUI as sg
import csv
from analizarDataset2 import *
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
    window = sg.Window('Analizar el DATASET 2').Layout([
                [sg.Text('Elija algún criterio', size=(30,1), font=("Sawasdee", 25), justification= 'center',key='-text-')],
                [sg.Button('Las veinte marcas de autos mas compradas en USA',key='-criterio1-')],
                [sg.Button('Las veinte marcas europeas mas compradas en USA',key='-criterio2-')],
                [sg.Button('SALIR',key='-exit-')],
            ]) 


    #Path del dataset de autos
    path = 'C:/Users/EXO/Desktop/Facu/FACULTAD/Seminario de Lenguajes - Python/trabajo individual/Datasets/DatasetAutos-Logos/companies.csv'

    while True:
        event, values = window.read()

        #Si el usuario clickea en salir
        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-","salir","Salir"):
            break

        #Si el usuario clickea el criterio 1
        if event == '-criterio1-':

            #Genera la lista de datos del csv con la funcion analizar dataset2
            lista = analizar_dataset2(False,path)

            #Lista generada:
            # [0] = RANK , [1] = MARCA

            #Ordenar la lista por rank
            lista = sorted(lista, key = lambda x : x[0])

            #Crear el dicc que se usara para cargar datos al json
            data = {}
            data['info_autos'] = list()


            #Informa los primeros 20 elementos (20 autos mas comprados en USA)
            i = 1
            for elem in lista[:20]:
                print(str(i) + ": " + str(elem[1]))

                d = {   
                    'rank' : i,
                    'marca': elem[1]
                }   

                data['info_autos'].append(d)
                i += 1
           
            #Path para el archivo json que contendrá las marcas de los autos mas vendidos
            path_json = 'C:/Users/EXO/Desktop/Facu/FACULTAD/Seminario de Lenguajes - Python/trabajo individual/data2crit1.json'

            #Abrir o crear el json, y agregar data
            try:
                with open(path_json,'x') as json_file:
                    json.dump(data, json_file, indent=4)
                sg.popup("Se ha creado un archivo json con las 20 marcas de autos mas compradas en USA")
            except FileExistsError:
                sg.popup("Ya se creó el json del analisis del dataset")

        #Si el usuario clickea el criterio 2
        if event == "-criterio2-":
            #Genera la lista de datos del csv con la funcion analizar dataset2
            lista = analizar_dataset2(True,path)
            #Lista generada:
            # [0] = RANK , [1] = MARCA

            #Ordenar la lista por rank
            lista = sorted(lista, key = lambda x : x[0])
            
            #Crear el dicc que se usara para cargar datos al json
            data = {}
            data['info_autos'] = list()
            

            #Informar los primeros 20 elementos (20 autos europeos mas comprados en USA)
            i = 1
            for elem in lista[:20]:
                print(str(i) + ": " + str(elem[1]))
                
                d = {
                'rank' : i,
                'marca': elem[1]
                }   

                data['info_autos'].append(d)
                i += 1

            
           
            #Path para el archivo json que contendrá las marcas de los autos europeos mas vendidos
            path_json = 'C:/Users/EXO/Desktop/Facu/FACULTAD/Seminario de Lenguajes - Python/trabajo individual/data2crit2.json'

            #Abrir o crear el json, y agregar data
            try:
                with open(path_json,'x') as json_file:
                    json.dump(data, json_file, indent=4)
                sg.popup("Se ha creado un archivo json con las 20 marcas de autos europeos mas compradas en USA")
            except FileExistsError:
                sg.popup("Ya se creó el json del analisis del dataset")

    return window

