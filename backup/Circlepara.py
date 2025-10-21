from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
cx=int(input("Enter circle center x:"))
cy=int(input("Enter circle center y:"))
radius=int(input("Enter circle radius:"))
width,height=500,500

def init():
 glClearColor(0,0,0,1)
 glMatrixMode(GL_PROJECTION)
 glLoadIdentity()
 gluOrtho2D(-width//2,width//2,-height//2,height//2)

def draw_circle_parametric(cx,cy,r):
 glBegin(GL_POINTS)
 theta = 0.0
 step = 0.001
 while theta <= 2*math.pi:
  x=r*math.cos(theta)
  y=r*math.sin(theta)
  glVertex2f(cx +x,cy+y)
  theta +=step
 glEnd()
 
 
def display(): 
 glClear(GL_COLOR_BUFFER_BIT)
 glColor3f(0,1,0)
 glPointSize(2)
 draw_circle_parametric(cx,cy,radius)
 glFlush()
  
  
def main():
 glutInit(sys.argv)
 glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
 glutInitWindowSize(width,height)
 glutInitWindowPosition(100,100)
 glutCreateWindow(b"Parametric Circle")
 init()
 glutDisplayFunc(display)
 glutMainLoop()
if __name__ == "__main__":
 main()   
