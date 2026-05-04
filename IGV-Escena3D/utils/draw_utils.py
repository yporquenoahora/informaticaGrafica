#!/usr/bin/env python
# coding: utf-8

# # Diseño de funciones de apoyo para la actividad grupal

# In[1]:


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import utils.igv_utils as igv_utils    # Módulo con funciones definidas para la asignatura

from random import randint
from random import choice

from math import sqrt
from math import cos
from math import sin
from math import tan
from math import pi


# In[2]:





# #### Definición de familias/paletas de colores

# In[3]:


# Definición de colores
grey = [128/255, 128/255, 128/255]
blue = [0, 204/255, 1]

yellow_1 = [254/255, 249/255, 231/255]
yellow_2 = [252/255, 243/255, 207/255]
yellow_3 = [247/255, 220/255, 111/255]
yellow_4 = [241/255, 196/255, 15/255]
yellow_5 = [183/255, 149/255, 11/255]

yellow_range = [yellow_1, yellow_2, yellow_3, yellow_4, yellow_5]
light_yellow_range = [yellow_1, yellow_2, yellow_3]
dark_yellow_range = [yellow_3, yellow_4, yellow_5]

brown_1 = [250/255, 229/255, 211/255]
brown_2 = [240/255, 178/255, 122/255]
brown_3 = [230/255, 126/255, 34/255]
brown_4 = [175/255, 96/255, 26/255]
brown_5 = [120/255, 66/255, 18/255]

brown_range = [brown_1, brown_2, brown_3, brown_4, brown_5]
light_brown_range = [brown_1, brown_2, brown_3]
dark_brown_range = [brown_3, brown_4, brown_5]

blue_1 = [214/255, 234/255, 248/255]
blue_2 = [133/255, 193/255, 233/255]
blue_3 = [52/255, 152/255, 219/255]
blue_4 = [40/255, 116/255, 166/255]
blue_5 = [27/255, 79/255, 114/255]

blue_range = [blue_1, blue_2, blue_3, blue_4, blue_5]
light_blue_range = [blue_1, blue_2, blue_3]
dark_blue_range = [blue_3, blue_4, blue_5]

green_1 = [213/255, 245/255, 227/255]
green_2 = [130/255, 224/255, 170/255]
green_3 = [46/255, 204/255, 113/255]
green_4 = [35/255, 155/255, 86/255]
green_5 = [24/255, 106/255, 59/255]

green_range  = [green_1, green_2, green_3, green_4, green_5]
light_green_range  = [green_1, green_2, green_3]
dark_green_range  = [green_3, green_4, green_5]

red_1 = [250/255, 219/255, 216/255]
red_2 = [241/255, 148/255, 138/255]
red_3 = [231/255, 76/255, 60/255]
red_4 = [176/255, 58/255, 46/255]
red_5 = [120/255, 40/255, 31/255]

red_range = [red_1, red_2, red_3, red_4, red_5]
light_red_range = [red_1, red_2, red_3]
dark_red_range = [red_3, red_4, red_5]


grey_1 = [242/255, 243/255, 244/255]
grey_2 = [215/255, 219/255, 221/255] 
grey_3 = [189/255, 195/255, 199/255] 
grey_4 = [144/255, 148/255, 151/255] 
grey_5 = [98/255, 101/255, 103/255] 


grey_range = [grey_1, grey_2, grey_3, grey_4, grey_5]
light_grey_range = [grey_1, grey_2, grey_3]
dark_grey_range = [grey_3, grey_4, grey_5]
dark_grey_range2 = [grey_4, grey_5]

black_5 = [27/255, 38/255, 49/255] 




# #### `solid_face_xz(x_size, z_size, colors)`
# 
# 
# Función que dibuja una cara sólida en el plano XZ con las siguientes características:
# 
# -  **elemento básico**: cubo de lado uno
# -  **esquina posterior izquierda**: cubo centrado en 0,0,0 (si la matriz MODELVIEW es la identidad)
# -  **largo en X**: parámetro x_size. >= 2
# -  **largo en Z**: parámetro z_size. >= 2
# -  **grosor (eje Y)**: 1 cubo
# -  **colores**: parámetro colors. Array de colores, si tiene sólo un elemento, la cara se dibuja en ese color y si tiene varios, se dibuja mezclándolos aleatoriamente.
# 
#

