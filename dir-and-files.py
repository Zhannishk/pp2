import pathlib
import os
from string import ascii_uppercase

path = '..'

# task 1
print("Task 1")
def listDirs(p):
    print([x.name for x in os.scandir(path = p) if x.is_dir()])


def listFiles(p):
    print([x.name for x in os.scandir(path = p) if x.is_file()])


def listDirsAndFiles(p):
    print([x.name for x in os.scandir(path = p)])
listDirs(path)
listFiles(path)
listDirsAndFiles(path)

# task 2
print('Task 2')
def check(p):
    exist_status = os.access(path = p, mode = os.F_OK)
    print(f'Existence : {exist_status}')
    read_status = os.access(path = p, mode = os.R_OK)
    print(f'Readibility : {read_status}')
    write_status = os.access(path = p, mode = os.W_OK)
    print(f'Writability : {write_status}')
    exec_status = os.access(path = p, mode = os.X_OK)
    print(f'Executability : {exec_status}')
check(path)

# task 3
print("Task 3")
def test(p):
    exist_status = os.access(path = p, mode = os.F_OK)
    if exist_status:
        print(f'File: {os.path.basename(p)}')
        print(f'Directory: {os.path.dirname(p)}')
    else:
        print("The file does not exist")
print()
test('TSIS6/smth.txt')

# # task 4
# print("Task 4")
# def count(p):
#     f = open(p, 'r')
#     cnt = 0
#     for i in f:
#         cnt += 1
#     return cnt
# print()
# print(f'Number of lines = {count("TSIS6/smth.txt")}')

# task 5
print("Task 5")
def show(fname, l):
    f = open(fname, "a")
    f.write(str(l))
    f.close()

    f = open(fname, "r")
    print(f.read())
print()
l = str(input())
show('TSIS6/smth.txt', l)

# task 6
print("Task 6")
def generateFiles():
    for char in ascii_uppercase:
        file = open(f'./files/{char}.txt', 'x')
        file.close()
print()
generateFiles()

# task 7
print("Task 7")
def copyContent(i, t):
    init_file = open(i, 'r')
    file_content = init_file.read()
    init_file.close()

    target_file = open(t, 'w')
    target_file.write(str(file_content))
    target_file.close()
    print('Successfully copied')

    target_file = open(t, 'r')
    print(target_file.read())
    target_file.close()
print()
copyContent('smth.txt', 'smth1.txt')

# task 8
print("Task 8")
def delete(p):
    os.remove(p)
print()
delete("smth1")