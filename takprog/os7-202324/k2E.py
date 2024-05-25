n = int(input())

p = 2
while p*p <= n:
    while n % (p*p) == 0: n //= p*p
    p += 1

print(n)