# In[5]:


def solid_face_xz(x_size, z_size, colors):
    
    # Comprobar x_size, z_size
    if (x_size < 2) or (z_size < 2):
        print("Error en los parámetros de solid_face_xz")
        return
    
    # Preservar la matriz MODELVIEW
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    
    for x in range(x_size):
        for z in range(z_size):
            color = choice(colors)       # Generar el color 
            igv_utils.color_cube(color)  # Dibujar el cubo
            glTranslatef(0, 0, 1)        # Desplazamiento en Z
        glTranslatef(1, 0, -z_size)      # Retorno al eje X
        
     
    # Restaurar la matriz MODELVIEW
    glPopMatrix()
    

# #### `solid_face_yz(y_size, z_size, colors)`
# 
# 
# Función que dibuja una cara sólida en el plano YZ.
# 
# -  Se construye a partir de `solid_face_xz` girando 90 grados sobre el eje Z.
# -  Para obtener la cara en YZ con los tamaños y_size, z_size la llamada es: solid_fase_xz(y_size, z_size, colors)
# 
# ![image-6.png](attachment:image-6.png)
# 

# In[6]:


def solid_face_yz(y_size, z_size, colors):
    
    # Comprobar y_size, z_size
    if (y_size < 2) or (z_size < 2):
        print("Error en los parámetros de solid_face_yz")
        return
    
    # Preservar la matriz MODELVIEW
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    
    # Preparación de la rotación
    glRotatef(90, 0, 0, 1)

    solid_face_xz(y_size, z_size, colors)
        
    # Restaurar la matriz MODELVIEW
    glPopMatrix()


# #### `solid_face_xy(x_size, y_size, colors)`
# 
# 
# Función que dibuja una cara sólida en el plano XY.
# 
# -  Se construye a partir de `solid_face_xz` girando -90 grados sobre el eje X.
# -  Para obtener la cara en XY con los tamaños x_size, y_size la llamada es: solid_fase_xz(x_size, y_size, colors)
# 
#
# 

# In[7]:


def solid_face_xy(x_size, y_size, colors):
    
    # Comprobar x_size, y_size
    if (x_size < 2) or (y_size < 2):
        print("Error en los parámetros de solid_face_xy")
        return
    
    # Preservar la matriz MODELVIEW
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    
    # Preparación de la rotación
    glRotatef(-90, 1, 0, 0)

    solid_face_xz(x_size, y_size, colors)

    # Restaurar la matriz MODELVIEW    
    glPopMatrix()


# #### `empty_ortho(x_size, y_size, z_size, colors)`
# 
# 
# Función que dibuja un ortoedro hueco con las siguientes características:
# 
# -  **elemento básico**: cubo de lado uno
# -  **esquina posterior izquierda**: cubo centrado en 0,0,0 (si la matriz MODELVIEW es la identidad)
# -  **largo en X**: parámetro x_size. >= 4
# -  **largo en Y**: parámetro y_size. >= 4
# -  **largo en Z**: parámetro z_size. >= 4
# -  **colores**: parámetro colors. Array de colores, si tiene sólo un elemento, el ortoedro se dibuja en ese color y si tiene varios, se dibuja mezclándolos aleatoriamente.
# 
# 
# El la imagen se muestra los pasos de la construcción. Se dibuja cada cara de un color para visualizar la construcción.
# 
# 
# ![image-2.png](attachment:image-2.png)
# 

# In[8]:


