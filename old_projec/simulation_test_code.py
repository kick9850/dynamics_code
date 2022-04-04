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
y, c1, s1, c2, s2, D, r1, r2, F_updatedX, F_updatedY = [0]*len(x), [0]*len(x), [0]*len(x), [0]*len(x), [0]*len(x), [0]*len(x), [0]*len(x), [0]*len(x), [0]*len(x), [0]*len(x)
S_updatedX, S_updatedY = [0]*len(x),[0]*len(x)

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

pygame.init()
length = 1200
height = 1200
srf = pygame.display.set_mode((length, height))
loopFlag = True
num = 0

while loopFlag:
    for event in pygame.event.get(QUIT):
        loopFlag = False

    print(num)
    srf.fill((255, 255, 255))

    F_updatedX[num] = length/2 + l1*math.cos(r1[num])
    F_updatedY[num] = height-10 + l1*math.sin(r1[num])
    S_updatedX[num] = length/2 + l1*math.cos(r1[num]) + l2*math.cos(r2[num])
    S_updatedY[num] = height-10 + l1*math.sin(r1[num]) + l2*math.sin(r2[num])

    pygame.draw.line(srf, (100, 100, 100), (length/2, height-100), (F_updatedX[num], F_updatedY[num]), 2)
    pygame.draw.circle(srf, (100, 100, 100), (int(F_updatedX[num]), int(F_updatedY[num])), 10, 0)

    pygame.draw.line(srf, (100, 100, 100), (F_updatedX[num], F_updatedY[num]), (S_updatedX[num], S_updatedY[num]), 2)
    pygame.draw.circle(srf, (100, 100, 100), (int(S_updatedX[num]), int(S_updatedY[num])), 10, 0)

    pygame.draw.line(srf, (0, 0, 0), (0, height-100), (length, height-100), 10)

    pygame.time.delay(40)
    pygame.display.flip()