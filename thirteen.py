cnt = 0
iter = 0
for a in range(0, 2):
    for b in range(a + 1, 4):
        for c in range(b + 1,6 ):
            for d in range(c + 1, 10):
                if a + b + c + d == 13:
                    print(f"{a}{b}{c}{d}")
                    cnt += 1 
                iter += 1 

print(f"{cnt}/{iter}")
print("-------")


