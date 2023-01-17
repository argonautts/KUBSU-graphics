import glfw
from OpenGL.GL import *
import numpy as np

# install library:
# pip install glfw
# pip install pyopengl
# pip install pyrr
# pip install pillow

def windowResize(window, width, height):
    glViewport(0,0, width, height)

# initializing glfw library
if not glfw.init():
    raise Exception("glfw can not be initialized!")

# creating the widnow
window = glfw.create_window(1280, 720, "Bosnia and Herzegovina", None, None)

# check if window was created
if not window:
    glfw.terminate()
    raise Exception("glfw window can not be created!")

# set window's position
glfw.set_window_pos(window, 400, 200)

glfw.set_window_size_callback(window, windowResize)

# make the context current
glfw.make_context_current(window)


def yellowTriangle():
    yellowVertices = [-0.5, 1, 0.0,
                      0.5, 1, 0.0,
                      0.5, -1, -1]

    yellowColors = [255, 255, 0,
                    255, 255, 0,
                    255, 255, 0]

    yVertices = np.array(yellowVertices, dtype=np.float32)
    yColors = np.array(yellowColors, dtype=np.float32)

    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, yVertices)

    glEnableClientState(GL_COLOR_ARRAY)
    glColorPointer(3, GL_FLOAT, 0, yColors)


def WT(Points):
    WhiteColors = [255, 255, 255,
                   255, 255, 255,
                   255, 255, 255, ]

    PWT = np.array(Points, dtype=np.float32)
    PWC = np.array(WhiteColors, dtype=np.float32)

    glVertexPointer(3, GL_FLOAT, 0, PWT)
    glColorPointer(3, GL_FLOAT, 0, PWC)


glClearColor(0, 0, 128, 1)

# the main application loop
while not glfw.window_should_close(window):
    glfw.poll_events()
    glClear(GL_COLOR_BUFFER_BIT)

    yellowTriangle()
    glDrawArrays(GL_TRIANGLES, 0, 3)
    '''                 yellow[-0.5, 1, 0.0,
                        0.5, 1, 0.0,
                        0.5, -1, -1]

                       WT([-0.85, 0.25, 0,
                        -0.80, -0.10, 0,
                        -0.70, 0.05, 0])'''
    # White Stars Center: top
    WT([-0.35, 0.25, 0,
        -0.30, -0.10, 0,
        -0.20, 0.05, 0])
    glDrawArrays(GL_TRIANGLES, 0, 3)
    # White Stars Center: right
    WT([-0.15, 0.23, 0,
        -0.23, -0.10, 0,
        -0.30, 0.07, 0])
    glDrawArrays(GL_TRIANGLES, 0, 3)
    # White Stars Center: under right
    WT([-0.12, -0.12, 0,
        -0.25, 0.10, 0,
        -0.30, -0.10, 0])
    glDrawArrays(GL_TRIANGLES, 0, 3)
    # White Stars Center: under left
    WT([-0.28, -0.33, 0,
        -0.20, 0.05, 0,
        -0.32, 0.07, 0])
    glDrawArrays(GL_TRIANGLES, 0, 3)
    # White Stars Center: left
    WT([-0.42, -0.08, 0,
        -0.25, -0.10, 0,
        -0.25, 0.10, 0])
    glDrawArrays(GL_TRIANGLES, 0, 3)

    # White Stars TOP: top |change x:-0.3 y:+0.6
    WT([-0.65, 0.85, 0,
        -0.60, 0.5, 0,
        -0.50, 0.65, 0])
    glDrawArrays(GL_TRIANGLES, 0, 3)
    # White Stars TOP: right |change x:-0.3 y:+0.6
    WT([-0.45, 0.83, 0,
        -0.53, 0.50, 0,
        -0.60, 0.67, 0])
    glDrawArrays(GL_TRIANGLES, 0, 3)
    # White Stars TOP: under right |change x:-0.3 y:+0.6
    WT([-0.42, 0.48, 0,
        -0.55, 0.70, 0,
        -0.60, 0.50, 0])
    glDrawArrays(GL_TRIANGLES, 0, 3)
    # White Stars TOP: under left |change x:-0.3 y:+0.6
    WT([-0.58, 0.27, 0,
        -0.50, 0.65, 0,
        -0.62, 0.67, 0])
    glDrawArrays(GL_TRIANGLES, 0, 3)
    # White Stars TOP: left |change x:-0.3 y:+0.6
    WT([-0.72, 0.52, 0,
        -0.55, 0.50, 0,
        -0.55, 0.70, 0])
    glDrawArrays(GL_TRIANGLES, 0, 3)

    # White Stars Middle: top |change x:+0.3 y: -0.6
    WT([-0.05, -0.35, 0,
        0, -0.70, 0,
        0.10, -0.55, 0])
    glDrawArrays(GL_TRIANGLES, 0, 3)
    # White Stars Middle: right |change x:+0.3 y: -0.6
    WT([0.15, -0.33, 0,
        0.07, -0.70, 0,
        0, -0.57, 0])
    glDrawArrays(GL_TRIANGLES, 0, 3)
    # White Stars Middle: under right |change x:+0.3 y: -0.6
    WT([0.18, -0.72, 0,
        0.05, -0.50, 0,
        0, -0.70, 0])
    glDrawArrays(GL_TRIANGLES, 0, 3)
    # White Stars Middle: under left |change x:+0.3 y: -0.6
    WT([0.02, -0.93, 0,
        0.10, -0.55, 0,
        -0.02, -0.53, 0])
    glDrawArrays(GL_TRIANGLES, 0, 3)
    # White Stars Middle: left |change x:+0.3 y: -0.6
    WT([-0.12, -0.68, 0,
        0.05, -0.70, 0,
        0.05, -0.50, 0])
    glDrawArrays(GL_TRIANGLES, 0, 3)

    glfw.swap_buffers(window)

