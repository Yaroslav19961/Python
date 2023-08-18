# 1) Создать переменную типа String
# 2) Создать переменную типа Integer
# 3) Создать переменную типа Float
# 4) Создать переменную типа Bytes
# 5) Создать переменную типа List
# 6) Создать переменную типа Tuple
# 7) Создать переменную типа Set
# 8. Создать переменную типа Frozen set
# 9) Создать переменную типа Dict

a1 = "Hello"
a2 = 10
a3 = 10.5
a4 = b"123456789"
a5 = [1, 2, 3, "world"]
a6 = (9, 8, 7, 6)
a7 = {1, 3, 4, 6, 7, 9, 10}
a8 = frozenset('qwerty')
a9 = {
    "Hello": "Привет",
    "World": "Мир"}

# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.

print(a1, type(a1))
print(a2, type(a2))
print(a3, type(a3))
print(a4, type(a4))
print(a5, type(a5))
print(a6, type(a6))
print(a7, type(a7))
print(a8, type(a8))
print(a9, type(a9))

# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.

x1 = "London"
x2 = "Tokyo"
x3 = x1 + x2

print(x3)

# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую).

s = "HI"
i = 100
result = str(i), str(s)

print(result)

# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)

result2 = str(i) + str(s)

print(result2)
