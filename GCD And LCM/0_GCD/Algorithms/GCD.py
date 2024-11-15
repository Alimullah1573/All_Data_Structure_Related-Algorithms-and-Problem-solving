def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = 15
num2 = 10
result = gcd(num1, num2)
print(f"{num1} and {num2} Of GCD To {result}")