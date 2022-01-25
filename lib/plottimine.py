import matplotlib.pyplot as plt
import numpy as np

# x_coords = [0, 6]
# y_coords = [0, 250]

# # (0, 0)
# # (6, 250)

# plt.plot(x_coords, y_coords)

# plt.show()


x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()