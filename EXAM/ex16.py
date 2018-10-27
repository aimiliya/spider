# 读写文件
"""
 close – 关闭文件。跟你编辑器的 文件->保存.. 一个意思。
 read – 读取文件内容。你可以把结果赋给一个变量。
 readline – 读取文本文件中的一行。
 truncate – 清空文件，请小心使用该命令。
 write(stuff) – 将 stuff 写入文件 接受一个字符串作为参数。

"""

from sys import argv

# 进行解包
script, filename = argv

# 打印提示信息
print("We're going to erase %r." % filename)
print("if you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# 输入操作类型
input("?")

print("Opening the file...")
target = open(filename, "w")

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# 将输入的数据写入
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
target.write("%r\n%r\n%r" % (line1, line2, line3))

print("And finally, we close it.")
target.close()



