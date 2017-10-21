n, k = list(map(int, input().split()))
points = list(map(int, input().split()))

"""
def parse_data(data):
	lines = data.split('\n')
	n, k = list(map(int, lines[0].split()))
	points = list(map(int, lines[1].split()))
	return n, k, points
"""

def solve():
	#print(n, k)
	#print(points)

	first = points[0]
	last = points[-1]
	dist = last - first
	#print(dist)

	# min_lenght = dist / (n - 1)
	# min_lenght = dist / k
	# print(min_lenght)

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
