# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 23:09:40 2020

@author: 81799
"""
import numpy as np
import pandas as pd

"""ESCRITURA
Escritura

<nombre del df>.to_csv("Direccion donde guardarás el archivo /nombre como se guardará.csv", index, header, encoding)

donde

*index es un booleano para saber si imprimir o no los índices
*header es un booleano para saber si imprimir o no los nombres de los campos
*encoding es un string que permite usar la codificación del "idioma" que se usaré. Por default es "UTF-8"; 
se recomienda tenerlo en "latin" para poder usar acentos."""
df = pd.DataFrame({"Nombre":["a","b","c"],"Número":[1,2,3]})
print(df)
df.to_csv("C:/Users/81799/Desktop/Scidata cursos/Tareas C.D.P/Clases/dataframe.csv",index=False, header=True, encoding="latin" )
#%%
"""Lectura y escritura de cvs
Para leer cvs con pandas usamos lo siguiente:
Lectura

<nombre donde se quiere llamar> = pd.read_csv("Direccion donde tienes el archivo a leer /nombre del archivo.csv")
"""
airbnb=pd.read_csv("C:/Users/81799/Desktop/Scidata cursos/Ciencia-de-datos-con-Python/airbnb_cdmx.csv")
a=airbnb.head()  #Este nos ayuda a visualizar el encabezado
print(a)
print(airbnb.columns) #Nos muestra los nombres de las columnas
"""
La agencia de viajes
Supongamos que somos un agente de Airbnb localizado en CDMX, y tenemos que atender peticiones de varios clientes.
Tenemos un archivo llamado airbnb_cdmx.csv donde tenemos información de todos los alojamientos de Airbnb en CDMX

En concreto el dataset tiene las siguientes variables:

id: el identificador de la propiedad
host_id: el identificador del dueño de la propiedad
neighborhood_cleansed: alcaldía en CDMX
property_type: tipo de propiedad
room_type: tipo de habitación
accommodates: El máximo número de personas que se pueden alojar en la propiedad price: precio (en pesos mexicanos)
minimum_nights, maximum_nights: mínimo y máximo de noches
bedrooms: El número de habitaciones
beds: número de camas
cancellation_policy: política de cancelación
number_of_reviews: El numero de opiniones
review_scores_accuracy: Puntuacion media del apartamento"""
#%%
#EJEMPLO 1
"""
Roberto contra su hermana

Roberto es un casero que tiene una casa en Airbnb. De vez en cuando nos llama preguntando sobre cuales son las críticas 
de su alojamiento. Hoy está particularmente molesto, ya que su hermana Valentina ha puesto una casa en Airbnb y Roberto 
quiere asegurarse de que su casa tiene más críticas que las de Valentina. Tenemos que crear un dataframe con las 
propiedades de ambos. Las id de las casas de Roberto y Valentina son 43856289 y 107078 respectivamente."""

problema_2=airbnb[(airbnb["id"]==43856289)|(airbnb["id"]==107078)]
#%%
#EJEMPLO 2
"""
Alicia y su familia
Alicia va a ir la CDMX durante una semana con su marido y sus 2 hijos. Están buscando un apartamento con habitaciones 
separadas para los padres y los hijos. No les importa donde alojarse o el precio, simplemente quieren tener una 
experiencia agradable. Esto significa que solo aceptan lugares con más de 10 críticas con una puntuación mayor de 4. 
Cuando seleccionemos habitaciones para Alicia, tenemos que asegurarnos de ordenar las habitaciones de mejor a peor 
puntuación. Para aquellas habitaciones que tienen la misma puntuación, debemos mostrar antes aquellas con más críticas.
 Debemos darle a lo más la tercera parte del total de posibilidades."""
#Días disponibles ==6
# El número de habitaciones tiene que ser >=2
# El no. de críticas >10
# puntuación >4
#Ordenar de mejor a peor puntuación. En caso de empate, ordenar por número de críticas de forma descendiente
#Dar la tercera parte del total de posibilidades
alicia=airbnb[(airbnb["maximum_nights"]>=6 )& (airbnb["minimum_nights"]<=6) & (airbnb["bedrooms"]>=2)
              & (airbnb["number_of_reviews"]>10) 
             & (airbnb["review_scores_accuracy"]>4)].sort_values(by=["review_scores_accuracy","number_of_reviews"],ascending=[False,False])
a=alicia.head(1076)
b=alicia.iloc[0:round(alicia.shape[0]*.03)]
c=alicia.head(round(alicia.shape[0]/3))
print(b)
#%%
#ejemplo 3
"""Diana "la mochilera"
Diana va a CDMX a pasar 3 noches y quiere conocer a gente nueva. Tiene un presupuesto de 1,250 pesos mexicanos para 
su alojamiento. Debemos buscarle las 10 propiedades más baratas, dandole preferencia a aquellas que sean 
habitaciones compartidas, y para aquellas viviendas compartidas debemos elegir aquellas con mejor puntuación."""
# 3 noches
#1250 pesos mexicanos para alojamiento
#!0 propiedades baratas
#Habitaciones compartidas
c=airbnb[(airbnb["minimum_nights"]<=3)& (airbnb["accommodates"]==1) &(airbnb["price"]<=1250)
         &(airbnb["beds"]>=1) &(airbnb["bedrooms"]>=1)
&(airbnb["room_type"]=="Shared room")].sort_values(by=["review_scores_accuracy","price"],ascending=[False,True])
d=c.head(10)
#%%
d.to_csv("C:/Users/81799/Desktop/Scidata cursos/Tareas C.D.P/Clases/la_mochilera.csv",index=False,header=True,encoding="latin")
#%%

f=airbnb[(airbnb["minimum_nights"]<=3)& (airbnb["room_type"]=="Shared room") &
         (airbnb["price"]<=1250)].sort_values(by=["review_scores_accuracy","price"],ascending=[False,True]).head(10)
f.to_csv("C:/Users/81799/Desktop/Scidata cursos/Tareas C.D.P/la_mochilera.csv",index=False,header=True,encoding="latin")























































