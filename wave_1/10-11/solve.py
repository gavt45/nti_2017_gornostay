import sys


def parse_input(data):
    # разбиваем входные данные на строки
    lines = data.split('\n')
    
    # считываем число вершин и удаляем строку
    n = int(lines[0])
    lines = lines[1:]
    
    # считываем n вершин
    files_graph = {}
    for i in range(n):
        # приводим к массиву int-ов
        line = list(map(int, lines[i].split()))
        # добавляем в граф зависимостей числа кроме 1го, т.к. 1е число - это количество файлов
        files_graph[i+1] = line[1:]
    # удаляем n строк
    lines = lines[n:]
    
    # приводим к массиву int-ов
    error_files = list(map(int, lines[1].split()))

    # возращаем словарь зависимостей и список файлов с ошибками
    return files_graph, error_files


def solve(data):
    # парсим входные данные
    # получаем словарь зависимостей и список файлов с ошибками
    files_graph, error_files = parse_input(data)
    print(files_graph)
    print(error_files)

    # создаем словарь посещенных вершин для обхода графа
    # изначально все вершины не посещены - False
    # для этого исользуем функцию "dict.fromkeys"
    # dict.fromkeys принимает 2 параметра:
    #   1) список ключей, в нашем случае имена вершин
    #   2) значение по умолчанию, которое будет присвоено для каждого ключа
    visited = dict.fromkeys(files_graph.keys(), False)
    print(visited)

    # у нас уже есть список, содержащий плохие вершины - error_files
    # т.к в питоне список можно использовать как стек, то используем error_files, 
    # а не создаем новый стек как на уроке

    # условие цикла: заходим в цикл пока error_files не пустой
    # такая запись красивее и короче, чем "while len(error_files) == 0:"
    while error_files:
        # берем из стека текущую вешину
        current_file = error_files.pop()

        # если она была посещена, то ничего не делаем и переходим к следующей вершине (в начало цикла)
        if visited[current_file]:
            continue

        # в противном случае смотрим, в какие вершины графа можно перейти из текущей
        # и добавляем их в стек
        for file, depends_on in files_graph.items():
            if current_file in depends_on:
                error_files.append(file)

        # помечаем, что посетили текущую вершину
        visited[current_file] = True

    # закончили обход графа
    # печатаем результат
    result = sum(visited.values())
    print(result)


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

# data = '''1
# 0
# 1
# 1'''
# solve(data)