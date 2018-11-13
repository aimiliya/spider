# while-loop

i = 0
number = []

while i < 6:
    print("At the top i is %d" % i)
    number.append(i)

    i += 1
    print("numbers now: ", number)
    print("At the bottom i is %d" % i)


print("the numbers:")

for num in number:
    print(num)