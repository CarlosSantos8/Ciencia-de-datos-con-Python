# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 01:50:26 2020

@author: 81799
"""
import os

def a(r):
    m=[]
    with open(p) as prueba:
        a=prueba.readlines()
        for linea in a :
            m.append(len(linea.strip("\n")))
        print(f"\nHay {m.count(max(m))} linea(s) con mayor longitud:")
        for i in a:        
            if len(i.strip("\n"))==max(m):
                print(i)
p=str(input("Inserta el ruta\n "))
a(p)
#%%
def b(a,b,c):
    d="C:/Users/81799/Desktop/Scidata cursos/Tareas C.D.P/"+c+".txt"
    m=[]
    with open(r) as rut:
        a=rut.readlines()
        for t in a:
            m.append(t.strip("\n"))
        n=m[::-1][:sa]
        if len(n)>=sa:
            with open(d,"w") as new:
                for w in n:
                    new.write(f"{w}\n")
        else: 
            print(f"No se puede agregar las últimas {sa} lineas, ya que hay solamente {len(n)} lineas en el documento")
    
r=str(input("Ingresa la ruta de donde quieres agarrar las últimas n-lineas\n"))
sa=int(input("Ingresa cuantas últimas lineas quieres agregaar a tu archivo \n"))
e=str(input("inserta el nommbre de tu nuevo documento\n"))
b(r,sa,e)
#%%
class Vehículo:
    def __init__(self,modelo,color):
        self.modelo=modelo
        self.color=color
class Carro(Vehículo):
    pass
class Otro(Vehículo):
    pass
class Taxi(Vehículo):
      def Cobrar(self,distancia_recorrida):
            self.distancia_recorrida=distancia_recorrida
            print(f"El taxi es un {self.modelo} {self.color}\nTu viaje duró:{self.Tiempo()} hrs")
            print(f"Usted debe pagar:{self.pago()}")
      def Tiempo(self):
            tiempo="{0:.2f}".format(self.distancia_recorrida/self.velocidad)
            return tiempo
      def pago (self):
            pagar="{0:.2f}".format(4.46*self.distancia_recorrida)
            return pagar
f=Carro("Volkwagen", "Amarillo")
taxi=Taxi("Volkwagen", "Amarillo")
taxi.velocidad=float(input("Ingrese la velocidad del taxi en km \t"))
taxi.Cobrar(float(input("Ingresa la distancia recorrida en km \t")))
#%%
class Vehículo:
    def __init__(self,auto,modelo,color,matricula):
        self.modelo=modelo
        self.color=color
        self.auto=auto
        self.matricula=matricula
class Carro(Vehículo):
    pass
class Otro(Vehículo):
    pass
class Parking:
    def __init__(self, auto,modelo,color,matricula):
        self.z=[]
        self.auto=auto 
        self.modelo=modelo 
        self.color=color
        self.matricula=matricula
    def Estacionamiento (self):
        if type(m)!=Carro:
                print(f"No estacionamos {self.auto}")
        elif type(m)==Carro and len(z)<x:
            if self.matricula in z:
                print(f"No se puede estacionar el {self.auto} porque ya està estacionado")
            else:
                z.append(self.matricula)
                print(f"Se estacionò el {self.auto} modelo {self.modelo} color {self.color} con matricula {self.matricula} ")
                print(f"Hay {len(z)} vehículos estacionados")
                print(f"El porcentaje de ocupaciòn es: {(len(z)*100)/x}% ")
        else:
            print("No hay espacio en estacionamiento")  
    def salir_coche(self):
        if self.matricula in z:
            z.remove(self.matricula)
            print(f"Hay {len(z)} vehículos estacionados")
            print(f"El porcentaje de ocupaciòn es: {(len(z)*100)/x}%")
        else:
            print("No hay coche estacionado con esa placa")
x=int(input("Ingrese cuantos lugares disponibles hay \n"))
p=int(input("Ingresa los automoviles que quieren entrar\n"))
print("Ingresa las característcas del automovil que va a estacionar\n\t<tipo>,<modelo>,<color>,<placas>")
print("Ejemplos:\n Carro,nissan,amarillo,ABC\nmoto,suzuki,azul,BCR" );z=[]
for i in range(p):
   y=(input(f"Ingresa las características del automovil {i+1}\n")).split(",")
   print(y[0].upper())
   if  y[0].upper()=="CARRO":
       m=Carro(auto=y[0],modelo=y[1],color=y[2],matricula=y[3])
   elif y[0].upper()!="CARRO":
       m=Otro(auto=y[0],modelo=y[1],color=y[2],matricula=y[3])
   Estacion_SciData=Parking(auto=y[0],modelo=y[1],color=y[2],matricula=y[3])
   Estacion_SciData.Estacionamiento()
q=int(input("Ingresa los automoviles que quieren salir\n"))
for r in range(q):
   y=(input(f"Ingresa las características del automovil que quiere salir \n")).split(",")
   m=Carro(auto=y[0],modelo=y[1],color=y[2],matricula=y[3])
   Estacion_SciData=Parking(auto=y[0],modelo=y[1],color=y[2],matricula=y[3])
   Estacion_SciData.salir_coche()
   #%%
   import numpy as np
a=np.transpose(np.reshape(np.arange(1,16),(3,5)))
print(f"1)\n {a}")
print(f"2)\nEl arreglo tiene un total de {a.ndim} dimensiones\nlas cuales valen {a.shape} ")
print(f"por lo cual cuenta con {a.size} elementos")
b=a[:,1]
print(f"3)\n{b}")
array2=np.arange(15,56)
print(f"4)\n array2 = {array2}")
array2[4]=23
print(f"5)\n {array2}")
array2=array2[::-1]
print(f"6)\n{array2}")
matriz_diag=np.diag(array2[0:5])
print(f"7)\n {matriz_diag}")
print(f"8\nEl arreglo tiene un total de {matriz_diag.ndim} dimensiones \nlas cuales valen {matriz_diag.shape}")
print(f"por lo tanto tiene {matriz_diag.size} elementos")
matriz_aleatoria=np.random.rand(5,3)
print(matriz_aleatoria)
print(matriz_diag.dot(matriz_aleatoria))
#%%
import numpy as np
import pandas as pd
airbnb=pd.read_csv("C:/Users/81799/Desktop/Scidata cursos/Ciencia-de-datos-con-Python/airbnb_cdmx.csv")
"""Diana "la mochilera"
Diana va a CDMX a pasar 3 noches y quiere conocer a gente nueva. Tiene un presupuesto de 1,250 pesos mexicanos para 
su alojamiento. Debemos buscarle las 10 propiedades más baratas, dandole preferencia a aquellas que sean 
habitaciones compartidas, y para aquellas viviendas compartidas debemos elegir aquellas con mejor puntuación."""
# 3 noches
#1250 pesos mexicanos para alojamiento
#!0 propiedades baratas
#Habitaciones compartidas
f=airbnb[(airbnb["minimum_nights"]<=3)& (airbnb["room_type"]=="Shared room") &
         (airbnb["price"]<=1250)].sort_values(by=["review_scores_accuracy","price"],ascending=[False,True]).head(10)
f.to_csv("C:/Users/81799/Desktop/Scidata cursos/Tareas C.D.P/la_mochilera.csv",index=False,header=True,encoding="latin")
















''