# terminate glfw, free up allocated resources
glfw.terminate()
--------------------------------------------------------------------------
import glfw
from OpenGL.GL import *
import keyboard

if not glfw.init():
    raise Exception("Не удалось инициализировать библиотеку")

window = glfw.create_window(1000, 600, "Танк", None, None)

if not window:
    glfw.terminate()
    raise Exception("Ошибка при инициализации окна")

glfw.set_window_pos(window,400,200)
glfw.make_context_current(window)
glClearColor(1, 1, 1, 0)
glEnable(GL_DEPTH_TEST)

while not glfw.window_should_close(window):
    glfw.poll_events()
    glClear(GL_COLOR_BUFFER_BIT)
    glClear(GL_DEPTH_BUFFER_BIT )
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    if keyboard.read_key() == "d":
        glRotate(5,0,1,0)
    elif keyboard.read_key() == "a":
        glRotate(-5,0,1,0)
    elif keyboard.read_key() == "w":
        glRotate(-5,1,0,0)
    elif keyboard.read_key() == "s":
        glRotate(5,1,0,0)

    """Лежачий Пк"""
    glBegin(GL_QUADS)
    glColor4f(0, 0, 255, 1)
    # Передний квадрат
    glVertex3f(0.5, -0.55, 0.5)
    glVertex3f(0.5, -0.9, 0.5)
    glVertex3f(-0.5, -0.9, 0.5)
    glVertex3f(-0.5, -0.55, 0.5)
    # Задний квадрат
    glVertex3f(0.5, -0.55, -0.5)
    glVertex3f(0.5, -0.9, -0.5)
    glVertex3f(-0.5, -0.9, -0.5)
    glVertex3f(-0.5, -0.55, -0.5)
    # Правый квадрат
    glVertex3f(0.5, -0.55, 0.5)
    glVertex3f(0.5, -0.9, 0.5)
    glVertex3f(0.5, -0.9, -0.5)
    glVertex3f(0.5, -0.55, -0.5)
    # Левый квадрат
    glVertex3f(-0.5, -0.55, 0.5)
    glVertex3f(-0.5, -0.9, 0.5)
    glVertex3f(-0.5, -0.9, -0.5)
    glVertex3f(-0.5, -0.55, -0.5)
    # Верхний квадрат
    glVertex3f(0.5, -0.55, 0.5)
    glVertex3f(0.5, -0.9, -0.5)
    glVertex3f(-0.5, -0.9, -0.5)
    glVertex3f(-0.5, -0.55, 0.5)
    # Нижний квадрат или наоборот
    glVertex3f(0.5, -0.55, 0.5)
    glVertex3f(-0.5, -0.9, 0.5)
    glVertex3f(-0.5, -0.9, -0.5)
    glVertex3f(0.5, -0.55, -0.5)
    glEnd()

    ''' Подставка для монитора'''
    glBegin(GL_QUADS)
    glColor4f(0, 0, 0, 1)
    # Передний квадрат
    glVertex3f(0.45, -0.45, 0.45)
    glVertex3f(0.45, -0.55, 0.45)
    glVertex3f(-0.45, -0.55, 0.45)
    glVertex3f(-0.45, -0.45, 0.45)
    # Задний квадрат
    glVertex3f(0.45, -0.45, -0.45)
    glVertex3f(0.45, -0.55, -0.45)
    glVertex3f(-0.45, -0.55, -0.45)
    glVertex3f(-0.45, -0.45, -0.45)
    # Правый квадрат
    glVertex3f(0.45, -0.45, 0.45)
    glVertex3f(0.45, -0.55, 0.45)
    glVertex3f(0.45, -0.55, -0.45)
    glVertex3f(0.45, -0.45, -0.45)
    # Левый квадрат
    glVertex3f(-0.45, -0.45, 0.45)
    glVertex3f(-0.45, -0.55, 0.45)
    glVertex3f(-0.45, -0.55, -0.45)
    glVertex3f(-0.45, -0.45, -0.45)
    # Верхний квадрат
    glVertex3f(0.45, -0.45, 0.45)
    glVertex3f(0.45, -0.55, -0.45)
    glVertex3f(-0.45, -0.55, -0.45)
    glVertex3f(-0.45, -0.45, 0.45)
    # Нижний квадрат или наоборот
    glVertex3f(0.45, -0.45, 0.45)
    glVertex3f(-0.45, -0.55, 0.45)
    glVertex3f(-0.45, -0.55, -0.45)
    glVertex3f(0.45, -0.45, -0.45)
    glEnd()

    ''' Трость для монитора'''
    glBegin(GL_QUADS)
    glColor4f(0.75, 0.6, 0, 1)
    # Передний квадрат
    glVertex3f(0.1, 0, 0.1)
    glVertex3f(0.1, -0.55, 0.1)
    glVertex3f(-0.1, -0.55, 0.1)
    glVertex3f(-0.1, 0, 0.1)
    # Задний квадрат
    glVertex3f(0.1, 0, -0.1)
    glVertex3f(0.1, -0.55, -0.1)
    glVertex3f(-0.1, -0.55, -0.1)
    glVertex3f(-0.1, 0, -0.1)
    # Правый квадрат
    glVertex3f(0.1, 0, 0.1)
    glVertex3f(0.1, -0.55, 0.1)
    glVertex3f(0.1, -0.55, -0.1)
    glVertex3f(0.1, 0, -0.1)
    # Левый квадрат
    glVertex3f(-0.1, 0, 0.1)
    glVertex3f(-0.1, -0.55, 0.1)
    glVertex3f(-0.1, -0.55, -0.1)
    glVertex3f(-0.1, 0, -0.1)
    # Верхний квадрат
    glVertex3f(0.1, 0, 0.1)
    glVertex3f(0.1, -0.55, -0.1)
    glVertex3f(-0.1, -0.55, -0.1)
    glVertex3f(-0.1, 0, 0.1)
    # Нижний квадрат или наоборот
    glVertex3f(0.1, 0, 0.1)
    glVertex3f(-0.1, -0.55, 0.1)
    glVertex3f(-0.1, -0.55, -0.1)
    glVertex3f(0.1, 0, -0.1)
    glEnd()

    ''' -Экран монитора'''
    glBegin(GL_QUADS)
    glColor4f(0, 0, 0, 1)
    # Передний квадрат
    glVertex3f(0.6, 0.9, 0.6)
    glVertex3f(0.6, 0, 0.6)
    glVertex3f(-0.6, 0, 0.6)
    glVertex3f(-0.6, 0.9, 0.6)
    # Задний квадрат
    glVertex3f(0.6, 0.9, -0.6)
    glVertex3f(0.6, 0, -0.6)
    glVertex3f(-0.6, 0, -0.6)
    glVertex3f(-0.6, 0.9, -0.6)
    # Правый квадрат
    glVertex3f(0.6, 0.9, 0.6)
    glVertex3f(0.6, 0, 0.6)
    glVertex3f(0.6, 0, -0.6)
    glVertex3f(0.6, 0.9, -0.6)
    # Левый квадрат
    glVertex3f(-0.6, 0.9, 0.6)
    glVertex3f(-0.6, 0, 0.6)
    glVertex3f(-0.6, 0, -0.6)
    glVertex3f(-0.6, 0.9, -0.6)
    # Верхний квадрат
    glVertex3f(0.6, 0.9, 0.6)
    glVertex3f(0.6, 0, -0.6)
    glVertex3f(-0.6, 0, -0.6)
    glVertex3f(-0.6, 0.9, 0.6)
    # Нижний квадрат или наоборот
    glVertex3f(0.6, 0.9, 0.6)
    glVertex3f(-0.6, 0, 0.6)
    glVertex3f(-0.6, 0, -0.6)
    glVertex3f(0.6, 0.9, -0.6)
    glEnd()


    glfw.swap_buffers(window)
glfw.terminate()