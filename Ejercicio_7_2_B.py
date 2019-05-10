#Garcia Azamar Cristopher Alejandro
#crisazami_123@ciencias.unam.mx

from io import open
import random as r

#Funciones axuliares

def Coordenadas_X(ArchivoDeTexto):
	Archivo_de_texto=open(ArchivoDeTexto,"r")
	lista_renglones=Archivo_de_texto.readlines()
	Archivo_de_texto.close()
	lista_coordenadas_X=[]
	for i in range(0,len(lista_renglones)):
		cadenita=""
		for k in range(0,len(lista_renglones[i])):
			if lista_renglones[i][k]==" ":
				indice_1=k
		for s in range(0,indice_1):
			cadenita=cadenita+lista_renglones[i][s]
			
			
		x=float(cadenita)
		lista_coordenadas_X.append(x)
	return lista_coordenadas_X

def Coordenadas_Y(ArchivoDeTexto):
	Archivo_de_texto=open(ArchivoDeTexto,"r")
	lista_renglones=Archivo_de_texto.readlines()
	Archivo_de_texto.close()
	lista_coordenadas_Y=[]
	for i in range(0,len(lista_renglones)):
		cadenita=""
		for k in range(0,len(lista_renglones[i])):
			if lista_renglones[i][k]==" ":
				indice_1=k
		for t in range(0,len(lista_renglones[i])):
			if lista_renglones[i][t]=="\n":
				indice_2=t
		for s in range(indice_1+1,indice_2):
			cadenita=cadenita+lista_renglones[i][s]
			
			
		y=float(cadenita)
		lista_coordenadas_Y.append(y)
	return lista_coordenadas_Y

print(Coordenadas_X("Coordenadas_2.txt"))
print(Coordenadas_Y("Coordenadas_2.txt"))

#B)

def Extremos(ArchivoDeTexto):
	Lista_ordenadas=Coordenadas_Y(ArchivoDeTexto)
	Lista_absisas=Coordenadas_X(ArchivoDeTexto)
	no_maximos_L=[]
	no_minimos_L=[]
	
	for i in range(0,len(Lista_ordenadas)):
		for k in range(0,len(Lista_ordenadas)):

			if Lista_ordenadas[i]-Lista_ordenadas[k]<0:
				no_maximos_L.append(Lista_ordenadas[i])	
			else:
				continue
	no_maximos=set(no_maximos_L)
	ordenadas=set(Lista_ordenadas)
	maximo=list(ordenadas-no_maximos)			

	for i in range(0,len(Lista_ordenadas)):
		for k in range(0,len(Lista_ordenadas)):

			if Lista_ordenadas[i]-Lista_ordenadas[k]>0:
				no_minimos_L.append(Lista_ordenadas[i])	
			else:
				continue

	no_minimos=set(no_minimos_L)
	minimo=list(ordenadas-no_minimos)

	for u in range(0,len(Lista_ordenadas)):
		if Lista_ordenadas[u]==maximo[0]:
			indice_maximo=u
		else:
			continue

	for v in range(0,len(Lista_ordenadas)):
		if Lista_ordenadas[v]==minimo[0]:
			indice_minimo=v
		else:
			continue

	PuntoNorte="Punto mas al norte: "+str(Lista_absisas[indice_maximo])+" "+str(maximo[0])+"\n"
	PuntoSur="Punto mas al sur: "+str(Lista_absisas[indice_minimo])+" "+str(minimo[0])+"\n"

	print(PuntoNorte)

	print(PuntoSur)

Extremos("Coordenadas_2.txt")
Extremos("Coordenadas.txt")

#C

def Centroide(ArchivoDeTexto):
	Lista_absisas=Coordenadas_X(ArchivoDeTexto)
	Lista_ordenadas=Coordenadas_Y(ArchivoDeTexto)
	Suma_absisas=0
	Suma_ordenadas=0

	for i in range(0,len(Lista_absisas)):
		Suma_absisas=Suma_absisas+Lista_absisas[i]
		Suma_ordenadas=Suma_ordenadas+Lista_ordenadas[i]

	Centroide_x = Suma_absisas/len(Lista_absisas)
	Centroide_y = Suma_ordenadas/len(Lista_ordenadas)

	Centroide= "Centroide = "+str(Centroide_x)+" "+str(Centroide_y)+"\n"
	print(Centroide)

Centroide("Coordenadas_2.txt")
Centroide("Coordenadas.txt")

#D

def PuntoAleatorio(ArchivoDeTexto):
	Lista_absisas=Coordenadas_X(ArchivoDeTexto)
	Lista_ordenadas=Coordenadas_Y(ArchivoDeTexto)
	n=r.randint(0,len(Lista_absisas)-1)
	PuntoAleatorio = "Puntos aleatorio: "+str(Lista_absisas[n])+" "+str(Lista_ordenadas[n])+"\n"
	print(PuntoAleatorio)

PuntoAleatorio("Coordenadas_2.txt")
PuntoAleatorio("Coordenadas.txt")



