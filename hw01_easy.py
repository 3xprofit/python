__author__ = 'Чепурной Юрий Викторович'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# код пишем тут...
numeric = str(input("Введите многозначное число: "))
#numeric = str(956)
for digit in numeric:
    print(digit)



# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

word1 = input("Введите переменную А: ")
word2 = input("Введите случайную B: ")

print('A =',word1, 'B =',word2)
word3 = word1
word1 = word2
word2 = word3
print('A =',word1, 'B =',word2)
# word1, word2 = word2, word1


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = int(input("Указите Ваш возраст: "))
if age >= 18:
    print("Доступ разрешен")
else:
    print("Извините, пользование данным ресурсом только с 18 лет")

