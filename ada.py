import time
import os

from sklearn.ensemble import *
import matplotlib.pyplot as plt
import numpy as np

ESTIMATORS = 50

x = [[5, 69], [-9, 68], [-21, 69], [-37, 50], [-51, 46], [-52, 20], [-39, 3], [-30, -19], [1, -40], [13, -51],
     [38, -56], [52, -52], [63, -24], [73, -18], [54, 48], [32, 58], [16, 53], [-4, 81], [-17, 69], [-47, 63],
     [-60, 59], [-62, 33], [-59, 0], [-42, -27], [-11, -39], [20, -60], [46, -53], [67, -53], [-13, 54], [-29, 77],
     [-26, 96], [-16, 80], [-17, 64], [-28, 47], [-36, 31], [-30, 2], [-23, -21], [-6, -18], [6, -16], [22, -41],
     [29, -22], [48, -18], [64, -14], [46, 1], [62, 15], [57, 26], [72, 44], [22, 52], [44, 67], [32, 69], [13, 57],
     [0, 39], [-9, 55], [-20, 35], [-20, 17], [-43, 21], [-21, -1], [-13, -27], [18, 93], [22, 77], [29, 61], [50, 75],
     [61, 72], [60, 59], [76, 50], [92, 36], [82, 27], [96, 8], [93, 1], [86, -8], [89, -20], [85, -36], [82, -52],
     [79, -55], [59, -74], [51, -59], [46, -41], [35, -57], [28, -76], [8, -75], [14, -57], [-13, -44], [-40, -41],
     [-39, -25], [-74, -25], [-69, 4], [-75, 29], [-69, 68], [-40, 70], [-38, 91], [-50, 90], [-54, 70], [10, 77],
     [5, 91], [-10, 99], [-8, 110], [28, 108], [39, 82], [63, 88], [82, 66], [67, 64], [107, 10], [-4, -57], [-23, -63],
     [-15, -36], [-49, -30], [-46, -13], [-28, -6], [-61, -6], [-66, -21], [-59, -41], [-72, -8], [-83, 31], [-72, 53],
     [-59, 49], [-48, 99], [0, 99]]
y = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0]
x = np.array(x)
y = np.array(y)
x1 = x[:, 0]
x2 = x[:, 1]
x_min = np.min(x1) - 10
x_max = np.max(x1) + 10
y_min = np.min(x2) - 10
y_max = np.max(x2) + 10


def draw_plane(clf):
    pass


plt.figure()

plot_colors = "br"
plot_step = 1
class_names = "AB"

xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step),
                     np.arange(y_min, y_max, plot_step))

plt.figure(1)
for i in range(1, ESTIMATORS):
    clf = AdaBoostClassifier(n_estimators=i)
    clf.fit(x, y)

    z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    z = z.reshape(xx.shape)

    plt.clf()
    cs = plt.contourf(xx, yy, z, cmap=plt.cm.Paired)
    plt.axis("tight")
    for class_value, class_name, class_color in zip(range(2), class_names, plot_colors):
        idx = np.where(y == class_value)
        plt.scatter(x[idx, 0], x[idx, 1],
                    c=class_color, cmap=plt.cm.Paired,
                    s=20, edgecolor='k',
                    label="Class %s" % class_name)

    plt.pause(0.3)
input("Press Enter to continue ...")