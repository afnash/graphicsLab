import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

x0, y0, x1, y1 = 0, 0, 0, 0

def init():
    glClearColor(0, 0, 0, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-300, 300, -300, 300)

def dda_line(x0, y0, x1, y1):
    points = []
    dx = x1 - x0
    dy = y1 - y0

    if abs(dx) > abs(dy):
        m = dy / dx if dx != 0 else 0
        x, y = x0, y0
        step = 1 if dx > 0 else -1
        while (step > 0 and x <= x1) or (step < 0 and x >= x1):
            points.append((round(x), round(y)))
            x += step
            y += m * step
    else:
        m = dx / dy if dy != 0 else 0
        x, y = x0, y0
        step = 1 if dy > 0 else -1
        while (step > 0 and y <= y1) or (step < 0 and y >= y1):
            points.append((round(x), round(y)))
            y += step
            x += m * step

    return points

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 0, 1)
    glPointSize(3)

    points = dda_line(x0, y0, x1, y1)
    glBegin(GL_POINTS)
    for x, y in points:
        glVertex2f(x, y)
    glEnd()

    glutSwapBuffers()
    glutPostRedisplay()

def main():
    global x0, y0, x1, y1

    print("Enter the starting point of the line:")
    x0 = int(input("x0: "))
    y0 = int(input("y0: "))
    print("Enter the ending point of the line:")
    x1 = int(input("x1: "))
    y1 = int(input("y1: "))

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"DDA Line Drawing")
    init()
    glutDisplayFunc(draw)
    glutMainLoop()

if __name__ == "__main__":
    main()

