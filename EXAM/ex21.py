# 函数返回值
# 实现加法
def add(a, b):
    print("ADDING %d + %d" % (a, b))
    return a + b


# 实现减法
def subtract(a, b):
    print("SUBTRACTING %d - %d " % (a, b))
    return a - b


# 实现乘法
def multiply(a, b):
    print("MULTIPLY %d * %d" % (a, b))
    return a * b


# 实现除法
def divide(a, b):
    print("DIVIDING %d / %d" % (a, b))
    return a / b


print("Let's do some math with just functions")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: %d,Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))


# A puzzle foe the extra credit, type it in anyway.
print("Here is a puzzle.")

# 函数嵌套使用
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes:", what, "Can you do it by hand?")


what_again = divide(age, multiply(height, subtract(weight, add(age, 2))))
