import numpy as np

import matplotlib.pyplot as plt
x = np.linspace(0,10)
y = x**2

p1 = [1,20]
p2 = [6,70]

plt.plot(x, y)
newline(p1,p2)
plt.show()