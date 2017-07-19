import matplotlib.pyplot as plt
import numpy as np
import os
os.system("clear")

x = np.linspace(0.0, 6.0, 50)
y = np.sin(x)
y1 = 1.0 / np.sin(x)

plt.figure()
plt.plot(x, y)


plt.figure()
plt.plot(x, y1)

plt.figure(num=4, figsize=(7, 5))
plt.plot(x, y, color='red', linewidth=2.0, linestyle='--')
plt.plot(x, y1)

plt.show()