def empty_ortho(x_size, y_size, z_size, colors):
    
    # Comprobar x_size, y_size, z_size
    if (x_size < 4) or (y_size < 4) or (z_size < 4):
        print("Error en los parámetros de empty_ortho")
        return
    
    # Preservar la matriz MODELVIEW
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()  
    
    # cara inferior
    solid_face_xz(x_size, z_size, colors)
   
    # cara lateral izquierda
    glTranslate(0, 1, 0)
    solid_face_yz(y_size-2, z_size, colors)
    
    # cara lateral derecha
    glTranslate(x_size-1, 0, 0)
    solid_face_yz(y_size-2, z_size, colors)    
    
    # cara posterior
    glTranslate(-(x_size-2), 0, 0)
    solid_face_xy(x_size-2, y_size-2, colors)     
    
    # cara frontal
    glTranslate(0, 0, z_size-1)
    solid_face_xy(x_size-2, y_size-2, colors)
    
    # cara superior
    glTranslate(-1, y_size-2, -(z_size-1))
    solid_face_xz(x_size, z_size, colors) 
    
    # Restaurar la matriz MODELVIEW
    glPopMatrix()
    


# #### `solid_ortho(x_size, y_size, z_size, colors)`
# 
# 
# Función que dibuja un ortoedro sólido con las siguientes características:
# 
# -  **elemento básico**: cubo de lado uno
# -  **esquina posterior izquierda**: cubo centrado en 0,0,0 (si la matriz MODELVIEW es la identidad)
# -  **largo en X**: parámetro x_size. >= 1
# -  **largo en Y**: parámetro y_size. >= 1
# -  **largo en Z**: parámetro z_size. >= 1
# -  **colores**: parámetro colors. Array de colores, si tiene sólo un elemento, el ortoedro se dibuja en ese color y si tiene varios, se dibuja mezclándolos aleatoriamente.

# In[9]:


def solid_ortho(x_size, y_size, z_size, colors):
    
    # Comprobar x_size, y_sixe, z_size, density
    if (x_size < 1) or (y_size < 1) or (z_size < 1):
        print("Error en los parámetros de solid_ortho")
        return
    
    # Preservar la matriz MODELVIEW
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    
    for y in range(y_size):    
        for x in range(x_size):
            for z in range(z_size):
                color = choice(colors) # Generar el color 
                igv_utils.color_cube(color)
                glTranslatef(0, 0, 1)
            glTranslatef(1, 0, -z_size)
        glTranslate(-x_size, 1, 0)
        
    # Restaurar la matriz MODELVIEW
    glPopMatrix()


# #### `density_face_xz(x_size, z_size, density, colors)`
# 
# 
# Función que dibuja una cara con una densidad determinada en el plano XZ con las siguientes características:
# 
# -  **elemento básico**: cubo de lado uno
# -  **esquina posterior izquierda**: cubo centrado en 0,0,0 (si la matriz MODELVIEW es la identidad)
# -  **largo en X**: parámetro x_size >= 2
# -  **largo en Z**: parámetro z_size >= 2
# -  **grosor (eje Y)**: 1 cubo
# -  **densidad**: parámetro density. IMPORTANTE, se espera un valor entero.
# -  **colores**: parámetro colors. Array de colores, si tiene sólo un elemento, la cara se dibuja en ese color y si tiene varios, se dibuja mezclándolos aleatoriamente.
# 
# ![image-3.png](attachment:image-3.png)
# 

# In[10]:


def density_face_xz(x_size, z_size, density, colors):
    
    # Comprobar x_size, z_size, density
    if (x_size < 2) or (z_size < 2) or (density < 0):
        print("Error en los parámetros de density_face_xz")
        return
    
    # Preservar la matriz MODELVIEW
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
        
        
    # Cálculo de los puntos necesarios según la densidad
    max_cubes = x_size * z_size
    #print(f"posibles cubos = {x_size} x {z_size} = {max_cubes}")
    
    num_cubes = int((max_cubes * density) / 100)
    #print(f"{density}% de {max_cubes} = {num_cubes}")
    
    n = 0   # Contador para sumar el número de cubos 
        
    for x in range(x_size):
        for z in range(z_size):
            if randint(0,100) < density:   # se pinta el cubo
                color = choice(colors) # Generar el color
                igv_utils.color_cube(color)
                n += 1
            glTranslatef(0, 0, 1)
        glTranslatef(1, 0, -z_size)
    
    #print(f"Se han pintado {n} cubos")
     
    # Restaurar la matriz MODELVIEW    
    glPopMatrix()


