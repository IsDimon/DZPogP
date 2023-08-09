
#Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.

import random 
spisok = [random.randint(0,10) for _ in range(15)]
print(spisok)
new_spisok = []
for i in set(spisok):
    if spisok.count(i) != 1:
        new_spisok.append(i)
print(new_spisok)        
