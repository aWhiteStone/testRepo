#coding:utf-8

import numpy as np
import matplotlib.pyplot as plt

x_data = np.linspace(-1,1,300) [:, np.newaxis]   # [:,np.newaxis] make row vector transform column vector
noise = np.random.normal(0, 0.05, x_data.shape) 
y_data = np.square(x_data) - 0.5 + noise

fig=plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x_data,y_data)
plt.xlabel('x_data')
plt.ylabel('y_data')
plt.show()
