numbers = []
for i in range(50):
    if i % 2 == 0 and i % 3 == 0:
        numbers.append(i * i)
print(numbers)

print([i**2 for i in range(50) if i % 2 == 0 and i % 3 == 0])
