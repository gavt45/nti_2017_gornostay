import sys

def parse(data):
    lines = data.split('\n')
    n = int(lines[0])
    m = int(lines[1])
    lines = lines[2:]

    bridges = {i+1: tuple(map(int, lines[i].split())) for i in range(m)}
    lines = lines[m:]

    bad = [int(i) for i in lines[1].split()]

    return n, bridges, bad

def dfs(c, cables, visited):
    for cable in cables:
        if c in cable:
            t = cable[1] if cable[0] == c else cable[0]
            if t not in visited:
                visited.add(t)
                dfs(t, cables, visited)

def solve(data):
    n, cables, bad_cables = parse(data)
    # print(n, cables, bad_cables)

    result = []
    for bad in bad_cables:
        del cables[bad]
        # print(bad, cables)

        visited = set()
        components = 0

        for c in range(1, n+1):
            if c not in visited:
                visited.add(c)
                components += 1
                dfs(c, cables.values(), visited)

        result.append(components)

    print(' '.join(str(r) for r in result))

solve(sys.stdin.read())