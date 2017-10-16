import math
x1,y1,x2,y2,x3,y3=0, 2, 2, 0, 2, 2#input().split()
dx,dy=3, 1#input().split()
"""
Этот код не работает 
Я его не дописал
"""

"""
x1,y1 --- a
x2,y2 --- b 
x3,y3 --- c
"""

def deg(rad):
	return (rad*180)/math.pi

def border_length(x1,y1,x2,y2):
	return math.sqrt(((x1+x2)/2)**2+((y1+y2)/2)**2)

def get_angle(dx,dy,x1,y1,x2,y2):
	a=border_length(dx,dy,x2,y2)
	b=border_length(dx,dy,x1,y1)
	c=border_length(x1,y1,x2,y2)
	cosa = (b**2+c**2-a**2)/(2*b*c)
	return math.acos(cosa)
dangles=[]
dangles.append(get_angle(dx,dy,x1,y1,x2,y2))
dangles.append(get_angle(dx,dy,x2,y2,x3,y3))
dangles.append(get_angle(dx,dy,x3,y3,x1,y1))

angles=[]
angles.append(get_angle(x3,y3,x1,y1,x2,y2))
angles.append(get_angle(x3,y3,x2,y2,x3,y3))
angles.append(get_angle(x2,y2,x3,y3,x1,y1))

lens=[]
lens.append(border_length(x1,y1,x2,y2))
lens.append(border_length(x2,y2,x3,y3))
lens.append(border_length(x3,y3,x1,y1))

print "dangles: ",map(deg, dangles)

print "angles: ",map(deg, angles)

for i in range(0,3):
	print "angle:",angles[i],";dangle:",dangles[i]
	if angles[i] >= dangles[i]:
		print "final: ",lens[i]
	elif angles[i] < dangles[i]:
		print "final: ",lens[i]+lens[i+1]