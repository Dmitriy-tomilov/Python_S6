# 39. Даны два массива чисел. Требуется вывести те элементы первого массива 
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. 
# Пользователь вводит число N - количество элементов в первом массиве, 
# затем N чисел - элементы массива. Затем число M - количество элементов во втором 
# массиве. Затем элементы второго массива

# ___________________________________________________________
# n = int (input("Количество элементов: "))
# list = []
# for i in range (n):
#     list.append(input("элемент: "))
# m = int (input("Количество элементов: "))
# list_1 = []
# for i in range(m):
#     list.append(input("элемент: "))
# result = []
# for i in list:
#     if i not in list_1:
#         result.append(i)
# print(result)
# _____________________________________________________________

n = int(input())
list_first = list()
for i in range(n):
    x = int(input())
    list_first.append(x)
m = int(input())
list_second = list()
for i in range(m):
    x = int(input())
    list_second .append(x)
count = 0
for i in range(n):
    for j in range(m):
        if list_first[i] == list_second[j]:
            count += 1
    if count != 0:
        print(list_first[i])
count = 0