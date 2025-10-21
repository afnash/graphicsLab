from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

width,height = 600,600
circle_centre = (width // 2, height // 2)
radius = 150

def plot_points(x,y):
 glVertex2f(x,y)

def plot_circle_symmetry(cx,cy,x,y,):
 plot_points(cx+x,cy+y)
 plot_points(cx-x,cy+y) 
 plot_points(cx+x,cy-y) 
 plot_points(cx-x,cy-y)
 plot_points(cx+y,cy+x)
 plot_points(cx-y,cy+x) 
 plot_points(cx+y,cy-x)
 plot_points(cx-y,cy-x)
 
def draw_circle_midpoint(cx,cy,r):
 x = 0
 y = r
 d = 1-r
 glBegin(GL_POINTS)
 plot_circle_symmetry(cx,cy,x,y)
 
 while x <= y:
  x+=1
  if d<0:
   d+=2*x+1
  else:
   y-=1
   d+=2*(x-y)+1
  plot_circle_symmetry(cx,cy,x,y)
 glEnd() 

def display():
 glClear(GL_COLOR_BUFFER_BIT)
 glLoadIdentity()
 glColor3f(0.0,0.6,1.0)
 glPointSize(3)
 cx,cy = circle_centre
 r = radius
 draw_circle_midpoint(cx,cy,r)
 glutSwapBuffers()
 
def reshape(width,height):
 glViewport(0,0,width,height)
 glMatrixMode(GL_PROJECTION)
 glLoadIdentity()
 glOrtho(0,width,0,height,-1,1)
 glMatrixMode(GL_MODELVIEW)
 glLoadIdentity()
 
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE |GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Circle")

    glClearColor(0,0,0,1)
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
 
 
   
