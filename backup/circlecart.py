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

def draw_circle_cartesian(cx,cy,r):
 glBegin(GL_POINTS)
 x=-r
 while x<=r:
  y=math.sqrt(r*r-x*x)
  glVertex2f(cx+x,cy+y)
  glVertex2f(cx+x,cy-y)
  x+=0.01
 glEnd() 
 
def display(): 
 glClear(GL_COLOR_BUFFER_BIT)
 glColor3f(0,0,0.5)
 glPointSize(3)
 draw_circle_cartesian(cx,cy,radius)
 glFlush()
  
  
def main():
 glutInit(sys.argv)
 glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
 glutInitWindowSize(width,height)
 glutInitWindowPosition(100,100)
 glutCreateWindow(b"cartesian Circle")
 init()
 glutDisplayFunc(display)
 glutMainLoop()
if __name__ == "__main__":
 main()   