# #### `density_ortho(x_size, y_size, z_size, density, colors)`
# 
# 
# Función que dibuja un ortoedro con una densidad determinada con las siguientes características:
# 
# -  **elemento básico**: cubo de lado uno
# -  **esquina posterior izquierda**: cubo centrado en 0,0,0 (si la matriz MODELVIEW es la identidad)
# -  **largo en X**: parámetro x_size >= 2
# -  **largo en Y**: parámetro y_size >= 2
# -  **largo en Z**: parámetro z_size >= 2
# -  **densidad**: parámetro density. IMPORTANTE, se espera un valor entero
# -  **colores**: parámetro colors. Array de colores, si tiene sólo un elemento, el ortoedro se dibuja en ese color y si tiene varios, se dibuja mezclándolos aleatoriamente.
# 
# 

# In[11]:


def density_ortho(x_size, y_size, z_size, density, colors):
    
    # Comprobar x_size, y_sixe, z_size, density
    if (x_size < 2) or (y_size < 2) or (z_size < 2) or (density < 0):
        print("Error en los parámetros de density_ortho")
        return
    
    # Preservar la matriz MODELVIEW
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
        
        
    # Cálculo de los puntos necesarios según la densidad
    max_cubes = x_size * y_size * z_size
    #print(f"posibles cubos = {x_size} x {y_size} x {z_size} = {max_cubes}")
    
    num_cubes = int((max_cubes * density) / 100)
    #print(f"{density}% de {max_cubes} = {num_cubes}")
    
    n = 0   # Contador para sumar el número de cubos
        
    for y in range(y_size):    
        for x in range(x_size):
            for z in range(z_size):
                if randint(0,100) < density:   # se pinta el cubo
                    color = choice(colors) # Generar el color
                    igv_utils.color_cube(color)
                    n += 1
                glTranslatef(0, 0, 1)
            glTranslatef(1, 0, -z_size)
        glTranslate(-x_size, 1, 0)
    
    #print(f"Se han pintado {n} cubos")
     
    # Restaurar la matriz MODELVIEW
    glPopMatrix()


# In[12]:


def density_ortho(x_size, y_size, z_size, density, colors):
    
    # Comprobar x_size, y_sixe, z_size, density
    if (x_size < 2) or (y_size < 2) or (z_size < 2) or (density < 0):
        print("Error en los parámetros de density_ortho")
        return
    
    # Preservar la matriz MODELVIEW
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
               
    for y in range(y_size):    
        for x in range(x_size):
            for z in range(z_size):
                if randint(0,100) < density:   # se pinta el cubo
                    color = choice(colors) # Generar el color
                    igv_utils.color_cube(color)
                glTranslatef(0, 0, 1)
            glTranslatef(1, 0, -z_size)
        glTranslate(-x_size, 1, 0)
    
    glPopMatrix()


# #### `empty_face_xz(x_size, z_size, colors)`
# 
# 
# Función que dibuja una cara hueca en el plano XZ con las siguientes características:
# 
# -  **elemento básico**: cubo de lado uno
# -  **esquina posterior izquierda**: cubo centrado en 0,0,0 (si la matriz MODELVIEW es la identidad)
# -  **largo en X**: parámetro x_size. >= 3
# -  **largo en Z**: parámetro z_size. >= 3
# -  **grosor (eje Y)**: 1 cubo
# -  **colores**: parámetro colors. Array de colores, si tiene sólo un elemento, la cara se dibuja en ese color y si tiene varios, se dibuja mezclándolos aleatoriamente.
# 
# ![image-2.png](attachment:image-2.png)
# 

# In[13]:


def empty_face_xz(x_size, z_size, colors):
    
    # Comprobar x_size, z_size
    if (x_size < 3) or (z_size < 3):
        print("Error en los parámetros de empty_face_xz")
        return
    
    # Preservar la matriz MODELVIEW
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    
       
    for x in range(x_size-1):
        color = choice(colors)
        igv_utils.color_cube(color)
        glTranslatef(1, 0, 0)

            
    for z in range(z_size-1):
        color = choice(colors)
        igv_utils.color_cube(color)
        glTranslatef(0, 0, 1)            
            
    for x in range(x_size-1):
        color = choice(colors)
        igv_utils.color_cube(color)
        glTranslatef(-1, 0, 0)           
            

    for z in range(z_size):
        color = choice(colors)
        igv_utils.color_cube(color)
        glTranslatef(0, 0, -1)   
    
    # Restaurar la matriz MODELVIEW
    glPopMatrix()


