# Importación de módulos

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

'''
Función que muestra por consola el contenido de la matriz MODELVIEW o la matriz PROJECTION.
El primer parámetro (tipo) permite seleccionar la matriz ('m': MODELVIEW, 'p': PROJECTION).
El segundo parámetro es el texto que aparecerá antes de la matriz.
'''

def print_matrix(tipo, mensaje):
    
    '''
    Muestra por consola el contenido de la matriz MODELVIEW o la matriz PROJECTION.
    
    Args:
        tipo: permite seleccionar la matriz ('m': MODELVIEW, 'p': PROJECTION).
        mensaje: texto que aparecerá antes de la matriz
    
    Returs:
        None
    
    
    '''

    print(mensaje)
    if tipo == 'm':
        m = glGetFloatv(GL_MODELVIEW_MATRIX)
    elif tipo == 'p':
        m = glGetFloatv(GL_PROJECTION_MATRIX)
    else:
        return

    for columna in range(4):
        for fila in range(4):
            print(round(m[fila][columna],2), end="\t")
        print("\n")



def cube():
    
    '''
    Dibuja un cubo centrado en el origen y de lado 1.

    El nombre de las caras (frontal, posterior, etc) corresponden a 
    un punto de vista situado en el eje Z positivo, mirando hacia el eje Z negativo.
    '''
    
    he = 0.5   # semilado del cubo (half-edge)
    
    v1 = [-he, -he, he]
    v2 = [-he, he, he]
    v3 = [he, -he, he]
    v4 = [he, he, he]
    v5 = [he, -he, -he]
    v6 = [he, he,-he]
    v7 = [-he, he, -he]
    v8 = [-he, -he, -he]
    
    
    # CARA POSTERIOR: NARANJA
    glColor3f(255/255, 153/255, 0/255)
    glBegin(GL_POLYGON);
    glVertex3fv(v8) 
    glVertex3fv(v7)   
    glVertex3fv(v6)   
    glVertex3fv(v5)   
    glEnd()

    # CARA FRONTAL: ROSA
    glColor3f(255/255, 102/255, 204/255)
    glBegin(GL_POLYGON)
    glVertex3fv(v1)   
    glVertex3fv(v3)   
    glVertex3fv(v4)   
    glVertex3fv(v2)   
    glEnd()

    # CARA DERECHA: GRIS
    glColor3f(204/255, 204/255, 204/255)
    glBegin(GL_POLYGON)
    glVertex3fv(v3)
    glVertex3fv(v5)
    glVertex3fv(v6)
    glVertex3fv(v4)
    glEnd()
    
    # CARA IZQUIERDA: VERDE
    glColor3f(153/255, 204/255, 0/255)
    glBegin(GL_POLYGON)
    glVertex3fv(v1)
    glVertex3fv(v2)
    glVertex3fv(v7)
    glVertex3fv(v8)
    glEnd()
    
    # CARA INFERIOR: ROJO
    glColor3f(204/255, 0/255, 0/255)
    glBegin(GL_POLYGON)
    glVertex3fv(v1)
    glVertex3fv(v3)
    glVertex3fv(v5)
    glVertex3fv(v8)
    glEnd()

    # CARA SUPERIOR: AZUL
    glColor3f(153/255, 204/255, 255/255)
    glBegin(GL_POLYGON)
    glVertex3fv(v2)
    glVertex3fv(v4)
    glVertex3fv(v6)
    glVertex3fv(v7)
    glEnd()    
    
    

