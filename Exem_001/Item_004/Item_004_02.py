# 2.	Дан список цветов: ‘red’, ‘green’, ‘white’, ‘black’, ‘pink’, ‘yellow’.
#       Создайте еще один список и переместите в него 1-ый, 5-ый и 6-ой элементы.

colors = ['red', 'green', 'white', 'black', 'pink', 'yellow']

colors_spec = list()
colors_spec.extend([colors[0], colors[4], colors[5]])

print(f'Первый список {colors}, \nвторой список {colors_spec}')
