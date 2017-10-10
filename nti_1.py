ax,ay=map(int, input().split())
bx,by=map(int, input().split())

print(max(abs(ax-bx), abs(ay-by)))