def color_cube(colorv):
    
    '''
    Dibuja un cubo centrado en el origen y de lado 1 con todas las caras del mismo
    
    Args:
        colorv: color del cubo en forma de lista de tres componentes R, G, B

    '''
    
    he = 0.5   # semilado del cubo (half-edge)
    
    v1 = [-he, -he, he]
    v2 = [-he, he, he]
    v3 = [he, -he, he]
    v4 = [he, he, he]
    v5 = [he, -he, -he]
    v6 = [he, he,-he]
    v7 = [-he, he, -he]
    v8 = [-he, -he, -he]
    
    
    glColor3fv(colorv)

    # CARA POSTERIOR
    glBegin(GL_POLYGON);
    glVertex3fv(v8) 
    glVertex3fv(v7)   
    glVertex3fv(v6)   
    glVertex3fv(v5)   
    glEnd()


    # CARA FRONTAL
    glBegin(GL_POLYGON)
    glVertex3fv(v1)   
    glVertex3fv(v3)   
    glVertex3fv(v4)   
    glVertex3fv(v2)   
    glEnd()

    # CARA DERECHA
    glBegin(GL_POLYGON)
    glVertex3fv(v3)
    glVertex3fv(v5)
    glVertex3fv(v6)
    glVertex3fv(v4)
    glEnd()
    
    # CARA IZQUIERDA
    glBegin(GL_POLYGON)
    glVertex3fv(v1)
    glVertex3fv(v2)
    glVertex3fv(v7)
    glVertex3fv(v8)
    glEnd()
    
    # CARA INFERIOR:
    glBegin(GL_POLYGON)
    glVertex3fv(v1)
    glVertex3fv(v3)
    glVertex3fv(v5)
    glVertex3fv(v8)
    glEnd()

    # CARA SUPERIOR
    glBegin(GL_POLYGON)
    glVertex3fv(v2)
    glVertex3fv(v4)
    glVertex3fv(v6)
    glVertex3fv(v7)
    glEnd()
    



def axes(xMin, xMax, yMin, yMax, zMin, zMax, tickmarks):
    
    '''
    Dibuja los 3 ejes de coordenadas con los siguientes colores:

        Eje X: azul oscuro el semieje positivo y azul claro el semieje negativo.

        Eje Y: verde oscuro el semieje positivo y verde claro el semieje negativo.

        Eje Z: rojo oscuro el semieje positivo y rojo claro el semieje negativo.
        
        
    Args:
        xMin: valor mínimo del eje X
        xMax: valor máximo del eje X
        yMin: valor mínimo del eje Y
        yMax: valor máximo del eje Y
        zMin: valor mínimo del eje Z
        zMax: valor máximo del eje Z
        tickmarks: si True, se dibujan marcas en los ejes en las posiciones enteras (1, 2, 3, etc).
    
    
    Returns:
        None

    '''    

    glLineWidth(2)
    glBegin(GL_LINES)
    # eje X POSITIVO azul
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(xMax, 0.0, 0.0)
    # eje X NEGATIVO azul
    glColor3f(0.8,  0.8, 1.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(xMin, 0.0, 0.0)
    # eje Y POSITIVO verde
    glColor3f(0.0, 1.0,  0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, yMax, 0.0)
    # eje Y NEGATIVO verde
    glColor3f(0.8, 1.0,  0.8)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, yMin, 0.0)
    # eje Z POSITIVO rojo
    glColor3f(1.0,  0.0,  0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, zMax)
    # eje Z NEGATIVO rojo
    glColor3f(1.0,  0.8,  0.8)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, zMin)
    glEnd()
    
    
    if tickmarks:
        glPointSize(5.0)
        glBegin(GL_POINTS)
        # eje X
        glColor3f(0.8, 0.8, 1.0)
        for x in range(xMin,0,1):            
            glVertex3f(x, 0.0, 0.0)
        glColor3f(0.0, 0.0, 1.0)  
        for x in range(0,xMax,1):            
            glVertex3f(x, 0.0, 0.0)
        #eje Y
        glColor3f(0.8, 1.0,  0.8)
        for y in range(yMin,0,1):
            glVertex3f(0.0, y, 0.0)   
        glColor3f(0.0, 1.0,  0.0)
        for y in range(0,yMax,1):
            glVertex3f(0.0, y, 0.0) 
        #eje Z
        glColor3f(1.0, 0.8,  0.)
        for z in range(zMin,0,1):
            glVertex3f(0.0, 0.0, z)
        glColor3f(1.0, 0.0,  0.0)
        for z in range(0,zMax,1):
            glVertex3f(0.0, 0.0, z)
        glEnd()

  

def draw_text(text, x, y):
    glRasterPos2f(x, y)
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(char))

def draw_text_3d(text, x, y, z):
    glRasterPos3f(x, y, z)
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(char))  