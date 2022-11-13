import numpy as np
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

mean = np.mean(speed)
median = np.median(speed)
mode = stats.mode(speed)
standardDeviation = np.std(speed)
variance = np.var(speed)

print(mean, 'mean')
print(median, 'median')
print(mode, 'mode')
print(standardDeviation, 'standardDeviation')
print(variance, 'variance')