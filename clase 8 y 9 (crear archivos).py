# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 22:09:19 2020

@author: 81799
"""
import os 
"""Para crear una carpeta utilizamos os.makedirs(\"ruta donde se creará la carpeta/nombre de la carpeta)  ojo:
    la ruta debe de ir con / diagonal invertida)"""
os.makedirs("C:/Users/81799/Desktop/Scidata cursos/ejemplo")
#%%
"Si queremos crear un archivo para escribir, debemos especificar argumento \"w\" de la siguinte manera"
archivo_para_escribir = open("C:/Users/81799/Desktop/Scidata cursos/usuario", "w")
#Para escribir en el archivo usamos el método write 
archivo_para_escribir.write("Hola mundo\n")
archivo_para_escribir.write("¿Cómo están todos?")
#no se escribe nada hasta que lo cerremos
archivo_para_escribir.close()
#%%
# si volvemos a escribir el argumento "w" en un archivo ya creado, este nuevo docuemnto reescribira el documento
archivo_para_escribir = open("C:/Users/81799/Desktop/Scidata cursos/usuario", "w")
archivo_para_escribir.write("Hola insectos\n")
archivo_para_escribir.close()
#podemos usar el método "a" para escribir sin borrar el original
archivo_para_escribir = open("C:/Users/81799/Desktop/Scidata cursos/usuario", "a")
archivo_para_escribir.write("Voy a dominar su planeta")
archivo_para_escribir.close()
#%%
"Para evitar el open y el close, utilizaremos with"
guerreros_z=["goku","Vegueta","krilin","Yamcha","Ten Chin Han","pikoro","gohan"]
with open("C:/Users/81799/Desktop/Scidata cursos/usuario","w") as archivo_para_escribir:
    for r in guerreros_z:
        archivo_para_escribir.write(f"{r}\n")
#%%
"    LECTURA      "
"Esto es para leer todo el archivo "
with open("C:/Users/81799/Desktop/Scidata cursos/usuario" ) as archivo_para_escribir :
    datos=archivo_para_escribir
    print(datos)

#%%
"""
Si queremos leer cada linea del archivo por separado, usamos el método readlines(), que va leyendo de forma 
iterativa (consume menos memoria) """
cada_linea=[]
with open("C:/Users/81799/Desktop/Scidata cursos/usuario") as prueba:
    lineas=prueba.readlines()
    for linea in lineas:
        cada_linea.append(linea.strip("\n"))
    print(cada_linea)
#%%
datos = {"nombre":["Antonio","Miguel","Julian","Andres"],
         "edad":["45","40","22","34"],
         "ciudad":["Ciudad de México","Puebla","Mexicali","Aguascalientes"]
         }

claves = list(datos.keys())
n_items = len(datos[claves[0]])

with open("C:/Users/81799/Desktop/Scidata cursos/Tareas C.D.P/Clases/dicci.csv", "w") as nombre_archivo:
    nombre_archivo.write(','.join(claves)+"\n")
    for i in range(n_items):
        fila = ",".join([str(datos[clave][i]) for clave in claves])
        nombre_archivo.write(fila+"\n")
        
        