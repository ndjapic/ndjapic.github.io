n = int(input())
k = int(input())

if n < 5:
    karta = 0
if 5 <= n <= 12:
    karta = 2800
if 13 <= n <= 64:
    karta = 3500
if n >= 65:
    karta = 3200

platiti = k * karta
if k > 10:
    platiti -= (k-10) * karta // 2
print(platiti)
