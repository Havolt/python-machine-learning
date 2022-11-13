# Data Distribution

import numpy as np
import matplotlib.pyplot as plt

randomNums = np.random.uniform(0.0, 5.0, 100000)

plt.hist(randomNums, 100)
plt.show()