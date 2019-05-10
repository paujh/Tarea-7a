#Garcia Azamar Cristopher Alejandro
#crisazami_123@ciencias.unam.mx

from io import open
import random as r

#A)

archivo_texto=open("Coordenadas.txt","w")
cadena=""
for i in range(0,100):
	cadena=cadena+str(r.uniform(0,100))+" "+str(r.uniform(0,100))+"\n"
archivo_texto.write(cadena)
archivo_texto.close()

#Archivo auxiliar de prueba

archivo_texto_2=open("Coordenadas_2.txt","w")
cadena=""
for i in range(0,5):
	cadena=cadena+str(r.uniform(0,100))+" "+str(r.uniform(0,100))+"\n"
archivo_texto_2.write(cadena)
archivo_texto_2.close()