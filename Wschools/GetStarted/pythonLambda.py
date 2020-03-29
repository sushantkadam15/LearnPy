x = lambda a: a+10
print(x(5))

cal = lambda a, b, c: a + b + c
print(cal(5,3,8))

def met(n):
    return lambda a : a * n

lam = met(6)
print(lam(6))