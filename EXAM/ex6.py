# 格式化输入整形
x = "There are %d types of people." % 10
# 定义变量
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# 输出变量
print(x)
print(y)

# 输出字符串
print("I said :%r." % x)
print("I also said: %s." % y)

# 定义布尔变量
hilarious = False
joke_evaluation = "Isn't that joke so funny?！% r"

print(joke_evaluation % hilarious)

w = "This is the left side of ..."
e = "a string with a right side."
# + 号重载输出
print(w + e)
