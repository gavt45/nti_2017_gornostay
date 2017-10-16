import sys
import math


def parse_input(data):
    # разбиваем входные данные на строки
    lines = data.split('\n')

    # приводим к списку int-ов
    points = list(map(int, lines[0].split()))

    triangle = []
    # добавляем координаты вершин в треугольник
    for i in range(0, 6, 2):
        vertex = (points[i], points[i+1])
        triangle.append(vertex)
    
    # приводим к списку int-ов и создаем точку D
    D = tuple(map(int, lines[1].split()))
    
    return triangle, D


def dist_square(p1, p2):
    '''
    Возвращает КВАДРАТ расстояния между точками
    '''
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2


def dist(p1, p2):
    '''
    Возвращает расстояние между точками
    '''
    return math.sqrt(dist_square(p1, p2))


def angle(p1, p2, p3):
    '''
    Функция возвращает угол p1-p2-p3, то есть угол в вершине p2 между вершин p1 и p3
    '''
    a2 = dist_square(p1, p3)
    b = dist(p2, p1)
    b2 = dist_square(p2, p1)
    c = dist(p2, p3)
    c2 = dist_square(p2, p3)
    # из теоремы косинусов:
    # cos α = (b**2 + c**3 - a**2) / (2*b*c)
    cos_α = (b2 + c2 - a2) / (2*b*c)
    # для нахождения угла берем arccos
    return math.degrees(math.acos(cos_α))


def solve(data):
    # парсим входные данные
    # будем представлять точку как тупл из 2х элементов
    # получаем список из 3х туплов - треугольник, и еще один тупл - точку D
    triangle, D = parse_input(data)
    print(triangle)
    print(D)

    # сортируем вершиы в порядке удаления от точки D
    triangle.sort(key=lambda p: dist(p, D))
    print(triangle)

    # вычисляем 2 угла треугольника, возле 2х дальних вершин
    a1 = angle(triangle[0], triangle[1], triangle[2])
    a2 = angle(triangle[0], triangle[2], triangle[1])
    print(a1, a2)

    # вычисляем 2 угла для точки D и дальней стороны треугольника
    _a1 = angle(D, triangle[1], triangle[2])
    _a2 = angle(D, triangle[2], triangle[1])
    print(_a1, _a2)

    # проверяем условия, находим область, в которой расположена точка D
    # печатем результат
    if _a1 <= a1:
        print('_a1 <= a1: {} <= {}'.format(_a1, a1))
        print(dist(triangle[0], triangle[2]))
    elif _a2 <= a2:
        print('_a2 <= a2: {} <= {}'.format(_a2, a2))
        print(dist(triangle[0], triangle[1]))
    else:
        print('_a1 > a1: {} <= {}'.format(_a1, a1))
        print('_a2 > a2: {} <= {}'.format(_a2, a2))
        print(dist(triangle[0], triangle[1]) + dist(triangle[0], triangle[2]))


# функция "sys.stdin.read" читает все данные из стандартного входного потока
solve(sys.stdin.read())

# если выполнить скрипт в терминале как обычно:
# python solve.py
# то данные нужно вводить с клавиатуры
# при этом после ввода всех данных нужно ввести специальный символ окончания ввода
# для Windows это CTRL+Z (и нажать enter), для Unix - CTRL+D

# скрипт также можно запустить, изменив стандартный ввод. звучит сложно, но делается очень просто:
# python solve.py < input1.txt
# тогда входные данные будут считаны из файла input1.txt
# я добавил несколько таких файлов для примера

# также можно проверить работы программу на данных из строки

# data = '''0 2 2 0 2 2
# 3 1'''
# solve(data)