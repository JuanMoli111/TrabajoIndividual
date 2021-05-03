import csv

def analizar_dataset1(path):
    """
        Abre y lee el dataset de videojuegos, el criterio de procesamiento de los datos se eligira con el parametro opc
        (por ahora 2 opc que son mostrar los 20 videojuegos mas vendidos y los 20 menos vendidos)
    """

    #Abre el dataset en modo lectura
    with open(path, 'r') as data_set:
        #Crea el objeto reader, sirve para leer las filas de un archivo csv
        reader = csv.reader(data_set, delimiter=',')

        reader.__next__()

        #Crea una lista vacía, donde almacenará cada fila del csv
        lista = list()
    
        #Itera a traves del csv
        while True:          
            
            try:
                #Guarda cada linea en la variable line, a medida que el reader avanza. 
                #line es de tipo lista y cada elemento es un valor de la fila del csv 
                line = reader.__next__()

            #Si hay excepciones cortar el loop (error de decodificacion o final de archivo)
            except UnicodeDecodeError:
                break
            except StopIteration:
                break

            #Filtra los juegos que no han registrado los datos necesarios
            if((not(line[9] == '')) and (not(line[9] == None)) and (not(line[1] == '')) and (not(line[1] == None))):
                #Genera la lista con la informacion del csv, a medida que itera
                lista.append([line[1],float(line[9])])

    return lista