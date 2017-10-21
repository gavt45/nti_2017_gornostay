n, k = list(map(int, input().split()))
points = list(map(int, input().split()))

def solve():
	first = points[0]
	last = points[-1]
	dist = last - first

	for count in range(k, 0, -1):
		lenght = dist / count
		#print(count, lenght)

		if not lenght.is_integer():
			continue

		lenght = int(lenght)
		good_points = set(range(first, last+1, lenght))
		
		if good_points.issubset(points):
			print(lenght)
			break

solve()
