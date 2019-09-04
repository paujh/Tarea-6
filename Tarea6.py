#Haremos un programa con las estadisticas hechas en la clase pasada, solo que ahora los datos para dichas estadisticas, las agarrara de un archivo de texto externo. 
#Primero haremos dicho archivo, con la biblioteca random, que nos dara tanto la longitud del archivo, como los datos con los que se trabajara. 
import random as r
from math import sqrt
datos = open("Datos.txt","w")
for i in range(r.randint(1,100)):
  datos.write(str(r.random())+"\n")
datos.close()
#Ya creado el documento, ahora trabajaremos las estadisticas sobre el. 
def promedio(archivo):
  suma = 0.0
  n = 0
  for linea in archivo:
    numero=float(linea) 
    suma = suma + numero
    n = n + 1
  return suma/n  

def varianza(archivo):
  suma = 0.0
  l = 0
  for linea in archivo:
    numero=float(linea) 
    suma = suma + numero
    l = l + 1
  prom = suma/l 
  m = 0
  suma = 0.0
  for linea in archivo:
    numero = float(linea)
    suma = suma + (numero - prom)**2.0
    m = m + 1
  return suma/m

def desvEst(archivo):
  return sqrt(varianza(archivo))

datos = open("Datos.txt","r")
print("Promedio: ",str(promedio(datos)))
print("Varianza: ",str(varianza(datos)))
print("Desviasion estandar: ",str(desvEst(datos)))
datos.close() 
