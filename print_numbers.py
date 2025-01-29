for i in range(1, 11):
    print(i)

a, b = 0, 1
for _ in range(10):
    print(a)
    a, b = b, a + b
