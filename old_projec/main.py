import cmath
import math
import matplotlib.pyplot as plt
import pygame
from pygame.locals import *
import numpy as np

#The initial location
start_x = 2.0
start_y = 5.0
#The goal location
end_x = 4.5
end_y = 6.5
#the link's length
l1 = 5.0
l2 = 4.0

#The slope of a straight line in an orthogonal complement
gradient = (end_y-start_y) / (end_x-start_x)

#x = np.arange(start_x, end_x+0.2, (end_x-start_x)/10)
x = np.linspace(2,4.5,10)
#reset parameter
y, c1, s1, c2, s2, D, r1, r2 = [0]*len(x), [0]*len(x), [0]*len(x), [0]*len(x), [0]*len(x), [0]*len(x), [0]*len(x), [0]*len(x)

for i in range(len(x)):
    y[i] = gradient*(x[i] - start_x) + start_y

for i in range(len(x)):
    c2[i] = (x[i] ** 2 + y[i] ** 2 - l1 ** 2 - l2 ** 2) / (2 * l1 * l2)
    if 1 - c2[i]**2 < 0:
        s2[i] = cmath.sqrt(1 - c2[i]**2)
    else :
        s2[i] = math.sqrt(1 - c2[i] ** 2)

#joint parameter
for i in range(len(x)):
    D[i] = np.linalg.det(
        [[l1+l2*c2[i], -l2*s2[i]],
         [ l2*s2[i], l1+l2*c2[i]]]
    )
    c1[i] = np.linalg.det(
        [[x[i], -l2*s2[i]],
         [y[i], l1+l2*c2[i]]])
    s1[i] = np.linalg.det(
        [[l1+l2*c2[i], x[i]],
         [l2*s2[i], y[i]]])

#radian value
for i in range(len(x)):
    if 1 - c2[i] ** 2 < 0:
        r1[i] = cmath.phase(complex(c1[i], s1[i]))
        r2[i] = cmath.phase(complex(c2[i], s2[i]))
    else:
        r1[i] = math.atan2(s1[i], c1[i])
        r2[i] = math.atan2(s2[i], c2[i])
print(r2)
#write graph
for i in range(len(x)):
    x_end_values = x[i]
    y_end_values = y[i]
    x_middle_values = l1*math.cos(r1[i])
    y_middle_values = l1*math.sin(r1[i])
    plt.plot([x_middle_values,x_end_values],[y_middle_values, y_end_values])
    plt.plot([0, x_middle_values], [0, y_middle_values])
plt.show()