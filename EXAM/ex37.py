# 复习
"""
关键词 del：删除数组中的一个或多个元素
del a[0] # 删除第0个元素
del a[2:4] # 删除从第2个元素开始，到第4个为止的元素。包括头不包括尾

global关键字主要作用是声明变量的作用域。
a = 5

def test():
    golbal a  #声明使用全局变量a
    a = 1

 with 语法用于简化资源操作的后续清除操作，是 try/finally 的替代方法
1.普通版

def test0():
    f = open("1.txt", "w")
    f.write("0000")
    f.close()1234

2.进阶版

def test1():
    f = open("1.txt", "w")
    try:
        f.write("111111")
    except Exception:
        print("ERROR")
    finally:
        f.close()12345678

3.高级版

def test2():
    with open("1.txt", "w") as f:
        f.write("2222")
---------------------
作者：老板来颗糖
来源：CSDN
原文：https://blog.csdn.net/lu13093323120/article/details/82195060
版权声明：本文为博主原创文章，转载请附上博文链接！

yield 生成器使用

exec 内置语句 返回值为None
isTrue = "True and True"
exec('print(isTrue)')

x = 10
expr = /"/"/"
z = 30
sum = x + y + z
print(sum)
/"/"/"
def func():
    y = 20
    exec(expr)
    exec(expr, {'x': 1, 'y': 2})
    exec(expr, {'x': 1, 'y': 2}, {'y': 3, 'z': 4})

func()

lambda表达式，通常是在需要一个函数，但是又不想费神去命名一个函数的场合下使用，也就是指匿名函数

add = lambda x, y : x+y
add(1,2)  # 结果为3
"""


