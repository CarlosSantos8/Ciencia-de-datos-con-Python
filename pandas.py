# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 18:07:34 2020

@author: 81799
"""
"    PANDAS      "
import pandas as pd
import numpy as np
"""Series
Los objetos instanciado de la clase pandas.Series son de una sola dimensión y pueden ser al ingresar como argumento de
data objetos de tipo:

tuple
list
dict
numpy.ndarray
A las series se les puede asignar un nombre mediante el parametro name."""
#%%
serie_1=pd.Series(np.random.rand(8)) #no.random.rand(n) sirve para gener n elementos aleatorios
print(serie_1)
#%%
serie_1=pd.Series(np.random.rand(8),name="mi primer serie")
print(serie_1)
#%%
print(serie_1[4])  #Aquí busca el índice con el que te proporciono la serie
#%%
"podemos especificar los valores de los índices"
#index
serie_2=pd.Series(np.random.rand(8),index=range(1,9),name="mi primer serie")
print(serie_2)
#%%
"podemos especificar los valores de los índices más generalmente"
serie_4=pd.Series(np.random.rand(5),index=[3,4,2,7,8])
print(serie_4)
a=serie_4[3]  #busca el índice 3 de la serie 
print(a)
#%%
serie_3=pd.Series(np.random.rand(5),index=["a","b","c","d","e"])
print(serie_3)
b=serie_3[0] #Cuando el indexado son letras, entonces el índice 0 la posición la toma como a
c=serie_3[2:4]
print(b)
print(c)
#%%
"""Incluso los diccionarios se pueden convertir en series
En este caso, los índices son las claves 
"""
nombre=pd.Series({"nombre":["Roberto","Carlos"],"Apellidos":["Santos","Alonzo"]})
print(nombre)
#%%
nombre1=pd.Series({"nombre":["Roberto","Carlos"],"Apellidos":["Santos"]})
print(nombre1)
""""Es importante notar que las series son estructuras de datos en una sola dimensión. Si queremos estructuras mas 
complejas, debemos usar dataframes."""
#%%
"                   DATAFRAMES                                   "

"""Los dataframes son similares a un aerreglo en 2 dimensiones de Numpy. Sin embargo, a diferencia de los arreglos de 
Numpy, no todas las columnas de estos objetos deben de ser necesariamente del mismo tipo.

La clase pandas.DataFrame permite crear dataframes a partir de datos que pueden corresponder a:
Objetos de tipo dict.
Series objetos tipo tuple.
Objetos numpy.ndarray (arreglos que contienen sólo números).
Otros objetos instanciado de pandas.DataFrame.
Dichos datos pueden ser ingresados como argumentos del parámetro data al instanciarlos.

Los dataframes indexan por defecto las columnas y los encabrezados con valores numéricos. Sin embargo, estos pueden 
ser modificados por el usuario.
"""
a=pd.DataFrame(data=[(0,1,2),(3,2,5),(6,2,8)])
print(a)
#%%
estudiantes = {'Nombre':["Hugo", "Paco", "Luis" ,"Pedro", "Juan", "Pablo"], 
                'Apellido':["López", "Silva", "Oca" , "Ramírez", "Gutiérrez", np.nan], 
                'Matrícula':["123455", "736923", "971298" ,"123098", "987656", "878652"], 
                'Edad':[20, 35, 30 ,25, np.nan, 23]}
a=pd.DataFrame(estudiantes)
print(a)
#%%
matriz = np.arange(9).reshape(3,3)
matriz=pd.DataFrame(matriz)
print(matriz)
#%%
"El parámetro index, permite incluir un índice a cada renglón."
reg=["1era persona","2da persona","3era persona","4ta persona","5ta persona","6ta persona"]#Puede ser lista o tuplka
v=pd.DataFrame(estudiantes,index=reg) #Puedes poner data=estudiantes o solamente estudiantes
print(v)
#%%
"El parámetro columns permite nombrar a las columnas."
#columns
matriz = np.arange(9).reshape((3,3))
a=pd.DataFrame(matriz,index=("uno","dos","tres"),columns=["a","b","c"])
print(a)
print(a)
#%%
a=pd.DataFrame(
[["Hugo","López",123455,20],
 ["Paco","Silva",736923,35],
 ["Luis","Oca",971298],
 ["Pedro","Ramírez",123098]    
], index = ["Registro 1","Registro 2","Registro 3","Registro 4"],
    columns = ["Nombre","Apellido","Matrícula","Edad"]
)
print(a)
#%%
"""Acceso a los elementos de un dataframe

