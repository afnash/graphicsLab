from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import sys


control_points = [
    [-0.8, -0.8],
    [-0.4,  0.8],
    [ 0.4, -0.8],
    [ 0.8,  0.8]
]

def bezier_point(t, p0, p1, p2, p3):
    """Calculate a point on a cubic Bezier curve."""
    u = 1 - t
    tt = t * t
    uu = u * u
    uuu = uu * u
    ttt = tt * t

    x = uuu * p0[0] + 3 * uu * t * p1[0] + 3 * u * tt * p2[0] + ttt * p3[0]
    y = uuu * p0[1] + 3 * uu * t * p1[1] + 3 * u * tt * p2[1] + ttt * p3[1]
    return x, y

def draw_bezier_curve():
    glColor3f(1.0, 1.0, 1.0)  # White color
    glBegin(GL_LINE_STRIP)

    
    for i in range(101):
        t = i / 100.0
        x, y = bezier_point(t, *control_points)
        glVertex2f(x, y)

    glEnd()

def draw_control_points():
    glPointSize(5.0)
    glColor3f(1.0, 0.0, 0.0)  # Red control points
    glBegin(GL_POINTS)
    for point in control_points:
        glVertex2f(point[0], point[1])
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_bezier_curve()
    draw_control_points()
    glFlush()

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Cubic Bezier Curve with OpenGL")
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()

if __name__ == "__main__":
    main()
