def hello_print(n):
    # print("Hello " * n)
    for i in range(n):
        print("Hello ", end="")
    print()

def hello_str(n):
    return "Hello " * n

def abs(n):
    if n < 0:
        n *= -1
    return n

def max(x, y):
    if x > y:
        return x
    else:
        return y

def amount(proc, total):
    return total / 100 * proc

def money(deposit, monthly_income, tax, years):
    money = deposit
    for year in range(years):
        money += 12 * monthly_income
        money += money / 100 * tax
    return money

def fact(n):
    if n < 2:
        return 1
    fact = 1
    for i in range(2, n + 1):
        fact = fact * i
    return fact

print(fact(5))