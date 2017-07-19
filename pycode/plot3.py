import numpy as np
from pylab import *
cls()

figure(figsize=(8,6), dpi=80)

subplot(2,1,1)
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)
plot(X,C)

subplot(2,1,2)
plot(X,S, color='red', linewidth=3.0, linestyle='--')

xlim(-4.0, 4.0)
xticks(np.linspace(-4,4,17, endpoint=True))

ylim(-1.6, 1.6)

show()

