# 1.	Дан список, состоящий из 4х элементов: ‘abc’, ‘xyz’, ‘aba’, ‘1221’.
#       Проверить для каждого элемента выполнение следующих условий:
#       элемента больше 2х и первый и последний символ у него совпадают.

my_list = ['abc', 'xyz', 'aba', '1221']

first_requirement = len(my_list[0]) > 2 and my_list[0][0] == my_list[0][len(my_list[0]) - 1]
print(first_requirement)

second_requirement = len(my_list[1]) > 2 and my_list[1][0] == my_list[1][len(my_list[1]) - 1]
print(second_requirement)

third_requirement = len(my_list[2]) > 2 and my_list[2][0] == my_list[2][len(my_list[2]) - 1]
print(third_requirement)

fourth_requirement = len(my_list[3]) > 2 and my_list[3][0] == my_list[3][len(my_list[3]) - 1]
print(fourth_requirement)
