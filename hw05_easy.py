# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

def makeDir(i):
    os.mkdir('{}'.format(i))

for r in range(9):
    makeDir('dir_{}'.format(r+1))


def removeDir(i):
    os.rmdir('{}'.format(i))

for r in range(9):
    removeDir('dir_{}'.format(r+1))


def chDir(i):# для задания normal
    os.chdir(i)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def inDir():
    print('{}'.format(os.listdir()))


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil
import sys


def copy_file(fileName, newFileName):
    shutil.copy(fileName, newFileName)
    print("Создан файл:\n",sys.argv[0]+"_1new")

# copy_file(sys.argv[0], sys.argv[0]+"_1new")