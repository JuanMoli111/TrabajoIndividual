import csv

def analizar_dataset1(opc,path):
    """
        Abre y lee el dataset de videojuegos, el criterio de procesamiento de los datos se eligira con el parametro opc
        (por ahora 2 opc que son mostrar los 20 videojuegos mas vendidos y los 20 menos vendidos)
    """

    #Abre el dataset en modo lectura
    with open(path, 'r') as data_set:
        #Crea el objeto reader, sirve para leer las filas de un archivo csv
        reader = csv.reader(data_set, delimiter=',')

        #Guarda la lista del encabezado (rank, nombre, genero... etc)
        header = reader.__next__()


        #Crea una lista vacía, donde almacenará cada fila del csv
        lista = list()
    
        #Itera a traves del csv
        for i in range(20):          
            
            try:
                #Guarda cada linea en la variable line, a medida que el reader avanza. 
                #line es de tipo lista y cada elemento es un valor de la fila del csv 
                line = reader.__next__()
                
            #Si hay excepciones cortar el loop (error de decodificacion o final de archivo)
            except UnicodeDecodeError:
                break
            except StopIteration:
                break

            #Agrega la linea a la lista
            lista.append(line[2])
            #Guarda el titulo del juego, en minusculas, en la variable title  (line[2] es la columa de titulos de los videojuegos)
            title = line[2].lower()            


            #PROCESAMIENTO DE DATOS SI SE ELIGE EL CRITERIO 0, 20 AUTOS MAS VENDIDOS
            if(opc == 0):
                pass    
            #PROCESAMIENTO DE DATOS SI SE ELIGE EL CRITERIO 1, 20 AUTOS MENOS VENDIDOS
            elif(opc == 1):
                pass     
                

            #Jugar con las condiciones
            if((not('a' in line[2])) and (len(line[2]) > 9) and (not('i' in line[2]))):
                print(line[2])

        
    print("#LISTA CONTIENE TODAS LAS LINEAS DEL CSV")


    return lista