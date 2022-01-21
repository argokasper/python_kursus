class Test:
 x = 5
 y = 6

 def __init__(self):
    # empty
    print('empty')

 def __str__(myclass):
     return 'Test={ x=' + str(myclass.x) + ', y=' + str(myclass.y) + ' }'

 def myfunction():
     return 'X'



test = Test()

test.x

print(test)

test.x = 10

print(test)





















from models.Course import Course

kursus1 = Course()
kursus1.name = 'Füüsika'

kursus2 = Course()
kursus2.name = 'Keeled'



kursus2.setGrades([5, 4, 3, 2, 1])

print(kursus1.grades)
print(kursus2.grades)




