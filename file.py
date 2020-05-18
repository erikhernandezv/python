"""Manejo de archivos en Python"""

def createFile():
    file = open('/home/erik/data.txt', 'w')
    file.close()
    
def writeFile():
    file = open('/home/erik/data.txt', 'a')
    file.write('Escribiendo en el archivo con Python..\n')
    file.write('Fin escritura.. \n')
    file.close()
    
def readingFile():
    file = open('/home/erik/data.txt', 'r')
    line = file.readline()
    
    while line!="":
        print(line)
        line = file.readline()
    file.close()
    
#createFile()
#writeFile()
readingFile()