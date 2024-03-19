zn = [[3, 1], [3, 2], [3, 1], [10, 3], [4, 4]]
sum, cnt = 0
for item in zn:
    cnt += item[0]
    sum += item[1] * item[0]

print("Aritmetický průměr je: ", sum /cnt)