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

def translation_line(x1,y1,x2,y2,tx,ty):
	glClear(GL_COLOR_BUFFER_BIT)
	rgb=(1.0,0.0,0.0)
	line(x1,y1,x2,y2,rgb)
	X1=x1+tx
	Y1=y1+ty
	X2=x2+tx
	Y2=y2+ty
	rgb=(0.0,1.0,0.0)
	line(X1,Y1,X2,Y2,rgb)
	
	
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

def reflection_line(x1,y1,x2,y2,choice):
	glClear(GL_COLOR_BUFFER_BIT)
	rgb=(1.0,0.0,0.0)
	line(x1,y1,x2,y2,rgb)
	
	if choice==1:
		X1=x1
		Y1=-y1
		X2=x2
		Y2=-y2
	elif choice==2:
		X1=-x1
		Y1=y1
		X2=-x2
		Y2=y2
	elif choice==3:
		X1=-x1
		Y1=-y1
		X2=-x2
		Y2=-y2
	elif choice==4:
		X1=y1
		Y1=x1
		X2=y2
		Y2=x2
	elif choice==5:
		X1=-y1
		Y1=-x1
		X2=-y2
		Y2=-x2
	
	rgb=(0.0,1.0,0.0)
	line(X1,Y1,X2,Y2,rgb)
	
def main():
	choice=0
	x1=float(input("enter x1:"))
	y1=float(input("enter y1:"))
	x2=float(input("enter x2:"))
	y2=float(input("enter y2:"))
	
	while choice!=5:
		glutInit()
		glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
		glutInitWindowSize(500,500)
		glutInitWindowPosition(200,200)
		
		choice=int(input("Choose the 2D transformation Technique \n\t1.Translation\n\t2.Scaling\n\t3.Rotation\n\t4.Reflection\n\t5.Exit\n"))
		
		if choice==1:
			tx=float(input("tx coordinate"))
			ty=float(input("ty coordinate"))
			glutCreateWindow("2D TRANSLATION")
			glutDisplayFunc(lambda:translation_line(x1,y1,x2,y2,tx,ty))
			glutIdleFunc(lambda:translation_line(x1,y1,x2,y2,tx,ty))
			clearscreen()
			glutMainLoop()
		
		elif choice==2:
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
			
		elif choice==3:
		
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
		
		elif choice==4:
			ch=int(input("Choose reflection method:\n\t1.About x axis\n\t2.about y axis\n\t3.about origin\n\t4.about  y=x \n\t5.about y=-x\n"))
			glutCreateWindow("2D Reflection")
			glutDisplayFunc(lambda:reflection_line(x1,y1,x2,y2,ch))
			glutIdleFunc(lambda:reflection_line(x1,y1,x2,y2,ch))
			clearscreen()
			glutMainLoop()
		else:
			print("exiting program")
			break
main()	
			
