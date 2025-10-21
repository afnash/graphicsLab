from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

width, height = 500, 500

def bresenham_line(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1

    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    if dy <= dx:
        err = dx // 2
        while x != x2:
            glVertex2f(x, y)
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
        glVertex2f(x, y)
    else:
        err = dy // 2
        while y != y2:
            glVertex2f(x, y)
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy
        glVertex2f(x, y) 

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,1,1)

    glBegin(GL_POINTS)
    bresenham_line(100, 100, 400, 400)
    glEnd()

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Bresenham Line")

    glClearColor(0,0,0,1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)

    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()

