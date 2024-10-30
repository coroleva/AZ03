import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(0,1,1000)

plt.bar(range(len(data)),(data))
plt.show()