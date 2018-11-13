# 列表的操作
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there's not 10 thingd in that list. let's fix that.")


# 对字符串进行分割，存入列表
stuff = ten_things.split(" ")

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print("There's %d items now." % len(stuff))

print("There we go: ", stuff)

print(stuff[1])
print(stuff[-1])  # whoal fancy
print(stuff.pop())
print(" ".join(stuff))  # what? cool!
print('#'.join(stuff[3:5]))  # super stellar!