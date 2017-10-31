import sys
from collections import Counter

def parse(data):
	lines = data.split('\n')
	n, k = [int(x) for x in lines[0].split()]
	s = lines[1]
	return k, s

def solve(data):
	k, s = parse(data)
	# print(k, s)

	counter = Counter(s)
	most_common_list = counter.most_common()
	most_common_chars = [char for char, count in most_common_list if count == most_common_list[0][1]]
	most_common_char = min(most_common_chars)

	s_k = s + most_common_char * k
	print(s_k)

solve(sys.stdin.read())