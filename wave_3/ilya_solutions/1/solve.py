import sys

def parse(data):
    lines = data.split('\n')
    sides = [int(x) for x in lines[0].split()]
    return sides

def solve(data):
    sides = parse(data)

    for side in sides:
    	other_sides = sides.copy()
    	other_sides.remove(side)

    	if side >= sum(other_sides):
    		print('No')
    		return

    print('Yes')

def solve(data):
    sides = parse(data)

    max_side = max(sides)
    other_sides = sides.copy()
    other_sides.remove(max_side)

    if max_side < sum(other_sides):
    	print('Yes')
    else:
    	print('No')

solve(sys.stdin.read())