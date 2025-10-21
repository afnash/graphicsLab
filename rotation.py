from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

def clearscreen():
        glClearColor(0.0,0.0,0.0,0.0)
        gluOrtho2D(-100,100,-100,100)
        glClear(GL_COLOR_BUFFER_BIT)
        glLineWidth(2)

def line(x1,y1,x2,y2,rgb):
        glColor3f(rgb[0],rgb[1],rgb[2])
        glBegin(GL_LINES)
        glVertex2f(x1,y1)
        glVertex2f(x2,y2)
        glEnd()
        glFlush()
def rotation_line(x1,y1,x2,y2,angle,xr=0.0,yr=0.0):
        glClear(GL_COLOR_BUFFER_BIT)
        rgb=(0.0,1.0,0.0)
        line(x1,y1,x2,y2,rgb)
        rad_angle=(angle*math.pi)/180
        cosT=math.cos(rad_angle)
        sinT=math.sin(rad_angle)
        X1=cosT*(x1-xr)-sinT*(y1-yr)+xr
        Y1=sinT*(x1-xr)+cosT*(y1-yr)+yr
        X2=cosT*(x2-xr)-sinT*(y2-yr)+xr
        Y2=sinT*(x2-xr)+cosT*(y2-yr)+yr
        rgb=(1.0,0.0,0.0)
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
        angle=float(input("Rotation angle(degree)"))
        method=int(input("1.About Orgin\n2.About reference Point"))
        if method==1:
                glutCreateWindow("2D rotation about orgin")
                glutDisplayFunc(lambda:rotation_line(x1,y1,x2,y2,angle))
                glutIdleFunc(lambda:rotation_line(x1,y1,x2,y2,angle))   
        else:
                xr=int(input("Enter x coordinate of reference point"))
                yr=int(input("Enter y coordinate of reference point"))
                glutCreateWindow("2D rotation about reference point")
                glutDisplayFunc(lambda:rotation_line(x1,y1,x2,y2,angle,xr,yr))
                glutIdleFunc(lambda:rotation_line(x1,y1,x2,y2,angle,xr,yr))     
        clearscreen()
        glutMainLoop()
main()


