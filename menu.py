import PySimpleGUI as sg
import json
import os.path

import PIL.Image
import io
import base64

def convert_to_bytes(file_or_bytes, resize=None):
    '''
    Will convert into bytes and optionally resize an image that is a file or a base64 bytes object.
    Turns into  PNG format in the process so that can be displayed by tkinter
    :param file_or_bytes: either a string filename or a bytes base64 image object
    :type file_or_bytes:  (Union[str, bytes])
    :param resize:  optional new size
    :type resize: (Tuple[int, int] or None)
    :return: (bytes) a byte-string object
    :rtype: (bytes)
    '''
    if isinstance(file_or_bytes, str):
        img = PIL.Image.open(file_or_bytes)
    else:
        try:
            img = PIL.Image.open(io.BytesIO(base64.b64decode(file_or_bytes)))
        except Exception as e:
            dataBytesIO = io.BytesIO(file_or_bytes)
            img = PIL.Image.open(dataBytesIO)

    cur_width, cur_height = img.size
    #Resizing 
    if resize:
        new_width, new_height = resize
        scale = min(new_height/cur_height, new_width/cur_width)
        img = img.resize((int(cur_width*scale), int(cur_height*scale)), PIL.Image.ANTIALIAS)

    bio = io.BytesIO()
    img.save(bio, format="PNG")
    del img
    return bio.getvalue()

def start():
    """
    Lanza la ejecución de la ventana del menú de inicio
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
                [sg.Button('Dataset2',key='-data2-')],
                [sg.Button('SALIR',key='-exit-')],
                [sg.Image(key='-IMAGE-')],
                [sg.Text('Folder'), sg.In(size=(25,1), enable_events=True ,key='-FOLDER-'), sg.FolderBrowse()],
                [sg.Listbox(values=[], enable_events=True, size=(40,20),key='-FILE LIST-')],
                [sg.Text('Resize to'), sg.In(key='-W-', size=(5,1)), sg.In(key='-H-', size=(5,1))]  
                ])

    
    while True:
        event, values = window.read()

        path = 'C:/Users/EXO/Desktop/Facu/FACULTAD/Seminario de Lenguajes - Python/trabajo individual/Imagenes'

        values['-FOLDER-'] = path

        file_list = os.listdir(path)

        print(file_list)


        for i in range(len(file_list)):
            filename = os.path.join(path, file_list[i])
            window['-IMAGE-'].update(data=convert_to_bytes(filename))

        #Si el usuario clickea en salir
        if event == '-exit-':
            break

        if event == 'WIN_CLOSED':
            return window

        #Si el usuario clickea el dataset 1
        if event == '-data1-':
            
            print("Eligio el dataset1")


        #Si el usuario clickea el dataset 2
        if event == "-data2-":
            
            print("Eligio el dataset2")


    return window

