from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
print("Enter the coordinates of the 1st endpoint:")
x1 = float(input("x1: "))
y1 = float(input("y1: "))
print("Enter the coordinates of the 2nd endpoint:")
x2 = float(input("x2: "))
y2 = float(input("y2: "))
print("Enter translation distances:")
tx = float(input("translate in x direaction: "))
ty = float(input("translate in y direction: "))


def init():
 glClearColor(0,0,0,1)
 glMatrixMode(GL_PROJECTION)
 glLoadIdentity()
 gluOrtho2D(-200,200,-200,200)

def display():
 glClear(GL_COLOR_BUFFER_BIT)
 glBegin(GL_LINES)
 glColor3f(0,0,1)
 glVertex2f(x2,y2)
 glVertex2f(x1,y1)
 glEnd()
 
 glColor3f(1,0,1)
 glBegin(GL_LINES)
 glVertex2f(x1+tx,y1+ty)
 glVertex2f(x2+tx,y2+ty)
 glEnd()
 
 glFlush()
 
def main():
 glutInit(sys.argv)
 glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
 glutInitWindowSize(500,500)
 glutInitWindowPosition(100,100)
 glutCreateWindow(b"Line Translation")
 init()
 glutDisplayFunc(display)
 glutMainLoop()
if __name__ == "__main__":
 main()   
 
 
