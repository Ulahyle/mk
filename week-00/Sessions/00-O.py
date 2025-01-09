numbers = [1, 2, 3, 4, 5]
sum = 0

for x in numbers:
    if x % 2 == 0:
        sum = sum + (x ** 2)
    

print(sum)
