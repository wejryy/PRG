def fibrek(n):
    a = 0
    b = 1 
    if n <= 1: return n
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
    return b
    
print(fibrek(50))
