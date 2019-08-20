#!/usr/bin/python
# -*- encoding=utf8 -*-

print "Hola Mundo en Python para Daniela Kawiz"

#Algunos tipos de datos en Python

var0 = 9
var1 = "Hola Mundo"
var2 = 9.5

print str(var0)+" "+var1+" "+str(var2)

#Typos de datos
print type(var0)
print type(var1)
print type(var2)

var3 = True
var4 = False
Var4 = "Otro Dato"

print var3
print var4
print Var4

print "\nListas En Python\n"

lista = ["Elemento 1","Elemento 2","Elemento 3","Elemento 4","Elemento 5","Elemento 6"]
print lista

lista2 = list()
lista3 = list(("Elemento 7","Elemento 8","Elemento 9","Elemento 10","Elemento 11","Elemento 12"));

print lista2
print lista3
print lista3[1:3]
print lista[0:6:2]
del(lista3[2])
print lista3

print "\nTuplas en Python\n"

tupla = ('Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis')
tupla1 = ()
print tupla
print tupla1
print tupla[1:3]


print "\nDiccionarios en Python\n"

dictionary = {"Uno":"Elemento 1","Dos":"Elemento 2","Tres":"Elemento 3","4":"Elemento 4","5":"Elemento 5","6":"Elemento 6"}
print dictionary

dictionary1 = dict()
print dictionary1

dictionary2 = {}
print dictionary2

dictionary3 = dict(d1="Datos 1",d2="Datos 2")
print dictionary3


print "\nSet en Python\n"
set1 = set()
set2 = {'Uno','Dos','Tres','Cuatro','Cinco'}
set3 = set(['Seis', 'Siete', 'Ocho', 'Nueve'])
print set1
print set2
print set3
print type(set2)

var3 = "True2"

if var3==True:
	print "Es verdadero"
	print "...."
elif var3==False:
	print "Diferente de verdadero"
	print "Otra linea"
else:
	print "Ninguna de las anteriores"
	print "Que pasa programador.."

print "\nWhile en Python\n"

vardump = 0
while vardump<10 and var3==True:
	vardump+=1
	print vardump*2
else:
	print "Esto es un else del while en Phyton"

print "\nBucle For en Python\n"

listax = ["Elemento 1","Elemento 2","Elemento 3","Elemento 4","Elemento 5","Elemento 6"]

for dato in listax:
	print dato

dictionaryx = {"Uno":"Elemento 1x","Dos":"Elemento 2x","Tres":"Elemento 3x","4":"Elemento 4x","5":"Elemento 5x","6":"Elemento 6x"}

for indice in dictionaryx:
	print dictionaryx[indice]+ ' *** '+indice

#igual que a las lineas anteriores pero con Iteritems()

print "\nBucle For en Python, con iteritem()\n"

for indice, valor in dictionaryx.iteritems():
	print valor+ ' *** '+indice


print "\nExcepciones en Python\n"

try:
	valor = 1000/100;
	print valor
	valor /= 0
	print valor
except:
	print "Exception capturada"

print "Funciones en Python\n"

variable_global = 'Esto es una variable global'
print variable_global

def saludar():
	"""
	Este es el DocString definido para documentar la funcion
	"""

	global variable_global
	variable_global = 'Modificando la variable global desde una función, No recomendado'
	print variable_global
	print "Se saluda dentro de una función en Python"
	print "Luego se verificará que hacer"
	print "Aquí termina el saludo"
	##Retornamos una tupla
	return "Valor", "Datos"

retorno = saludar()
print retorno

def calcular(param, *param1):
	"""
	Esta es una funcion que recibe como parametro argumentos
	"""

	print param

	for i in param1:
		print i

calcular("Datos 1", "Datos 2", "Datos 3")

print "Ejemplo de Decoradores en Python"

def decoradores(funcion_entrada):
	def funcion_salida():
		funcion_entrada()
		print "Dentro del Decorador"
	return funcion_salida

@decoradores
def saludar1():
	print "Hola Decorador"

saludar1()
