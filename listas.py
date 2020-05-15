#!/usr/bin/python
# -*- coding: utf-8 -*-

lista01 = ['Mexico','Peru','Irak','Usa','Colombia','Venezuela']
lista02 = ['Holanda','Italia','España','Iran','Cuba']

print('Tamaño de la lista ' + str(len(lista01)))

for itemList in lista01:
    print(itemList)
    
"""Concatenamos dos listas"""
lista02 = lista02 + lista01

print ("\n\n")

for lista02Item in lista02:
    print(lista02Item)

print ("\n\n")
print ("La lista inicialmente es .... \n")
print ( lista01 )
print ("\n\n")

print("Eliminamos el ultimo elemento de la lista ...\n")
print ( lista01.pop())
print ( lista01 )
print ("\n\n")

print ("Eliminamos Elemento de la lista por un indice especifico .... \n")
print ( lista01.pop(2) )
print ( lista01 )
print ("\n\n")

print ("Eliminamos Elemento de la lista directamente por su valor .... \n")
print ( lista01.remove('Mexico') )
print ( lista01 )
print ("\n\n")