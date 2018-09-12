"""
Parcial de ciencias de los datos

Anthony Vargas Sepulveda 20132020115
David Felipe Pena Huertas 20132020018

12/09/2018
"""
#Generar de librerias
import numpy as np
#Declaracion Bases nitrogenadas
bases = "ACGT"
#Longitud de secuencia general y especifica
lensecuencia=500
lenprueba=30
#Generacion de secuencia general y especifica
indices= np.random.randint(0,3,lensecuencia)
matPuntajes=np.zeros((((lensecuencia+lenprueba)-1),lensecuencia))
#Secuencia de 500 bases
secuencia = [bases[x] for x in indices]
#secuencia=['A','A','C','G','G','A','A','A','G','A'] #Ejemplo especifico
indicesPrueba=np.random.randint(0,3,lenprueba)
prueba=[bases[x] for x in indicesPrueba]
#prueba=['A','G','A','G'] #Ejemplo especifico
rPrueba=prueba[::-1]
columna=0
for base in secuencia:
    #fila=columna;
    for fila in range(len(rPrueba)):
        #print(fila)
        pr=rPrueba[fila]
        if pr==base:
            matPuntajes[fila+columna,columna]=1
    columna+=1

#Suma horizontal de resultados
results=np.sum(matPuntajes,axis=1)
matPuntajes=np.hstack((matPuntajes,results.reshape(len(results),1)))
#Numero maximo de coincidencias
maximo=np.amax(results)
#Posicion del maximo de coincidencias
inx=  np.where(results==maximo)
#Indices con los maximos
indicesMaximos=inx[0]-(lenprueba-1)
#Posicion primera coincidencia
posFinal=indicesMaximos[0]
#Impresion de resultados
print("Resultado:")
print("(posicion,Maximo de coincidencias)")
print(posFinal,maximo)