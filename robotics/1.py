import matplotlib.pyplot as plt
from math import radians, pi

a = ''
with open('data.txt') as f:
    a = f.read()
a = a.replace('][', ', ')[2:-2]
print(a.split('), ('))
a = list(map(float, ', '.join(a.split('), (')).split(', ')))
print(a)
theta = []
r = []
for i in range(len(a)):
    if (i - 1) % 3 == 0:
        theta.append(radians(a[i]))
    elif (i - 2) % 3 == 0:
        if a[i] > 4000:
            r.append(4000)
        elif a[i] < 5:
            r.append(5)
        else:
            r.append(a[i])
print(theta)
print(r)
plt.polar(theta, r, '.', markersize=1)
# plt.polar(theta, r)
plt.axis([0, 2 * pi, 5, 4000])
plt.savefig('laser_ThereIsNoZooPark.png')
plt.show()
