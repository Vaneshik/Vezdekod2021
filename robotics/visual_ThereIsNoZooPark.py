import matplotlib.pyplot as plt
import matplotlib.animation as animation


def init():
    ax.set_ylim(0, 10)
    ax.set_xlim(0, l)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,


l = int(input())
n = int(input())
coords = map(int, input().split())
mid = l / 2
left = []
right = []
time = 0
for i in coords:
    if i > mid:
        left.append(i)
    else:
        right.append(i)

fig, ax = plt.subplots()
line, = ax.plot([], [], '.r', markersize=15)
ax.grid()
room, = ax.plot([0, l, l], [2, 2, 0], 'k')
xdata, ydata = [], []
count = 0
ax.set_ylim(0, 10)
ax.set_xlim(0, l)


def run(data):
    global count, left, right, time
    if left or right:
        # print(left, right)
        # print()
        for i in left:
            if i < 0:
                left.pop(left.index(i))
        for i in right:
            if i > l:
                right.pop(right.index(i))

        xdata = []

        right = list(map(lambda x: x + 0.05, right))
        left = list(map(lambda x: x - 0.05, left))
        time += 0.05
        right_o = right.copy()
        left_o = left.copy()
        for i in right_o:
            for j in left_o:
                mid = (i + j) / 2
                if mid - 0.2 <= i <= mid + 0.2 and mid - 0.2 <= j <= mid + 0.2:
                    left_o[left_o.index(j)] = mid + 0.2
                    right_o[right_o.index(i)] = mid - 0.2

        for i in right_o:
            xdata.append(i)
        for i in left_o:
            xdata.append(i)
        ydata = [1] * (len(right) + len(left))
        # print()
        # print(xdata)
        # print(left, right)
        # print()
        # print(time)
        print(time)
        line.set_data(xdata, ydata)

    return line,


ani = animation.FuncAnimation(fig, run, interval=25, init_func=init)
plt.show()
'''
20
7
2 3 4 9 11 15 17
'''