# s = (a+b+c)/2
# area = √(s(s-a)*(s-b)*(s-c)) # ruutjuur **0.5, sqrt(9)=3 == 9**0.5 = 3

a = float(input('a= '))
b = float(input('b= '))
c = float(input('c= '))


s = (a + b + c) / 2

area = (s*(s-a)*(s-b)*(s-c))**0.5

print(area)