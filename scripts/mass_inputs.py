import random

def randomInputs(function, runs = 100):
    for i in range(runs):
        a = random.randint(0, 20)
        b = random.randint(0, 20)
        print('a={0}, b={1} vastus={2}'.format(a, b, function(a, b)))
