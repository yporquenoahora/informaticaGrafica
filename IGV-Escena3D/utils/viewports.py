from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from math import sqrt
from math import cos
from math import sin
from math import tan
from math import pi

import utils.igv_utils as igv_utils

viewports_list = []
MARGIN_VIEWPORT = 10       #Margen para separar los viewports entre sí y de los bordes de la ventana

def config_viewports(width, height, num_viewports=1, rows=1):
    """ 
    # Distribucion de viewports
        - Si el número de viewports es entre 2 y 8, se distribuyen en filas (rows) y columnas (num_viewports//rows)
        La posición va de 1 hasta 8, y se asigna a cada viewport una posición en la ventana según el orden de la posición (de izquierda a derecha y de arriba a abajo)
        - Si el número de viewports es 1 o mayor que 8, se asigna un único viewport que ocupa toda la ventana.
        Ejemplo con 8 viewports y 2 filas:
        | 1 | 2 | 3 | 4 |
        | 5 | 6 | 7 | 8 |
    """
    
    viewports_list.clear()

    if num_viewports <= 1:
        size = min(width, height) - 2 * MARGIN_VIEWPORT
        x = (width - size) // 2
        y = (height - size) // 2
        viewports_list.append([x, y, size, size])
        return

    cols = num_viewports // rows

    vp_width = width // cols
    vp_height = height // rows

    for r in range(rows):
        for c in range(cols):
            x = c * vp_width
            y = height - (r + 1) * vp_height

            size = min(vp_width, vp_height) - 2 * MARGIN_VIEWPORT

            # centrar viewport cuadrado dentro de su celda
            x_offset = x + (vp_width - size) // 2
            y_offset = y + (vp_height - size) // 2

            viewports_list.append([x_offset, y_offset, size, size])

    #print(viewports_list)


def set_viewport(index):    
    if index-1 < len(viewports_list):
        x_lower, y_lower, width, height = viewports_list[index-1]
        glViewport(x_lower, y_lower, width, height)                # glViewport(x_lower_left_corner, y_lower_left_corner, width, height)
    else:
        print("Índice de viewport no válido")


def viewport_cabinet(xMin, xMax, yMin, yMax, dNear, dFar):
 
    ###############################################################
    # PREPARACIÓN DE LA PROYECCIÓN - SE ESTUDIARÁ POSTERIORMENTE
    ###############################################################
    
    # PREPARACIÓN DE LA MATRIZ DE CONVERSIÓN GABINETE
    factor = pi/180                 # Factor de conversión de grados a radianes
    alpha = 63.4                    # Definición del ángulo alfa
    alpha = alpha * factor          # Conversión a radianes
    phi = 30                        # Definición del ángulo phi 
    phi = phi * factor              # Conversión a radianes
    cx = cos(phi)/tan(alpha)
    cy = sin(phi)/tan(alpha)
    cabinet_matrix = [1, 0, 0, 0, 0, 1, 0, 0, cx, cy, 1, 0, 0, 0, 0, 1]
    
    # DEFINICIÓN DE LA MATRIZ DE PROYECCIÓN (tipo de proyección) 
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glMultMatrixf(cabinet_matrix)   # definición de la proyección (tipo gabinete)
    
    ###############################################################
    
    # Definición del volumen de recorte
    glOrtho(xMin, xMax, yMin, yMax, dNear, dFar) 

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    # Definición de la posición de la cámara (punto de vista)
    # valor por defecto de lookAt (punto de vista hacia Zworld-)
    x0 = 0.0;  y0 = 0.0;  z0 = 0.0;  xref = 0.0;  yref = 0.0;  zref = -1.0;  vx = 0.0;  vy = 1.0; vz = 0.0
    gluLookAt(x0, y0, z0, xref, yref, zref, vx, vy, vz)   # Se podría eliminar porque se usa el valor por defecto
    
    
    igv_utils.axes(xMin, xMax, yMin, yMax, dNear, dFar, False)
    
    #igv_utils.draw_text_3d("GABINETE", 0.0, -1.0, 0.0)


