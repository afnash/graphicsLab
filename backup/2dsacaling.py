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
s = float(input("scalling factor: "))
choice = int(input("Rotate w.r.t. 1.Origin 2.Reference point?"))
if choice ==2:
 xr,yr = map(float,input("Enter refrence point(xr,yr):").split())
else:
 xr,yr = 0.0,0.0 


def scale_point(x,y,xr,yr,s):
 x_shift = x-xr
 y_shift = y-yr
 
 xr_new=x_shift*s
 yr_new=y_shift*s
 
 return xr_new+xr,yr_new+yr
 
xr1,yr1=scale_point(x1,y1,xr,yr,s) 
xr2,yr2=scale_point(x2,y2,xr,yr,s) 
def init():
 glClearColor(0,0,0,1)
 glMatrixMode(GL_PROJECTION)
 glLoadIdentity()
 gluOrtho2D(-200,200,-200,200)

def display():
 glClear(GL_COLOR_BUFFER_BIT)
 glBegin(GL_LINES)
 glColor3f(0,0,1)
 glVertex2f(x1,y1)
 glVertex2f(x2,y2)
 glEnd()
 
 glColor3f(1,0,1)
 glBegin(GL_LINES)
 glVertex2f(xr1,yr1)
 glVertex2f(xr2,yr2)
 glEnd()
 
 glFlush()
 
def main():
 glutInit(sys.argv)
 glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
 glutInitWindowSize(500,500)
 glutInitWindowPosition(100,100)
 glutCreateWindow(b"Line scalling")
 init()
 glutDisplayFunc(display)
 glutMainLoop()
if __name__ == "__main__":
 main()   
 
 
