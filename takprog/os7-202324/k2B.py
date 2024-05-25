a = int(input())
b = int(input())
c = int(input())
d = int(input())

odg = 0
if a < c:
    odg = max(odg, c-a)
if b > d:
    odg = max(odg, b-d)

print(odg)
