from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

# Объявляем все глобальные переменные
global xrot  # Величина вращения по оси x
global yrot  # Величина вращения по оси y
global ambient  # рассеянное освещение
global treecolor  # Цвет елочного стебля
global lightpos  # Положение источника освещения


def drawBody():
    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)

    glMaterialfv(GL_FRONT, GL_DIFFUSE, treecolor)
    glTranslatef(0.0, 0.0, -0.5)
    quadratic = gluNewQuadric()
    gluSphere(quadratic, 0.5, 100, 100)

    glTranslatef(0.0, 0.0, 1)
    gluSphere(quadratic, 0.5, 100, 100)
    glTranslatef(0.0, 0.0, -1)
    gluCylinder(quadratic, 0.5, 0.5, 1, 100, 100)

    glPopMatrix()


def drawTail():
    # Up
    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glRotatef(90, 1.0, 0.0, 0.0)

    glMaterialfv(GL_FRONT, GL_DIFFUSE, treecolor)
    quadratic = gluNewQuadric()

    glTranslatef(0.0, 0.75, 0)
    glutSolidCone(0.2, 1.0, 100, 100)
    glPopMatrix()




def drawWings():
    glPushMatrix()
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glRotatef(90, 1.0, 1.0, 1.0)
    glTranslatef(0.0, -0.2, 0.35)

    glMaterialfv(GL_FRONT, GL_DIFFUSE, treecolor)
    quadratic = gluNewQuadric()

    glutSolidCone(0.256, 1.0, 100, 100)
    glPopMatrix()

    glPushMatrix()
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glRotatef(90, 1.0, -1.0, -1.0)
    glTranslatef(0.0, -0.2, 0.35)

    glMaterialfv(GL_FRONT, GL_DIFFUSE, treecolor)
    quadratic = gluNewQuadric()

    glutSolidCone(0.256, 1.0, 100, 100)
    glPopMatrix()

def drawHighway():
    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glRotatef(90, 1.0, 0.0, 0.0)

    glMaterialfv(GL_FRONT, GL_DIFFUSE, treecolor)
    quadratic = gluNewQuadric()

    glTranslatef(0.25, 0.5, -0.6)
    gluCylinder(quadratic, 0.125, 0.125, 0.5, 100, 100)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glRotatef(90, 1.0, 0.0, 0.0)

    glMaterialfv(GL_FRONT, GL_DIFFUSE, treecolor)
    quadratic = gluNewQuadric()

    glTranslatef(-0.25, 0.5, -0.6)
    gluCylinder(quadratic, 0.125, 0.125, 0.5, 100, 100)
    glPopMatrix()

def drawNose():
    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0, 0, 0, 1))
    quadratic = gluNewQuadric()
    glTranslatef(0.0, 0.125, -0.82)
    gluSphere(quadratic, 0.2, 100, 100)
    glPopMatrix()

def drawFrontWindows():
    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (1, 1, 1, 1))
    quadratic = gluNewQuadric()
    glTranslatef(0.25, -0.125, -0.8)
    gluSphere(quadratic, 0.125, 100, 100)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (1, 1, 1, 1))
    quadratic = gluNewQuadric()
    glTranslatef(-0.25, -0.125, -0.8)
    gluSphere(quadratic, 0.125, 100, 100)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (1, 1, 1, 1))
    quadratic = gluNewQuadric()
    glTranslatef(0.15, -0.125, -0.86)
    gluSphere(quadratic, 0.125, 100, 100)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (1, 1, 1, 1))
    quadratic = gluNewQuadric()
    glTranslatef(-0.15, -0.125, -0.86)
    gluSphere(quadratic, 0.125, 100, 100)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (1, 1, 1, 1))
    quadratic = gluNewQuadric()
    glTranslatef(0.05, -0.125, -0.89)
    gluSphere(quadratic, 0.125, 100, 100)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (1, 1, 1, 1))
    quadratic = gluNewQuadric()
    glTranslatef(-0.05, -0.125, -0.89)
    gluSphere(quadratic, 0.125, 100, 100)
    glPopMatrix()


# Процедура инициализации
def init():
    global xrot  # Величина вращения по оси x
    global yrot  # Величина вращения по оси y
    global ambient  # Рассеянное освещение
    global treecolor  # Цвет елочного ствола
    global lightpos  # Положение источника освещения

    xrot = 0.0  # Величина вращения по оси x = 0
    yrot = 0.0  # Величина вращения по оси y = 0
    ambient = (1.0, 1.0, 1.0, 1)  # Первые три числа цвет в формате RGB, а последнее - яркость
    treecolor = (1.0, 1.0, 1.0, 0.8)  # Коричневый цвет для ствола
    lightpos = (2, -2, 0)  # Положение источника освещения по осям xyz

    glClearColor(0.5, 0.5, 0.5, 1.0)  # Серый цвет для первоначальной закраски
    gluOrtho2D(-1.5, 1.5, -1.5, 1.5)  # Определяем границы рисования по горизонтали и вертикали
    glRotatef(-90, 1.0, 0.0, 0.0)  # Сместимся по оси Х на 90 градусов
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient)  # Определяем текущую модель освещения
    glEnable(GL_LIGHTING)  # Включаем освещение
    glEnable(GL_LIGHT0)  # Включаем один источник света
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)  # Определяем положение источника света
    glEnable(GL_DEPTH_TEST)


# Процедура обработки специальных клавиш
def specialkeys(key, x, y):
    global xrot
    global yrot
    # Обработчики для клавиш со стрелками
    if key == GLUT_KEY_UP:  # Клавиша вверх
        xrot -= 4.0  # Уменьшаем угол вращения по оси Х
    if key == GLUT_KEY_DOWN:  # Клавиша вниз
        xrot += 4.0  # Увеличиваем угол вращения по оси Х
    if key == GLUT_KEY_LEFT:  # Клавиша влево
        yrot -= 4.0  # Уменьшаем угол вращения по оси Y
    if key == GLUT_KEY_RIGHT:  # Клавиша вправо
        yrot += 4.0  # Увеличиваем угол вращения по оси Y

    glutPostRedisplay()  # Вызываем процедуру перерисовки


# Процедура перерисовки
def draw():
    global xrot
    global yrot
    global lightpos
    global greencolor
    global treecolor

    # glClear(GL_COLOR_BUFFER_BIT)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)  # Источник света вращаем вместе с елкой

    drawBody()
    drawHighway()
    drawFrontWindows()
    drawNose()
    drawTail()
    drawWings()
    glutSwapBuffers()  # Выводим все нарисованное в памяти на экран


# Здесь начинается выполнение программы
# Использовать двойную буферизацию и цвета в формате RGB (Красный, Зеленый, Синий)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
# Указываем начальный размер окна (ширина, высота)
glutInitWindowSize(500, 500)
# Указываем начальное положение окна относительно левого верхнего угла экрана
glutInitWindowPosition(400, 200)
# Инициализация OpenGl
glutInit(sys.argv)
# Создаем окно с заголовком "Airplane"
glutCreateWindow(b"Airplane")
# Определяем процедуру, отвечающую за перерисовку
glutDisplayFunc(draw)
# Определяем процедуру, отвечающую за обработку клавиш
glutSpecialFunc(specialkeys)
# Вызываем нашу функцию инициализации
init()
# Запускаем основной цикл
glutMainLoop()