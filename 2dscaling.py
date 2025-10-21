from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

def clearscreen():
        glClearColor(0.0,0.0,0.0,0.0)
        gluOrtho2D(-100,100,-100,100)
        glClear(GL_COLOR_BUFFER_BIT)
        glPointSize(5.0)

def line(x1,y1,x2,y2,rgb):
        glColor3f(rgb[0],rgb[1],rgb[2])
        glBegin(GL_LINES)
        glVertex2f(x1,y1)
        glVertex2f(x2,y2)
        glEnd()
        glFlush()

def scaling_line(x1,y1,x2,y2,sx,sy,xr=0.0,yr=0.0):
        glClear(GL_COLOR_BUFFER_BIT)
        rgb=(1.0,0.0,0.0)
        line(x1,y1,x2,y2,rgb)
        X1=(x1-xr)*sx+xr
        X2=(x2-xr)*sx+xr
        Y1=(y1-yr)*sy+yr
        Y2=(y2-yr)*sy+yr
        rgb=(0.0,1.0,0.0)
        line(X1,Y1,X2,Y2,rgb)
def main():
        x1=float(input("enter x1:"))
        y1=float(input("enter y1:"))
        x2=float(input("enter x2:"))
        y2=float(input("enter y2:"))
        glutInit()
        glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
        glutInitWindowSize(500,500)
        glutInitWindowPosition(200,200)
        sx=float(input("scaling factor of x"))
        sy=float(input("scaling factor of y"))
        method=int(input("1.About Orgin\n2.About reference Point"))             
        if method==1:
                glutCreateWindow("2D scaling")
                glutDisplayFunc(lambda:scaling_line(x1,y1,x2,y2,sx,sy))
                glutIdleFunc(lambda:scaling_line(x1,y1,x2,y2,sx,sy))
        else:
                xr=int(input("Enter x coordinate of reference point"))
                yr=int(input("Enter y coordinate of reference point"))
                glutCreateWindow("2D scaling about reference")
                glutDisplayFunc(lambda:scaling_line(x1,y1,x2,y2,sx,sy,xr,yr))
                glutIdleFunc(lambda:scaling_line(x1,y1,x2,y2,sx,sy,xr,yr))
        clearscreen()
        glutMainLoop()
main()


 
