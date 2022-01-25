import numpy as np

# list = np.arange(6)
# print(list)
# print(type(list))

# for x in list:
#     print(x)


# a = np.arange(6)
# a2 = a[np.newaxis, :]
# print(a2.shape)

range = np.arange(10)
summa = range.sum()
print(summa)


x = [1, 2, 3, 4, 5, 56, 4, 3, 2, 2, 2]
print(np.unique(x))
print(np.flip(x))