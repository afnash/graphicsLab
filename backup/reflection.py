from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
x1,y1=map(float,input("Enter 1st point of line(x1,y1):").split())
x2,y2=map(float,input("Enter 2nd point of line(x1,y1):").split())

print("\nReflection options:")
print("1. About origin")
print("2.About x-axis")
print("3.About y-axis")
print("4.About line x=y")
print("5.About line x=-y")
choice = int(input("Enter your choice(1-5):"))

def reflect_point(x,y,option):
 if option == 1:
  return -x,-y
 elif option == 2:
  return x,-y
 elif option == 3:
  return -x,y  
 elif option == 4:
  return y,x 
 elif option == 5:
  return -y,-x 
 else: 
  return x,y
xr1,yr1=reflect_point(x1,y1,choice) 
xr2,yr2=reflect_point(x2,y2,choice) 

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
 glutCreateWindow(b"Line rotation")
 init()
 glutDisplayFunc(display)
 glutMainLoop()
if __name__ == "__main__":
 main()   
 
   
