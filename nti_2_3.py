mask = input()
count = input()
addreses=[]
m=[255,255,255,0]
s=set()
for i in range(int(count)):
    addreses.append(input())
for addr in addreses:
    addrArr = list(map(int,addr.split('.')))
    a=[]
    for i in range(4):
        r=addrArr[i]&m[i]
        a.append(r)
    s.add(str(a))
print(len(s))
