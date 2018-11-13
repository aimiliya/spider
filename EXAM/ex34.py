"""
cardinal 基数

ordinal序数

序数是在基数的基础上再增加一层意思。

例如：

　　基数：一、二、三、四、五、六、七、八、九、十。

　　序数：第一、第二、第三、第四、第五、第六、第七、第八、第九、第十。

"""
animals = ['bear', 'tiger', 'penguin', 'zebra']

ordinal = 0
for animal in animals:
    order = ['1st', '2nd', '3rd', '4th']
    print("The %r animal is at %d ,and is a %s" % (order[ordinal], ordinal, animal))
    ordinal += 1
