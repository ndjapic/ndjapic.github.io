a, b = map(int, input().split("/"))
c, d = map(int, input().split("/"))

print("Разломци:", a, "/", b, " и ", c, "/", d);
print("Збир:", a*d+b*c, "/", b*d);
print("Разлика:", a*d-b*c, "/", b*d);
print("Производ:", a*c, "/", b*d);
print("Количник:", a*d, " /", b*c);