Podemos accesar a los elementos de un dataframe mediante las siguientes maneras. Consideremos nuevamente el dataframe
 anterior:"""
a=pd.DataFrame(
[["Hugo","López",123455,20],
 ["Paco","Silva",736923,35],
 ["Luis","Oca",971298],
 ["Pedro","Ramírez",123098]    
], index = ["Registro 1","Registro 2","Registro 3","Registro 4"],
    columns = ["Nombre","Apellido","Matrícula","Edad"]
)
# Acceso a una columna: usando el nombre de los campos
print(a["Nombre"])
#%%
# Acceso a varias columnas: usando el nombre de los campos
print(a[["Nombre","Edad"]])
#%%
# Acceso a una fila mediante el nombre del ínice del registro
print(a.loc[["Registro 2","Registro 4"]])
#%%
# Acceso a una fila mediante el número del índice del registro
print(a.iloc[1])
#%%
# Acceso a ciertas columnas y ciertas filas.
print(a.loc[["Registro 1","Registro 4"]][["Matrícula","Edad"]])
#%%
"""Operaciones básicas de dataframes
También es posible añadir nuevas columnas a un dataframe utilizando columnas que ya existen."""
a["Nombre completo"] = a["Nombre"] + " " + a["Apellido"]
print(a)
#%%
"Eliminado de columnas"
#inplae=True significa que si reemplaza en la original, si se pone False, lo hace pero no lo reemplaza
a.drop("Nombre completo",axis = 1,inplace = True)  #axis=1 ->columna axis=0-> filas 
print(a)
#%%
"Indexar numéricamente los registros"
a.reset_index(inplace = True)
print(a)
#%%
"Acceso a ciertas columnas y ciertas filas."
b=a.loc[[0,3],["Matrícula","Edad"]]
print(b)
#%%
"Acceso a ciertas columnas y ciertas filas."
c=a[a["Edad"]>20]
print(c)
#%%
"Incluso podemos hacer seleción por filtrado"
d=c[["index","Edad","Matrícula"]]
print(d)
#%%
"Cambiando los nombres de las columnas"
a.columns = ["Campo 1","Campo 2","Campo 3","Campo 4","Campo 5"]
print(a)
#%%
"Cambiando los nombres de las filas"
a.index = a["Campo 4"]
print(a)
#%%
"Agregado de una fila"
nuevo_elemento = "Registro 5,Helena,González,888888,29".split(",")
a.loc[888888] = nuevo_elemento
print(a)
#%%
w=a.iloc[-1]
print(w) 
#%%
print(a.head(2)) #Es una herramiento para visualizar n datos, sino se pone ningun valor te da los primeros 5
#%%
a["Campo 5"] = pd.to_numeric(estudiantes["Campo 5"], downcast = "float")
#%%
print(type(a.iloc[4]["Campo 5"])) #Esto aparece porque cuando ocupas .split() los convierte en str
#%%
"   PROCEDIMIENTO DE DATOS       to numeric"
a["Campo 5"] = pd.to_numeric(a["Campo 5"], downcast = "float")
print(a)
#%%
"suma de datos   .sum() "
b=a["Campo 5"].sum()    #suma de datos
print(b)
#%%
" promedio de datos .mean()   "
promedio=a["Campo 5"].mean()
print(promedio)
#%%
" Tabla de frecuencias "
q=a["Campo 5"].value_counts()
print(q)
#%%
a.loc[777222] = ["Registro 6","José","López","777222",30]
print(a)
#%%
m=a["Campo 3"].value_counts()
print(m)
#%%
"   ORDENAMIENTOS   "
estudiantes = pd.DataFrame(
[["Hugo","López","123455",20],
 ["Paco","Silva","736923",35],
 ["Luis","Silva","971298"],
 ["Pedro","Ramírez","123098"]    
], index = ["Registro 1","Registro 2","Registro 3","Registro 4"],
    columns = ["Nombre","Apellido","Matrícula","Edad"]
)
estudiantes["Nombre completo"] = estudiantes["Nombre"] + " " + estudiantes["Apellido"]
estudiantes.columns = ["Campo 1","Campo 2","Campo 3","Campo 4","Campo 5"]
estudiantes.sort_values(by = "Campo 5",inplace = True, ascending=False)
print(estudiantes)
#%%
estudiantes["Campo 4"] = pd.to_numeric(estudiantes["Campo 4"], downcast = "float")
print(estudiantes)
#%%
edad_media=estudiantes["Campo 4"].mean()
print(edad_media)
"reasignación de los NaN"
estudiantes["Campo 4"].fillna(float(edad_media),inplace = True)
print(estudiantes)
#%%
"Ordenamiento por 2 condiciones "
estudiantes.sort_values(by = ["Campo 2","Campo 1"],ascending = [True,True],inplace = True)
print(estudiantes)
#%%
"Subtablas donde coincidan los datos"
r=estudiantes[estudiantes ["Campo 2"]=="Silva"]
print(r)
#%%
"Convertir a mayusculas las columnas"
estudiantes["Campo 1"]=estudiantes["Campo 1"].str.upper() 
print(estudiantes)
#%%
"Contar los ekementos de una columna"
estudiantes["Campo 1"].str.len
print(estudiantes)
#%%
"Añadiendo una nueva fila"
estudiantes.loc["536271"] = ["Luisa","González","12534",23,"Luisa Gónzalez"]
#%%
"Añadiendo una nueva columna"

estudiantes["Estado"] = ["Activo","Baja","Baja","Graduado","Activo"]
print(estudiantes)
#%%
"Creando un nuevo DataFrame acerca de  la columna estado"
s=pd.get_dummies(estudiantes["Estado"])
print(s)
#%%
"pd.concat([arreglo,agregar_arreglo],axis=(1 o 0)"
#axis=0-> pega la tabla abajo, axis=1->pega la tabala a ala derecha
Frame=pd.concat([estudiantes,s],axis=1)
print(Frame)
#%%
Frame["FAC"]=[4,3,6,4,5]
Frame["Sexo"]=[1,1,1,1,0]
print(Frame)
#%%
".groupby Agrupa la tabla respecto a la columna( que des"
r=Frame.groupby("Estado")["FAC"].sum()
print(r)
#%%
".groupy agrupa la tabla respecto a las columnas dadas"
x=Frame.groupby(['Estado',"Sexo"])["FAC"].sum()
print(x)
#%%
"ANALISIS ESTADÍSTICO"
describe=Frame.describe()
print(describe)






























































































