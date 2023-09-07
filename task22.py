from random import randint

n = input('Введите количество элементов первого множества: ')
n = set(randint(1, 20) for i in range(int(n)))
print(n)
m = input('Введите количество элементов второго множества: ')
m = set(randint(1, 20) for i in range(int(m)))
print(m)
n_m_sorted_set = n.intersection(m)
print(sorted(n_m_sorted_set))