n, m, v, u = map(int, input().split())
print(v, u)

mos = []
for i in range(m):
    a = list(map(int, input().split()))
    mos.append(a)
print(mos)

k = int(input())
if k != 0:
    zat = list(map(int, input().split()))
else:
    zat = []
print(zat)

ways = []
c = False
for i in mos:
    if v in i:
        try:
            n = i[i.index(v)+1]
        except:
            n = i[i.index(v)-1]
        if n not in zat:
            ways.append([v, n])
print(ways)
print()

for i in ways:
    for b in mos:
        if i[-1] in b:
            try :
                n = b[b.index(i[-1])+1]
            except:
                n = b[b.index(i[-1])-1]
            if n not in i and n not in zat:
                i.append(n)
        print(ways)
        if i[-1] == u:
            c = True
            print('break')
            break

if c == True:
    print('YES')
else:
    print('NO')
