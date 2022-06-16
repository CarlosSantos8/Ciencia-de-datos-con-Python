# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 16:53:34 2020

@author: 81799
"""
import numpy as np

array_1d = np.array([1,2,3])
print(array_1d)
#%%
datos=sorted(list((input("Inserte los datos\n")).split(",")))
datos=np.array(datos)
print(datos)
n=datos.size # Nos da cuantos datos hay
print(n)  
#%%
array_2d = np.array([[1,2,3],[4,5,6]])
print(array_2d)
# <nombre_del_arreglo>.ndim = muestra la dimensión de un arreglo
print(f"El arreglo array_2d tiene un total de {array_2d.ndim} dimensiones")
#%% <nombre_del_arreglo>.shape muestra cuantas columnas y filas hay
print(f"Las cuales valen {array_2d.shape}")
#%% <nombre_del_arreglo>.size dice cuantos elementos hay en total
print(f"El arreglo tiene en total {array_2d.size} elementos" )
#%%
"         INDEXADO        "
r=np.array([[2,4,5,6],[1,3,5,6],[1,6,9,12],[1,2,8,9]])
print(r)
#%%
"""
Los índices en python recuerda que empiezan desde 0, el siguiente ejemplo es como obtener la fila (1,2,3) y los : 
representan que queremos todos los elementos de la columna"""
print(r[1:4,:]) 
 """(1:4) va de la fila (1) a (3) ya que recuerda que en las sucesiones de python 
 hace un rebanado"""
 #%%
 print(r[-1,:][2]) #Accede a la última fila
 print(r[:,-1]) #Accede a la última columna
 #%%
 "     OBSERVACIÓN SOBRE LOS ÍNDICES   "
 # Matriz donde todos los elementos son iguales a 1: np.ones((u,v))
a= np.ones((2,1))
print(a)
#%%
# dtype nos indica los datos el tipo de dato a considerar
b=np.ones((4,3),dtype = int)
print(b)
#%%
# Matriz donde todos los elementos son iguales a 0: np.zeros((u,v))
c=np.zeros((2,1))
print(c)
#%%
# Matriz donde todos sus elementos son vacíos: np.empty((u,v))
e=np.empty((4,5),dtype = str)
print(e)
#%%
f=np.empty((4,3),dtype = bool)
print(f)
#%%
"""La función np.arange().
La función np.arange() generará un arreglo de una dimensión que contiene los enteros definidos en un rango al estilo de
 range().

np.arange(inicio, fin, incrementos, dtype=<tipo de dato>)"""
# Arreglo de una dimensión al estilo de un range: np.arange(<inicio>,<final>,incrementos,dtype)
a=np.arange(5,12)
print(a)
#%%
"""La función np.linspace().
Esta función creará un arreglo de una dimensión que contiene una secuencia  lineal de números dentro de un rango dado 
entre un valor incial y un valor  final. El número de segmentos incluyendo el valor incial y el valor final es definido 
meduante el parámentro num. El valor por defecto del parámetro num es de 50.

np.linspace(inicio, fin, num=segmentos, dtype=tipo de dato)"""
#En este ejemplo buscamos de 0 hasta pi en 100 subintervalos
a=np.linspace(0,np.pi,num=100)
print(a)
#%%
"""La función np.ravel()
La función np.ravel() regresará un arreglo de una dimensión que contiene la referencia de cada uno de los elementos del 
arreglo que se ingresa como  argumento. 
    np.ravel(<arreglo>) """
arreglo_1 = np.array([[1, 2, 3],
                      [4, 0, -5],
                      [-6, -7, -8]])

a=np.ravel(arreglo_1)
print(a)
#%%
"""La función np.reshape().
La función np.reshape() regresará un arreglo compuesto por el mismo número de elementos que el arreglo ingresado como primer argumento, pero con la forma descrita por el objeto de tipo tuple que se ingrese como segundo argumento. Las nuevas dimensiones deben de coincidir con el numero total de elementos del arreglo de origen.

np.reshape(<arreglo>, <forma>)"""
arreglo_2 = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]])
a=arreglo_2.shape #<nombre_del_arreglo>.shape nops dice cuantas filas y columnas hay, de la forma (filas,columnas)
print(a)
print(np.reshape(arreglo_2,(6, 2)))
print(np.reshape(arreglo_2,(2, 6)))
print(np.reshape(arreglo_2,(4, 3)))
#%%
"""La función np.resize()
La función np.resize() regresará un nuevo arreglo a partir del arreglo que se ingrese como primer argumento, con la forma
que se ingrese como segundo argumento.
En caso de que las nuevas dimensiones sean menores a tamaño original, se recortarán los últimos de ellos.
En caso de que las nuevas dimensiones sean mayores al tamaño original, los elementos faltantes serán sustituidos por una 
secuencia iterativa de los elementos contenidos en el arreglo.

