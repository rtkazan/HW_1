from random import randint

berry_list = list(randint(1, 5) for i in range(int(input('Введите количество кустов: '))))
print(berry_list)
tree = int(input('Введите номер куста: '))
result = 0
if tree == 1:
    result = berry_list[0] + berry_list[1] + berry_list[-1]
elif tree == len(berry_list):
    result = berry_list[-2] + berry_list[-1] + berry_list[0]
else:
    result = berry_list[tree - 1] + berry_list[tree - 2] + berry_list[tree]
print(result)