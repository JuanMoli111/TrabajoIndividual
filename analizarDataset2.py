import csv

def analizar_dataset2(EU,path):
    """
        Abre y lee el dataset de autos, almacena en una lista la informacion
        necesaria para el json y la retorna
        El parametro booleano EU determina si la lista será solo de marcas de
        auto europeas, o no
    """

    #Abre el dataset en modo lectura
    with open(path, 'r') as data_set:
        #Crea el objeto reader, sirve para leer las filas de un archivo csv
        reader = csv.reader(data_set, delimiter=',')

        header = reader.__next__()
        print(header)

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

            if(EU):
                #Filtra los autos que no han registrado los datos necesarios
                if((line[2] == 'France' or line[2] == 'Italy' or line[2] == 'United Kingdom' or line[2] == 'Sweden' or line[2] == 'Germany') and ((not(line[0] == '')) and (not(line[0] == None)) and (not(line[2] == '')) and (not(line[2] == None)) and (not(line[4] == '')) and (not(line[4] == None)))):
                    #Genera la lista con la informacion del csv, a medida que itera
                    lista.append([int(line[0]),line[3]])
            else:
                if((not(line[0] == '')) and (not(line[0] == None)) and (not(line[2] == '')) and (not(line[2] == None)) and (not(line[4] == '')) and (not(line[4] == None))):
                    #Genera la lista con la informacion del csv, a medida que itera
                    lista.append([int(line[0]),line[3]])

    return lista