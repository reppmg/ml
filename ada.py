import time
import os

from sklearn.ensemble import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("geyser.csv")

x = data.iloc[:, :-1].to_numpy()
y = data.iloc[:, -1].to_numpy()
y = LabelEncoder().fit_transform(y)

ESTIMATORS = 50

x1 = x[:, 0]
x2 = x[:, 1]
x_min = np.min(x1) - 1.1
x_max = np.max(x1) * 1.1
y_min = np.min(x2) * 0.9
y_max = np.max(x2) * 1.1

plot_colors = "br"
plot_step = 0.1
class_names = "AB"

xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step),
                     np.arange(y_min, y_max, plot_step))

plt.figure(1)
plt.pause(20)
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