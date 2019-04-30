# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.


line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'


import re
line_small = re.findall(r"[a-z]+", line)
print("Задание-1.1: \n Буквы в нижнем регистре, модуль re :", line_small)

#------
line_list = list(line)# преобразование строки в список


abc = "QWERTYUIOPLKJHGFDSAZXCVBNM"
abc_list = list(abc)# преобразование строки в список


for i, element1 in enumerate(line_list[:]):# замена больших букв на пробел
    for element2 in abc_list:
        if element1 == element2:
            line_list[i] = ' '


joinWord=''.join(line_list).split(' ')# объединение в слова элементов строки между которыми пробел

line_new = [i for i in joinWord if i != '']# удаление элементов пробел из списка
print('Задание-1.2: \nБуквы в нижнем регистре, БЕЗ модуля re :',line_new)

# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

import re
line_2_1 = re.findall(r'[a-z]{2}([A-Z]+)[A-Z]{2}', line_2)
print('Задание-2.1: \nБуквы в верхнем регистре, модуль re: ', line_2_1)

#------
line_list = list(line)# преобразование строки в список

ABC = "QWERTYUIOPLKJHGFDSAZXCVBNM"
ABC_list = list(ABC)# преобразование строки в список

abc = "qwertyuiopasdfghjklzxcvbnm"
abc_list = list(abc)# преобразование строки в список

lst = []
i = len(line_list) - 1

while i >= 0:# Ишем большую букву после которой стоят 2 большие буквы
       if line_list[i] in abc_list:
              lst.append(line_list[i])
       elif line_list[i] in ABC_list and i <= len(line_list) - 3 and line_list[i + 1] in ABC_list and line_list[
              i + 2] in ABC_list:
              lst.append(line_list[i])
       else:
              lst.append(' ')
       i -= 1

lst.reverse()  # Переворачиваем список

i = 0
lst2 = []
registr = True
while i <= len(lst) - 1:# фильтруем первоначанльный список
       if lst[i] in abc_list:
              registr = True
       if lst[i] in ABC_list and lst[i - 1] in abc_list and lst[i - 2] in abc_list:
              lst2.append(lst[i])
              registr = False
       elif lst[i] in ABC_list and registr == False:
              lst2.append(lst[i])
       else:
              lst2.append(' ')
       i += 1

joinWord = ''.join(lst2).split(' ')  # объединение в слова элементов строки между которыми пробел

line_2_2 = [i for i in joinWord if i != '']  # удаление элементов пробел из списка
print('Задание-2.2: \nБуквы в верхнем регистре, БЕЗ модуля re:', line_2_2)

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

from itertools import groupby
import random
import os


characters_in_number = 2500

digit = [random.randint(0, 9) for _ in range(characters_in_number)]# формироваие рандомного списка
digit = ''.join(list(map(lambda x: str(x), digit)))#преобраование списка [_,_] в число


path = os.path.join('files', 'text.txt')# путь к файлу
with open(path, 'w', encoding='UTF-8') as file:# Запись в файл
    file.write(str(digit))

with open(path, 'r', encoding='UTF-8') as file: #выгружаем из файла
    file_text = list(file.read())
print('Задание-3: \n2500-значное произвольное число из файла выгружено:', file_text)

from itertools import groupby
longDigit = max((list(g) for k, g in groupby(file_text)), key = len)
print("Максимальна последоватльность одинаковых", longDigit)
