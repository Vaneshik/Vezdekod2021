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
while left and right:
    for i in left:
        if i < 0:
            left.pop(left.index(i))
    for i in right:
        if i > l:
            right.pop(right.index(i))
    minn = 10 ** 5
    left.sort()
    right.sort()
    right.reverse()
    for i in left:
        for j in right:
            if j < i:
                if 0 < i - j < minn:
                    minn = i - j
    if minn == 10 ** 5:
        time += max(max(left), l - min(right))
        break
    left = list(map(lambda x: x - minn / 2, left))
    right = list(map(lambda x: x + minn / 2, right))
    time += minn / 2
print(int(time))
