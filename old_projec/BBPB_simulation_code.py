import math
import numpy as np
import matplotlib.pyplot as plt

#목표 위치/초기 위치는 기존과제와 동일하게 진행하고, 가속도는 임의로 정해서 진행했습니다.
#Setting values
a = 0.5

l1 = 5.0
l2 = 4.0

l1_r0 = 0.4028228148634954
l1_rf = 0.5244535115942187
l2_r0 = 1.8754889808102941
l2_rf = 1.0033266997205754

#l1/l2 link get time's
tf = math.sqrt(4*(l1_rf - l1_r0)/a**2)
tb = tf/2
t = np.linspace(0, tf, 60)
print(t)
#reset parameter
Fr, Sr, Fdetr, Sdetr, Fdet2r, Sdet2r = [0]*len(t), [0]*len(t), [0]*len(t), [0]*len(t), [0]*len(t), [0]*len(t)
all_Location, all_vector, all_acceleration = [0]*len(t), [0]*len(t), [0]*len(t)

#l1 calculation
for i in range(len(t)):
    if len(t)/2 > i:
        Fr[i] = l1_r0 + (1/2)*a*t[i]**2
        Fdetr[i] = a*t[i]
        Fdet2r[i] = a
    else:
        Sr[i] = l1_rf - (1/2)*a*(tf-t[i])**2
        Sdetr[i] = -a*(tf-t[i])
        Sdet2r[i] = -a
for i in range(len(t)):
    all_Location[i] = Fr[i] + Sr[i]
    all_vector[i] = Fdetr[i] + Sdetr[i]
    all_acceleration[i] = Fdet2r[i] + Sdet2r[i]

for i in range(len(t)):
    if i > 0:
        #location
        plt.plot([t[i-1],t[i]],[all_Location[i-1],all_Location[i]], 'r')
        # vector
        plt.plot([t[i-1],t[i]],[all_vector[i-1],all_vector[i]], 'g')
        # acceleration
        plt.plot([t[i-1],t[i]],[all_acceleration[i-1],all_acceleration[i]], 'b')
#l2 calculation
for i in range(len(t)):
    if len(t)/2 > i:
        Fr[i] = l2_r0 + (1/2)*a*t[i]**2
        Fdetr[i] = a*t[i]
        Fdet2r[i] = a
    else:
        Sr[i] = l2_rf - (1/2)*a*(tf-t[i])**2
        Sdetr[i] = -a*(tf-t[i])
        Sdet2r[i] = -a
for i in range(len(t)):
    all_Location[i] = Fr[i] + Sr[i]
    all_vector[i] = Fdetr[i] + Sdetr[i]
    all_acceleration[i] = Fdet2r[i] + Sdet2r[i]

for i in range(len(t)):
    if i > 0:
        #location
        plt.plot([t[i-1],t[i]],[all_Location[i-1],all_Location[i]], linestyle = ':', color = 'y')
        # vector
        plt.plot([t[i-1],t[i]],[all_vector[i-1],all_vector[i]], linestyle = ':',color = 'g')
        # acceleration
        plt.plot([t[i-1],t[i]],[all_acceleration[i-1],all_acceleration[i]], linestyle = ':',color = 'b')
plt.show()