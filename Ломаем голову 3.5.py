#Даны два файла, в каждом из которых находится запись многочлена.
#Задача - сформировать файл, содержащий сумму многочленов.

list1 = ['1 ','2 ','3 ','5 ']
list2 = ['7 ','8 ','9 ','4 ']
n = -1
data = open('file1.txt', 'w')
data.writelines(list1)

data = open('file2.txt', 'w')
data.writelines(list2)

data = open('file3.txt', 'w')
while (n <= len(list1)):
    n += 1
    sum = list1[n] + list2[n]
    data.writelines(sum)

data.close()
data.close()
data.close()