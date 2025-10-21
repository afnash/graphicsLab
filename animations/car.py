from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math


car_x = -200   # starting X position of car
wheel_angle = 0   # wheel rotation

def draw_circle(x, y, r):
    glBegin(GL_POLYGON)
    for i in range(360):
        theta = math.radians(i)
        glVertex2f(x + r * math.cos(theta), y + r * math.sin(theta))
    glEnd()

def draw_wheel(x, y, r):
    global wheel_angle

    # Tire
    glColor3f(0, 0, 0)
    draw_circle(x, y, r)

    # Hub
    glColor3f(0.7, 0.7, 0.7)
    draw_circle(x, y, r/3)

    # Spokes
    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    for i in range(4):  # 4 spokes
        theta = math.radians(wheel_angle + i * 90)
        glVertex2f(x, y)
        glVertex2f(x + r * math.cos(theta), y + r * math.sin(theta))
    glEnd()

def draw_car():
    global car_x

    # Car body
    glColor3f(0.2, 0.6, 1)  # blue body
    glBegin(GL_POLYGON)
    glVertex2f(car_x, 100)
    glVertex2f(car_x + 200, 100)
    glVertex2f(car_x + 200, 150)
    glVertex2f(car_x, 150)
    glEnd()

    # Car roof
    glColor3f(1, 0, 0)  # red roof
    glBegin(GL_POLYGON)
    glVertex2f(car_x + 50, 150)
    glVertex2f(car_x + 150, 150)
    glVertex2f(car_x + 120, 200)
    glVertex2f(car_x + 80, 200)
    glEnd()

    # Wheels
    draw_wheel(car_x + 50, 90, 20)
    draw_wheel(car_x + 150, 90, 20)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    draw_car()
    glutSwapBuffers()

def update(value):
    global car_x, wheel_angle
    car_x += 5
    wheel_angle -= 15   # rotate wheel clockwise
    if wheel_angle <= -360:
        wheel_angle = 0
    if car_x > 600:   # reset to left side
        car_x = -200
    glutPostRedisplay()
    glutTimerFunc(30, update, 0)


def init():
    glClearColor(0.3, 0.3, 0.3, 1)   # white background
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 600, 0, 400)  # 2D world size
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(600, 400)
    glutCreateWindow(b"Car Animation with Horn")
    init()
    glutDisplayFunc(display)
 
    glutTimerFunc(0, update, 0)
    glutMainLoop()

main()