# #### `empty_pipe_y(x_size, y_size, z_size, colors)`
# 
# 
# Función que dibuja un "tubo" hueco en el eje Y con las siguientes características:
# 
# -  **elemento básico**: cubo de lado uno
# -  **esquina posterior izquierda**: cubo centrado en 0,0,0
# -  **largo en X**: parámetro x_size. >= 3
# -  **largo en Y**: parámetro y_size. >= 3
# -  **largo en Z**: parámetro z_size. >= 3
# -  **colores**: parámetro colors. Array de colores, si tiene sólo un elemento, el ortoedro se dibuja en ese color y si tiene varios, se dibuja mezclándolos aleatoriamente.
# 
# ![image.png](attachment:image.png)
# 

# In[14]:


def empty_pipe_y(x_size, y_size, z_size, colors):
    
    # Comprobar x_size, y_size, z_size
    if (x_size < 3) or (y_size < 3) or (z_size < 3):
        print("Error en los parámetros de empty_pipe_y")
        return
    
    # Preservar la matriz MODELVIEW
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()

    for y in range(y_size):
        empty_face_xz(x_size, z_size, colors)
        glTranslatef(0,1,0)
        
    # Restaurar la matriz MODELVIEW
    glPopMatrix()



# In[18]:


def config_projection(projection, lookAt, axes_length, draw_axes):

    # límites de los ejes de coordenadas
    #axes_length = 100
    xMin = yMin = zMin = - axes_length
    xMax = yMax = zMax = axes_length    
    
    # La proyección puede se paralela ortogonal ("ortho") o paralela oblicua de tipo gabinete ("cabinet").
    #projection = "cabinet"
    
    # El punto de vista puede ser: "default" (d), "x+", "x-", "y+", "y-", "z+"
    #lookAt = "d"
    

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Borrar buffers
    
    # Establecer dNear y dFar en función de los límites del eje Z
    dNear = -zMax;  dFar = -zMin         # El plano de proyección es z = -dNear
    
    ##############################
    # PREPARACIÓN DE LA PROYECCIÓN
    ##############################
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    
    if projection == "cabinet":  
        # PREPARACIÓN DE LA MATRIZ DE CONVERSIÓN GABINETE
        factor = pi/180                 # Factor de conversión de grados a radianes
        alpha = 63.4                    # Definición del ángulo alfa
        alpha = alpha * factor          # Conversión a radianes
        phi = 30                        # Definición del ángulo phi 
        phi = phi * factor              # Conversión a radianes
        cx = cos(phi)/tan(alpha)
        cy = sin(phi)/tan(alpha)
        cabinet_matrix = [1, 0, 0, 0, 0, 1, 0, 0, cx, cy, 1, 0, 0, 0, 0, 1] 
        glMultMatrixf(cabinet_matrix)   # definición de la proyección (tipo gabinete)
    

    # Llamada a la función que define el volumen de recorte
    # Los límites en los ejes X e Y coinciden con los límites de dibujo de los ejes X e Y
    glOrtho(xMin, xMax, yMin, yMax, dNear, dFar)

    
    ##############################
    # PREPARACIÓN DE LA CÁMARA
    ##############################  
    
    if lookAt == "x+":
        x0 = 0.0;  y0 = 0.0;  z0 = 0.0;  xref = 1.0;  yref = 0.0;  zref = 0.0;  vx = 0.0;  vy = 1.0; vz = 0.0
    elif lookAt == "x-":
        x0 = 0.0;  y0 = 0.0;  z0 = 0.0;  xref = -1.0;  yref = 0.0;  zref = 0.0;  vx = 0.0;  vy = 1.0; vz = 0.0
    elif lookAt == "z+":
        x0 = 0.0;  y0 = 0.0;  z0 = 0.0;  xref = 0.0;  yref = 0.0;  zref = 1.0;  vx = 0.0;  vy = 1.0; vz = 0.0
    elif lookAt == "y+":
        x0 = 0.0;  y0 = 0.0;  z0 = 0.0;  xref = 0.0;  yref = 1.0;  zref = 0.0;  vx = 0.0;  vy = 0.0; vz = 1.0   # z+
