# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
#  Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
#  *Верните все возможные варианты комплектации рюкзака.

things = {'Ложка': 1.0,
          'Вилка': 1.0,
          'Вода': 3.0,
          'Ботинки': 3.0,
          'Куртка': 5.0,
          'Камера':4.0,
          'Чайник': 4.0,
          'Палатка': 12.0,
          'Еда': 5.0,
          'Джинсы': 4.0,
          'Посуда': 5.0}
carrying = int(input("Введите грузоподъемность рюкзака: "))
knapsack = 0
pack = []
for name, weight in things.items():
    if knapsack + weight <= carrying:
        knapsack += weight
        pack.append(name)
pack.append(knapsack)
print(pack)
