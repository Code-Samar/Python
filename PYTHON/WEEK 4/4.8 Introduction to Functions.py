def add(a, b):
    ans = a + b
    return ans

def sub(p, q):
    ans = p - q
    return ans

def discount(cost, d):
    ans = cost - (cost * d / 100)
    return ans

result = add(10 , 5) + add(discount(100, 10), sub(100, 5))
print(result)
