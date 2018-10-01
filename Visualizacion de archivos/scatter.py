import csv
import matplotlib.pyplot as plt
import numpy as np
with open('Visualizacion de archivos/saber11.csv','rb') as archivocsv:
    for line in archivocsv.readlines():
        array=line.split(',')
        primerItem=array[0]
    numeroColumnas=len(array)
    archivocsv.seek(0)
    lector=csv.reader(archivocsv,delimiter=',')
    next(lector)
    edad=[]
    puntajeIngles=[]
    puntajeSociales=[]
    puntajeNaturales=[]
    puntajeMatematicas=[]
    puntajeLectura=[]
    puntajeGlobal=[]
    for row in lector:
        edad.append(list(row[i] for i in [3]))
        puntajeGlobal.append(list(row[i] for i in [80]))
        puntajeIngles.append(list(row[i] for i in [77]))
        puntajeSociales.append(list(row[i] for i in [74]))
        puntajeNaturales.append(list(row[i] for i in [71]))
        puntajeMatematicas.append(list(row[i] for i in [68]))
        puntajeLectura.append(list(row[i] for i in [65]))

    fig1= plt.figure() 
    fig1.suptitle("Puntajes por areas")
    ax11=fig1.add_subplot(221)
    ax11.title.set_text("Ingles")
    ax11.set_ylabel("Puntaje")
    ax11.set_xlabel("Edad")
    ax11=plt.scatter(edad,puntajeIngles,s=5,c=puntajeIngles,marker='*',cmap='hot',alpha=0.5)
    ax12=fig1.add_subplot(222)
    ax12.title.set_text("Sociales")
    ax12.set_ylabel("Puntaje")
    ax12.set_xlabel("Edad")
    ax12=plt.scatter(edad,puntajeSociales,s=5,c=puntajeSociales,marker='h',cmap='hot',alpha=0.5)
    ax13=fig1.add_subplot(223)
    ax13.title.set_text("Ciencias Naturales")
    ax13.set_ylabel("Puntaje")
    ax13.set_xlabel("Edad")
    ax13=plt.scatter(edad,puntajeNaturales,s=5,c=puntajeNaturales,marker='H',cmap='hot',alpha=0.5)
    ax14=fig1.add_subplot(224)
    ax14.title.set_text("Matematicas")
    ax14.set_ylabel("Puntaje")
    ax14.set_xlabel("Edad")
    ax14=plt.scatter(edad,puntajeMatematicas,s=5,c=puntajeMatematicas,marker='x',cmap='hot',alpha=0.5)

    fig2=plt.figure()
    fig2.suptitle("Puntaje Global")
    fig2=plt.scatter(edad,puntajeGlobal,s=20,c=puntajeGlobal,marker='x')

    fig3=plt.figure()
    fig3.suptitle("Relacion de Areas")
    ax31=fig3.add_subplot(221)
    ax31.title.set_text("Correlacion Ingles - Lectura")
    ax31.set_ylabel("Ingles")
    ax31.set_xlabel("Lectura")
    ax31=plt.scatter(puntajeLectura,puntajeIngles,s=5,c=puntajeGlobal,marker='*',cmap='winter',alpha=0.5)
    ax32=fig3.add_subplot(222)
    ax32.title.set_text("Correlacion Matematicas - Naturales")
    ax32.set_ylabel("Matematicas")
    ax32.set_xlabel("Naturales")
    ax32=plt.scatter(puntajeNaturales,puntajeMatematicas,s=5,c=puntajeGlobal,marker='.',cmap='winter',alpha=0.5)
    ax33=fig3.add_subplot(223)
    ax33.title.set_text("Correlacion Sociales - Naturales")
    ax33.set_ylabel("Sociales")
    ax33.set_xlabel("Naturales")
    ax33=plt.scatter(puntajeNaturales,puntajeSociales,s=5,c=puntajeGlobal,marker='.',cmap='winter',alpha=0.5)
    ax34=fig3.add_subplot(224)
    ax34.title.set_text("Correlacion Matematicas - Ingles")
    ax34.set_ylabel("Matematica")
    ax34.set_xlabel("Ingles")
    ax34=plt.scatter(puntajeIngles,puntajeMatematicas,s=5,c=puntajeGlobal,marker='.',cmap='winter',alpha=0.5)
    
    plt.show()