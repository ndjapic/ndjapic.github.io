n = int(input())
a = [int(input()) for i in range(n)]
x = (sedista // 2 for sedista in a)
print(sum(x))

# 258 // 10 = 25
# 258 / 10 = 25.8
# 258 % 10 = 8
