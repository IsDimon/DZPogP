a = float(input("Введите сторону a: ")) 
b = float(input("Введите сторону b: ")) 
c = float(input("Введите сторону c: ")) 
 
if a + b > c and b + c > a and c + a > b:
    print('Трегольник существует')
    if a != b and b != c and c != a:
        print('Треугольник разносторонний')
    if a == b or b == c or c == a:
        print('треугольник является равнобедренным')
    if a == b == c:
        print('треугольник является равносторонним')
else:
    print('Такого треугольника не существует')
   