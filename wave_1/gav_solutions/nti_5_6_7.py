#ryfms=[]
"""
1=(1,2)(3,4)
2=(1,3)(2,4)
3=(1,4)(2,3)
"""

def cw(w1,w2):
    if len(w1) == 1 or len(w2) == 1:
        return False
    else:
        return w1[-2:]==w2[-2:]

def cl(l1,l2):
    w1 = l1.split(' ')[-1]
    w2 = l2.split(' ')[-1]
    return cw(w1,w2)

def check_chetwr(chetwr):
    if cl(chetwr[0], chetwr[1]) and cl(chetwr[2], chetwr[3]):
        return 1
    elif cl(chetwr[0], chetwr[2]) and cl(chetwr[1], chetwr[3]):
        return 2
    elif cl(chetwr[0], chetwr[3]) and cl(chetwr[1], chetwr[2]):
        return 3
    else:
        print("Nope")
        exit(0)

count = input()
chetwr=[]
strokes=[]
for i in range(int(count)):
    strokes.append(input())
    if i%4==3 and i != 0:
        chetwr.append(strokes)
        strokes=[]
print(chetwr)
s=set()

for choto in chetwr:
    s.add(str(check_chetwr(choto)))
print(s)
if len(s)==1:
    print("Yes")
else:
    print("Nope")

#for chetIdx in range(0,len(strokes)-1)
