# 文件读取

from sys import argv

script, filename = argv

# 打开文件
txt = open(filename, mode='r')

print("Here's your file %r:" % filename)
# 读取文件内容
print(txt.read())
print("Type the filename again:")
print(txt.tell())
txt.close()

# 用户输入文件名
file_again = input(">")
txt_again = open(file_again)
print(txt_again.read())
txt_again.close()
