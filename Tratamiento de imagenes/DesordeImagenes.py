'''
Tratamiento de imagenes 
Introduccion a la ciencia de los datos
'''

import numpy as np
from skimage import io
from random import shuffle

img=io.imread('los-simpson-400x400.jpg',True)

#obtiene 16 pedazos de la imagen de 100*100 pixeles
chunks = np.array([img[y:y+100,x:x+100] for x in [0,100,200,300] for y in [0,100,200,300]])
    
#horizontal stack
positions = np.arange(16)
np.random.shuffle(positions)
Harray = []
for col in range(0,16,4):
    #une horizontalmente 4 pedazos
    pos = positions[col:col+4]
    hor = np.hstack((chunks[pos[0]],chunks[pos[1]],chunks[pos[2]],chunks[pos[3]]))
    Harray.append(hor)
#vertical stack 
img_final = np.vstack((Harray[0],Harray[1],Harray[2],Harray[3]))    
io.imsave('final.jpg',img_final)