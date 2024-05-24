# x *= 8
# x += 10
# x /= 2
# x -= 8

n = int(input())
n += 8
n *= 2
n -= 10
print('greska' if n % 8 > 0 else n // 8)
