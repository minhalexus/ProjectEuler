sum = 0
for i in range (0,1000,5):
    sum += i

for i in range(0,1000,3):
    if (i % 5 != 0):
        sum += i

print(sum)
