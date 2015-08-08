# Project Euler - 05
# https://projecteuler.net/problem=5
# smallest multiple

def gcd(a,b):
    while b:
        a, b = b, a%b
    return a

def lcm(a,b):
    return a * b / gcd(a,b)

def smallest(n):
    for i in range(1, n):
        n = lcm(n, i)
    return n

print smallest(20)