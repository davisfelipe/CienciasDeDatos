#Librerias
import matplotlib.image as pltimg
import matplotlib.pyplot as plt
import numpy as np
import os
from prettytable import PrettyTable
from skimage import io
#Funciones Definidas
##Limpiar Consola
clear=lambda: os.system('clear')
##Generar bordes de las imagenes para evitar errores al recorrer la imagen
def duplicarBordes(matriz):
    bordeSup=matriz[:][0]
    bordeInf=matriz[:][matriz.shape[0]-1]
    matriz=np.vstack((bordeSup,matriz))
    matriz=np.vstack((matriz,bordeInf))
    bordeIzq=matriz[:,0]
    bordeDer=matriz[:,matriz.shape[1]-1]
    bordeIzq=np.reshape(bordeIzq,(len(bordeIzq),1))
    bordeDer=np.reshape(bordeDer,(len(bordeDer),1))
    matriz=np.hstack((bordeIzq,matriz))
    matriz=np.hstack((matriz,bordeDer))
    return matriz
##Suavizado de imagene
def suavizadoImagen(matriz):
    col=matriz.shape[1]
    fil=matriz.shape[0]
    imagenSuavizada=np.zeros((fil,col))
    for i in range(1,matriz.shape[0]-1):
        for j in range(1,matriz.shape[1]-1):
            pro=matriz[i-1,j-1]+matriz[i-1,j]+matriz[i-1,(j+1)]+matriz[i,j-1]+matriz[i,j]+matriz[i,(j+1)]+matriz[(i+1),j-1]+matriz[(i+1),j]+matriz[(i+1),(j+1)]
            imagenSuavizada[i,j]=pro/9
    return imagenSuavizada
##Identificación de bordes de la imagen
def bordesImagen(matriz):
    col=matriz.shape[1]
    fil=matriz.shape[0]
    imagenBordes1=np.zeros((fil,col))
    imagenBordes2=np.zeros((fil,col))
    for i in range(1,fil-1):
        for j in range(1,col-1):
            imagenBordes1[i,j]=matriz[i,j]-matriz[i,j-1]
    for i in range(1,col-1):
        for j in range(1,fil-1):
            imagenBordes2[j,i]=matriz[j,i]-matriz[j+1,i]
    imagenCompuesta=((imagenBordes2)**2+(imagenBordes1)**2)**0.5
    for i in range(1,col-1):
        for j in range(1,fil-1):
            if imagenCompuesta[j,i]>1:
                imagenCompuesta[j,i]=1
            elif imagenCompuesta[j,i]<0:
                imagenCompuesta[j,i]=0
    return imagenCompuesta
##Menu de opciones de modificacion de imagen
def Menu():
    menu= PrettyTable(['Filtro','Opcion'])
    menu.add_row(['Suavizado','1'])
    menu.add_row(['Bordes','2'])
    menu.add_row(['Perfilado','3'])
    print(menu)
    opcion=input('Ingrese la opcion:')
    if opcion==1:
        imagenSuavizada=suavizadoImagen(imagen)
        io.imsave('imagenSuavizada.png',imagenSuavizada)
        clear()
        print("Imagen generada como 'imagenSuavizada.png'")
    elif opcion==2:
        imagenBordeada=bordesImagen(imagen)
        io.imsave('imagenBordeada.png',imagenBordeada)
        print("Imagen generada como 'imagenBordeada.png'")
    elif opcion==3:
        print("opcion3") 
    else:
        clear()
        print("Ingrese de nuevo la opcion")
        Menu()
#Ejecución del programa
clear()
img=io.imread('rickymorty.jpg',True)    
imagen=(duplicarBordes(img))
print('Bienvenido a modificacion de imagenes')
Menu()