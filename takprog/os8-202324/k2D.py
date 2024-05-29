n = int(input())

d = 2
while d*d*d <= n:
    while n % (d*d) == 0:
        n //= d*d
    d += 1

print(n)
