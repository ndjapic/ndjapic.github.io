# p z m k
p = int(input())
z = int(input())
m = int(input())
k = int(input())

prevezao = p
while prevezao >= k:
    prevezao -= k
    print('pera')

prevezao += z
while prevezao >= k:
    prevezao -= k
    print('zika')

prevezao += m
while prevezao >= k:
    prevezao -= k
    print('mika')
