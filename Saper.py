S, V, C = (int(i) for i in input().split())  # Ввод ширина на высоту и кол-во мин
a = [[0 for j in range(V)] for i in range(S)]  # Заполнили наше поле 0

for i in range(C):  # Перебираем кол-во мин
    rw, cw = (int(i) - 1 for i in input().split())  # Записываем строку и столбец одной мины при каждом проходе
    a[rw][cw] = -1  # Записываем мину по координатам столбца и колонны

for i in range(S):  # Перебираем строки
    for j in range(V):  # Перебираем столбцы
        if a[i][j] == 0:  # Если ячейка без мины
            for qi in range(-1, 2):  # Перебираем соседние строки
                for qj in range(-1, 2):  # Перебираем соседние столбцы
                    ai = qi + i  # Кординаты по строке
                    aj = qj + j  # Кординаты по столбцу
                    if 0 <= ai < S and 0 <= aj < V and a[ai][aj] == -1:  # Проверка вхождения в диапазон и мины по соседству
                        a[i][j] += 1
# Далее меняем значения на удобное чтение
for i in range(S):
    for j in range(V):
        if a[i][j] == -1:
            print('*', end='')
        elif a[i][j] == 0:
            print(0, end='')
        else:
            print(a[i][j], end='')
    print()
