import random
import numpy as np
import collections

while True:
    n = int(input("Задайте розмір суміжної матриці [5-100]: "))
    if 5<=n<=100:
        break

matrix = np.random.randint(0,2,size=(n,n))
print('\n')
for i in range(0, n):
    for j in range(0, i+1):
        if i == j:
            matrix[i][j] = 0
        else:
            matrix[i][j] = matrix[j][i]

print('Матриця суміжності: \n{}\n'.format(matrix))

graph ={}
for i in range(n):
    ls = []
    for j in range(n):
        if matrix[i][j] == 1:
            ls.append(j)
    graph[i] = set(ls)

def bfs(graph, start, end):
    visited, queue = set(), collections.deque([(start, [start])])
    visited.add(start)
    while queue:
        (vertex, path) = queue.popleft()
        for neighbour in graph[vertex] - set(path):
            if neighbour not in visited:
                if neighbour == end:
                    yield path + [neighbour]
                else:
                    visited.add(neighbour)
                    queue.append((neighbour, path + [neighbour]))

def shortest_path(graph, start, end):
    try:
        return next(bfs(graph, start, end))
    except StopIteration:
        return None

distance = np.random.randint(0,1,size=(n,n))
for i in range(0, n):
    for j in range(0, i+1):
        if i == j:
            distance[i][j] = 10**9
        else:
            if shortest_path(graph, i, j) == None:
                distance[i][j] = 10**9
                distance[j][i] = distance[i][j]
            else:
                ls = len(list(shortest_path(graph, i, j)))
                if ls == 0:
                    distance[i][j] = 10**9
                    distance[j][i] = distance[i][j]
                else:
                    distance[i][j] = ls - 1
                    distance[j][i] = distance[i][j]

print('Матриця відстані: \n{}\n'.format(distance))
print('Перевірити для двох точок')
while True:
    i = int(input('Початкова точка [0 - {}]: '.format(n)))
    j = int(input('Початкова точка [0 - {}]: '.format(n)))
    print('\n')
    print('Найкоротший шлях: {}\nДовжина шляху: {}\n'.format(list(shortest_path(graph, i, j)),len(list(shortest_path(graph, i, j)))-1))