#         x0 = 0.0;  y0 = 0.0;  z0 = 0.0;  xref = 0.0;  yref = 1.0;  zref = 0.0;  vx = 0.0;  vy = 0.0; vz = -1.0  # z-
#         x0 = 0.0;  y0 = 0.0;  z0 = 0.0;  xref = 0.0;  yref = 1.0;  zref = 0.0;  vx = 1.0;  vy = 0.0; vz = 0.0   # x+
#         x0 = 0.0;  y0 = 0.0;  z0 = 0.0;  xref = 0.0;  yref = 1.0;  zref = 0.0;  vx = -1.0;  vy = 0.0; vz = 0.0  # x-
#         x0 = 0.0;  y0 = 0.0;  z0 = 0.0;  xref = 0.0;  yref = 1.0;  zref = 0.0;  vx = 0.0;  vy = -1; vz = 0.0  # Contradicción
#         x0 = 0.0;  y0 = 0.0;  z0 = 0.0;  xref = 0.0;  yref = 1.0;  zref = 0.0;  vx = 0.0;  vy = 1; vz = 0.0  # Contradicción
#         x0 = 0.0;  y0 = 0.0;  z0 = 0.0;  xref = 0.0;  yref = 1.0;  zref = 0.0;  vx = 1.0;  vy = 0; vz = 1.0     
    elif lookAt == "y-":
        x0 = 0.0;  y0 = 0.0;  z0 = 0.0;  xref = 1.0;  yref = -1.0;  zref = 0.0;  vx = 1.0;  vy = 0.0; vz = 0.0
    else:   # default (z-)
        x0 = 0.0;  y0 = 0.0;  z0 = 0.0;  xref = 0.0;  yref = 0.0;  zref = -1.0;  vx = 0.0;  vy = 1.0; vz = 0.0
    

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(x0, y0, z0, xref, yref, zref, vx, vy, vz)
    
    if draw_axes:
        igv_utils.axes(xMin, xMax, yMin, yMax, zMin, zMax, False)  # Dibujo de los ejes de coordenadas

 
    ###############################################
    # solid_face_xz con matriz MODELVIEW identidad
    ###############################################

#     solid_face_xz(30, 30, [blue_4])

    ###############################################
    # solid_face_xz trasladado al punto (0, 10, 0)
    ###############################################

#     glTranslatef(1, 10, 0)
#     solid_face_xz(30, 30, [blue_3])   

    ###############################################
    # empty_ortho
    ###############################################
#     empty_ortho(20, 20, 20, red_range)

    ###############################################
    # solid_ortho
    ###############################################
#     solid_ortho(10, 10, 10, grey_range)
    
    ###############################################
    #density_face_xz
    ###############################################
#     density_face_xz(30, 30, 25, blue_range)
    
    ###############################################
    #density_ortho
    ###############################################
#     density_ortho(30, 30, 30, 15, green_range)
    
    #empty_face_xz
    ###############################################
#     empty_face_xz(30, 30, red_range)
    ###############################################
    
    ###############################################
    #empty_pipe_y
    ###############################################
    
#     empty_pipe_y(10, 30, 10, dark_red_range)


    ###############################################
    # Dos árboles
    ###############################################
#     tree(dark_brown_range, dark_green_range)
#     glTranslatef(60,0,0)
#     tree(brown_range, dark_red_range)

    ###############################################
    # Pirámide
    ###############################################
#     pyramid(51, dark_yellow_range)

    ###############################################
    # Banco
    ###############################################

#     bench()

#    glFlush()



# ### Función principal que llama a las funciones de inicialización y de dibujo

# In[19]:

"""
def main():
    init_gl()
    glutDisplayFunc(display)
    glutMainLoop()    # Deja la ventana abierta a la espera de eventos
    


# ### Llamada a la función principal

# In[20]:


main()
"""
