n = 2999
je_prvocislo = True
for i in range(2, n, 1):
    if n % i == 0:
        je_prvocislo = False
        break
if je_prvocislo:
    print(n, "je prvocislo")
else:
    print(n, "neni prvocislo")