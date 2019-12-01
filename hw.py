import numpy as np

n, m, k = list(map(int, str(input()).split(" ")))
classes = list(map(int, str(input()).split(" ")))
arange = np.arange(n)
data = np.array([np.array(classes), arange], np.int32)


