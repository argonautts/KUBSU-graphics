import glfw
from OpenGL.GL import *
import keyboard

if not glfw.init():
    raise Exception("Не удалось инициализировать библиотеку")

window = glfw.create_window(1000, 600, "PC", None, None)

if not window:
    glfw.terminate()
    raise Exception("Ошибка при инициализации окна")

glfw.set_window_pos(window, 400, 200)
glfw.make_context_current(window)
glClearColor(1, 1, 1, 0)
glEnable(GL_DEPTH_TEST)

while not glfw.window_should_close(window):
    glfw.poll_events()
    glClear(GL_COLOR_BUFFER_BIT)
    glClear(GL_DEPTH_BUFFER_BIT )
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    if keyboard.read_key() == "r":
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