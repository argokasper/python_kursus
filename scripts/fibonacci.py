

n1, n2 = 0, 1

for n in range(1, 10):
    print(n1)
    nth = n1 + n2

    n1 = n2
    n2 = nth


def fibonacci(n1, n2):
    if (n1 < 100):
        print(n1)
        nth = n1 + n2
        n1 = fibonacci(n2, nth)

fibonacci(0, 1)