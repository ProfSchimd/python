# Un parametro 'n' -> 0, 1, 2, ..., n-1
print("range(10)")
for i in range(10):
    print(i)

print()
print("range(5,10)")
# Due parametri 'm' e 'n' -> m, m+1, m+2, ..., n-1
for i in range(5,10):
    print(i)

print()
print("range(0,100,10)")
# Tre parametri 'm', 'n' e 'k' -> m, m+k, m+k+k, ...
for i in range(0, 100, 10):
    print(i)