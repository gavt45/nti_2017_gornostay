import sys
import time

def parse_data(data):
    lines = data.split('\n')

    n, m, u, v = map(int, lines[0].split())
    lines = lines[1:]

    bridges = []
    for i in range(m):
        bridge = tuple(map(int, lines[i].split()))
        bridges.append(bridge)
    lines = lines[m:]

    k = int(lines[0])
    sinked = list(map(int, lines[1].split())) if k != 0 else []

    return u, v, bridges, sinked


def next_island(bridge, c):
    return bridge[1] if bridge[0] == c else bridge[0]


def get_reachable_islands(bridges, c):
    islands = []
    for bridge in bridges:
        if c in bridge:
            n = next_island(bridge, c)
            islands.append(n)
    return islands


def solve(data):
    u, v, bridges, sinked = parse_data(data)
    print(u, v)
    print('bridges', bridges)
    print('sinked', sinked)

    work_bridges = []
    for bridge in bridges:
        if bridge[0] not in sinked and bridge[1] not in sinked:
            work_bridges.append(bridge)
    print('bridges', work_bridges)

    todo = set([u])
    done = set()
    print(todo, done)

    while todo:

        c = todo.pop()
        if c in done:
            continue
        done.add(c)

        qwe = get_reachable_islands(work_bridges, c)
        print(c, qwe)
        for n in qwe:
            if n == v:
                print('YES')
                exit(0)
            todo.add(n)

        print('\t', todo, done)
        time.sleep(1)

    print('NO')



data = sys.stdin.read()
solve(data)
