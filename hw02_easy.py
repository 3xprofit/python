# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
print("Задача 1")
fruit = ["яблоко", "банан", "киви", "арбуз"]
last_fruit = len(fruit)
print("Исходный список ", fruit)
print("Список в результате действий:")
for i in range(last_fruit):
    print(str(i + 1) +".", "{:>6}".format(fruit[i]))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
print("\nЗадача 2")
list1 = {"1", "яблоко", "3", "груша"}
list2 = {"2", "3", "4", "груша"}

list = list1 - list2

print("Список 1", list1)
print("Список 2", list2)
print("Список 1-2",list)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
print("\nЗадача 3")
list_old = [4, 23, 12, 34, 7, 16]
list_new = []
last_num = len(list_old)
for i in range(last_num):
    if list_old[i] % 2 == 0:
        list_new.append(list_old[i] / 4)
    else:
        list_new.append(list_old[i] * 2)
print("Исходный список ", list_old)
print("Список в результате действий ", list_new)
