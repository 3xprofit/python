# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    # pass
    a = 1
    b = 1
    list = [1, ]

    for i in range(m):
        a, b = b, a + b
        list.append(a)

    return list[n - 1:m]


print(fibonacci(1, 10))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):

    n=len(origin_list)
    m=n-1
    while m>0:
        for i in range(m):
            if (origin_list[i]>origin_list[i+1]):
                x=origin_list[i]
                origin_list[i]=origin_list[i+1]
                origin_list[i+1]=x
        m=m-1
    print(origin_list)
sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def filter_func(function, list):
    return (item for item in list if function(item))

print(list(filter_func(lambda x: True if x > 5 else False, [2, 10, -10, 8, 2, 0, 14])))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

#нужно проверить проверить равенство противоположных сторон.
def parallelogram(A1, A2, A3, A4):
    if (abs(A3[0] - A2[0]) == abs(A4[0] - A1[0])) and (abs(A2[1] - A1[1]) == abs(A3[1] - A4[1])):
        return True
    return False
print(parallelogram([1,2], [2,3], [4, 5], [6, 7]))