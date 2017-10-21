n,m,v,u=map(int,input().split())

bridges=[]

for i in range(m):
    a=list(map(int,input().split()))
    bridges.append((a[0], a[1]))
count=input()
if int(count)!= 0:
    bad=list(map(int,input().split()))
else:
    bad=[]

bridges_=list(bridges)

for bridge in bridges:
    #print(bridge)
    if (bridge[0] in bad) or (bridge[1] in bad):
        bridges_.remove(bridge)
del bridges
bridges = bridges_
del bridges_
#print("bridges:", bridges)

todo=set([v])
done=set()

def get_islands(bridges, c):
    out=[]
    for br in bridges:
        if c in br:
            out.append(br[1] if br[0] == c else br[0])
    return out

while todo:
    c=todo.pop()
    if c in done:
        continue
    isls = get_islands(bridges, c)
    for i in isls:
        if i==u:
            print("YES")
            exit(0)
        todo.add(i)
    #if c not in visited:
    done.add(c)
print("NO")
