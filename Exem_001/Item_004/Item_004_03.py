# 3.	Даны несколько списков: [-8, 1, 2, -2, 0], [1, 1, 0, 0, 2, -2, -2], [1, -1, 0, -9, 4, -5], [1, 4, 0, 23, 6, 34].
#       Для каждого из списков найти второе наименьшее значение в нем (правильные ответы выделены жирным шрифтом).

my_list = [[-8, 1, 2, -2, 0], [1, 1, 0, 0, 2, -2, -2], [1, -1, 0, -9, 4, -5], [1, 4, 0, 23, 6, 34]]

s1 = sorted(set(my_list[0]))
s2 = sorted(set(my_list[1]))
s3 = sorted(set(my_list[2]))
s4 = sorted(set(my_list[3]))

print(f'Первый минимум {s1[1]}, второй минимум {s2[1]}, третий минимум {s3[1]}, четвертый минимум {s4[1]}')