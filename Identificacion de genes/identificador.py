"""
Parcial de ciencias de los datos
Anthony Vargas Sepulveda 20132020115
David Felipe Pena Huertas 20132020018
12/09/2018
"""
#Importar librerias
import numpy as np
bases = "ACGT" #Bases nitrogenadas
lensecuencia=500
lenprueba=30

secuenciaGeneral= np.random.randint(0,3,lensecuencia)
matPuntajes=np.zeros((((lensecuencia+lenprueba)-1),lensecuencia))
secuenciaEspecifica = [bases[x] for x in secuenciaGeneral]
secuenciaGeneralPrueba=np.random.randint(0,3,lenprueba)
prueba=[bases[x] for x in secuenciaGeneralPrueba]
rPrueba=prueba[::-1]
columna=0
for base in secuenciaEspecifica:
    #fila=columna;
    for fila in range(len(rPrueba)):    
        #print(fila)
        if rPrueba[fila]==base:
            matPuntajes[fila+columna,columna]=1
    columna+=1
#Suma horizontal de resultados
results=np.sum(matPuntajes,axis=1)
matPuntajes=np.hstack((matPuntajes,results.reshape(len(results),1)))
#Posicion del maximo de coincidencias
inx=  np.where(results==np.amax(results))
# con los maximos
Maximos=inx[0]-(lenprueba-1)
#Posicion primera coincidencia
posFinal=Maximos[0]
#Impresion de resultados
print("Resultado:")
print("(posicion,Maximo de coincidencias)")
print(posFinal,np.amax(results))