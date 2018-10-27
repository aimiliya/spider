# input 输入中默认end="\n" 若不换行需要设置
print("How old are you?", end="")
age = input()
print("How tall are you?")
height = input()
print("How much do you weight?")
weight = input()

print("So, you're %r old, %r tall and %r heavy." % (age, height, weight))