def viewport_ortho_front(xMin, xMax, yMin, yMax, dNear, dFar):
    
    # Definición del viewport
    #glViewport(650, 500, 500, 500)   # glViewport(x_lower_left_corner, y_lower_left_corner, width, height)
    
    # Preparación de la proyección ortogonal
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    
    glOrtho(xMin, xMax, yMin, yMax, dNear, dFar) 

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    # Definición de la posición de la cámara (punto de vista). Valor por defecto de lookAt (punto de vista hacia Zworld-)
    x0 = 0.0;  y0 = 0.0;  z0 = 0.0;  xref = 0.0;  yref = 0.0;  zref = -1.0;  vx = 0.0;  vy = 1.0; vz = 0.0
    gluLookAt(x0, y0, z0, xref, yref, zref, vx, vy, vz)   # Se podría eliminar porque se usa el valor por defecto
    
    # Dibujo de los ejes y la casa
    igv_utils.axes(xMin, xMax, yMin, yMax, dNear, dFar, False)
        
    # Dibujo de una etiqueta  
    #igv_utils.draw_text_3d("VISTA FRONTAL", -1.0, -1.0, 0.0)

def viewport_ortho_rear(xMin, xMax, yMin, yMax, dNear, dFar):
    
    # Definición del viewport
    #glViewport(300,0,300,300)   # glViewport(x_lower_left_corner, y_lower_left_corner, width, height)
    
    # Preparación de la proyección ortogonal
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    
    glOrtho(xMin, xMax, yMin, yMax, dNear, dFar) 

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    # Definición de la posición de la cámara (punto de vista). Punto de vista hacia Zworld+
    x0 = 0.0;  y0 = 0.0;  z0 = 0.0;  xref = 0.0;  yref = 0.0;  zref = 1.0;  vx = 0.0;  vy = 1.0; vz = 0.0
    gluLookAt(x0, y0, z0, xref, yref, zref, vx, vy, vz)
    
    # Dibujo de los ejes y la casa
    igv_utils.axes(xMin, xMax, yMin, yMax, dNear, dFar, False)
   
    # Dibujo de una etiqueta
    #igv_utils.draw_text_3d("VISTA POSTERIOR", 1.0, -1.0, 0.0)

def viewport_ortho_right(xMin, xMax, yMin, yMax, dNear, dFar):
    
    # Definición del viewport
    #glViewport(600,300,300,300)   # glViewport(x_lower_left_corner, y_lower_left_corner, width, height)
    
    # Preparación de la proyección ortogonal
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    
    glOrtho(xMin, xMax, yMin, yMax, dNear, dFar) 
  
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    # Definición de la posición de la cámara (punto de vista). Punto de vista hacia Xworld-
    x0 = 0.0;  y0 = 0.0;  z0 =0.0;  xref = -1;  yref = 0.0;  zref = 0.0;  vx = 0.0;  vy = 1.0; vz = 0.0
    gluLookAt(x0, y0, z0, xref, yref, zref, vx, vy, vz)
    
    # Dibujo de los ejes y la casa
    igv_utils.axes(xMin, xMax, yMin, yMax, dNear, dFar, False)
    
    # Dibujo de una etiqueta
    #igv_utils.draw_text_3d("VISTA LATERAL DERECHO", 0.0, -1.0, 2.0)

def viewport_ortho_left(xMin, xMax, yMin, yMax, dNear, dFar):
    
    # Preparación de la proyección ortogonal
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    
    glOrtho(xMin, xMax, yMin, yMax, dNear, dFar) 

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    # Definición de la posición de la cámara (punto de vista). Punto de vista hacia Xworld+
    x0 = 0.0;  y0 = 0.0;  z0 =0.0;  xref = 1;  yref = 0.0;  zref = 0.0;  vx = 0.0;  vy = 1.0; vz = 0.0
    gluLookAt(x0, y0, z0, xref, yref, zref, vx, vy, vz)
    
    # Dibujo de los ejes y la casa
    igv_utils.axes(xMin, xMax, yMin, yMax, dNear, dFar, False)
    
    # Dibujo de una etiqueta
    #igv_utils.draw_text_3d("VISTA LATERAL IZQUIERDO", 0.0, -1.0, -2.0)

def viewport_ortho_top(xMin, xMax, yMin, yMax, dNear, dFar):
    
    # Definición del viewport    # Preparación de la proyección ortogonal
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    
    glOrtho(xMin, xMax, yMin, yMax, dNear, dFar) 

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    # Definición de la posición de la cámara (punto de vista). Punto de vista hacia Yworld-
    x0 = 0.0;  y0 = 0.0;  z0 =0.0;  xref = 0.0;  yref = -1.0;  zref = 0.0;  vx = 0.0;  vy = 0.0; vz = 1
    gluLookAt(x0, y0, z0, xref, yref, zref, vx, vy, vz)
    
    # Dibujo de los ejes y la casa
    igv_utils.axes(xMin, xMax, yMin, yMax, dNear, dFar, False)
    
    
    # Dibujo de una etiqueta
    #glColor3fv([1,0,0])
    #igv_utils.draw_text_3d("VISTA PLANTA", 1.0, 0.0, 1.0)
