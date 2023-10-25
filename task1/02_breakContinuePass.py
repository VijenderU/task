# 1 
for i in range(100):
    if i == 8:
        break
    print(i)

# prints all the numbers from 0 to 10 except multiples of 3
for i in range(11):
    if i % 3 == 0:
        continue
    print(i)

# prints all the even numbers from 0 to 10 (use pass).

for i in range(11):
    if i % 2 != 0:
        pass
    else:
        print(i)

# prints all the odd numbers from 0 to 10 (use pass).
for i in range(11):
    if i % 2 == 0:
        pass
    else:
        print(i)