np.resize(<arreglo>, <forma>)"""
arreglo_3 = np.array([[1, 2],
                     [3, 4]])
a=np.resize(arreglo_3, (3, 2))
print(a)
#%%
"""La función np.concatenate().
Une una secuencia de arreglos contenidos dentro de un objeto tuple a un eje existente, se puede indicar el eje en el que 
se realizará la operación ingresando su número correspondiente como tercer argumento.

np.concatenate(<arreglo 1>, <arreglo 2>, <eje>)
Donde:

eje = 0 significa pegar arreglo 2 debajo de arreglo 1
eje = 1 significa pegar arreglo 2 a la derecha de arreglo 1 """ 
arreglo_1 = np.array([[1, 2],
                      [3, 4]])

arreglo_2 = np.array([[5, 6],
                      [7, 8]])
a=np.concatenate((arreglo_1, arreglo_2), 0)
print(a)
b=np.concatenate((arreglo_1, arreglo_2), 1)
print(b)

#%%
"""    MATRICES CON ELEMENTOS ALEATORIOS    
La función np.random.rand().

La función np.random.rand() crea un arreglo cuyos elementos son valores aleatorios que van de 0 a antes de 1 dentro de
 una distribución uniforme.

           np.random.rand(<forma>)
"""
a=np.random.rand(4,6)
print(a)
#%%
"""La funciòn np.random.uniform(a,b,[<forma>]) esto sirve para que te genere nùmeros aletorios  entre a y b
"""
b=np.random.uniform(2,5,[3,4])
print(b)
#%%
"""La función np.random.randint().
La función np.random.randint() crea un arreglo cuyos elementos son valores entros aleatorios en un rango dado.

np.random.randint(<inicio>, <fin>, <forma>)"""
a=np.random.randint(1, 6, (3,3))
print(a)
print(a[0])
#%%
b=np.random.randint(1, 250, (10, 3))
print(b)
#%%
"""ÁLGEBRA LINEAL 
Matriz identidad
Se refiere a matrices cuadradas donde todos los elementos son cero excepto aquellos de la diagonal principal, que valen 1"""
a=np.eye(5)
print(a)
#%%
"""Producto puntual (de Hadamard) de dos matrices.
Es el producto "elemento a elemento" de dos matrices. Ambas deben ser del mismo tamaño."""
a=np.array([[1,2,3],[4,5,6]])
print(a)
b=np.array([[0,1,0],[0,0,1]])
print(b)
c=np.array([[1,2,3],[4,5,6]]) * np.array([[0,1,0],[0,0,1]])
print(c)
#%%
A = np.array([[1,4,3],[2,5,1]])
c=(A>= 3)
print(c)
b=(A >= 3 ) * A # De esta manera obtenemos los valores que tenemos por condicional
print(b)
#%%
"""Producto usual de matrices
Es el producto usual de matrices. Se debe tomar en cuenta que si  𝐴  y  𝐵  son dos matrices, para que el producto  𝐴𝐵 
tenga sentido se debe cumplir que el número de columnas de  𝐴  es igual al número de filas de  𝐵 . Se obtiene como 
resultado una matriz con el mismo número de filas que  𝐴  y el mismo número de columnas de  𝐵"""
A = np.array([[1,4,3],[2,5,1]])
B = np.array([[2,3,1,0],[5,5,1,0],[4,1,2,0]])
C=A @ B
print(C)
print(f"La forma de A es {A.shape}; la de B es {B.shape}. Por lo tanto la de AB es {(A @ B).shape}")
#%%
"""El paquete numpy.linalg
La biblioteca especializada en operaciones de algebra lineal de Numpy es numpy.linalg.

Algunas de las funciones mas importantes que contiene son

np.linalg.det()
np.linalg.solve()
np.linalg.inv()
DETERMINANTES """
A = np.arange(9).reshape(3,3)
B=np.linalg.det(A)
print(B)
#%%
"""
Soluciones de ecuaciones lineales con la función np.linalg.solve().
De la forma    Ax=y
La función numpy.linagl.solve() permite resolver sistemas de ecuaciones lineales ingresando un arreglo (A) de 
dimensiones (n, n) como primer argumente y otro(y) con dimensión (n) como segundo argumento."""
a = np.array([[2, 5, -3],
              [11, -4, 22],
              [54, 1, 19]])

y = np.array([22.2, 11.6, -40.1])

x=np.linalg.solve(a, y)
print(x)
#%%
"""
Matriz Inversa """
b=np.linalg.inv(a)
print(a)
#%%
"""Producto usual de matriz"""
d=np.linalg.inv(a).dot(y)
print(d)
#%%
"Transpuesta de una matriz"
b = np.arange(9).reshape((3,3))
c=np.transpose(b)
print(c)
#%%
"Hacer una diagonal con nùmeros dados"
b=np.diagflat(array2[0:5])
print(b)

