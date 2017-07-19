import matplotlib.pyplot as plt
import numpy as np
import os
os.system("clear")

x = np.linspace(0.0, 6.0, 50)
y = np.sin(x)
y1 = 1.0 / np.sin(x)

plt.figure(num=4, figsize=(7, 5))
plt.plot(x, y, color='red', linewidth=2.0, linestyle='--')
plt.plot(x, y1)

plt.yticks(
        [-3, 0, 4],
        ['low', 'midle', 'high above'] )

# gca = 'get current axis'
ax = plt.gca()

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))


plt.show()


