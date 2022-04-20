a = int(input("Введите ваше число: "))
b = int(input("Введите ваше число: "))
c = int(input("Введите ваше число: "))
if  a > b and a > c:
    print(a, '>')
if  c > a and c > b:
    print(c, ">")
if b > c and  b > a:
    print(b,' >')
if a < b and a < c:
    print(a, "<")
if b < a and b < c:
    print(b, "<")
if c < a and c < b:
    print(c, "<")


