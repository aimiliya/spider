# 更多文件操作
# 命名时尽量不是有函数名作为变量名
from sys import argv
from os.path import exists  # exists这个命令，将文件名字符串作为参数，如果文件存在的话，它将返回 True，否则将返回 False

script, from_file, to_file = argv

print("Copying from %s to %s" % (from_file, to_file))

# We could do it these two on one line too, how?
input_file = open(from_file)
indata_file = input_file.read()

# indata = open(from_file).read()


print("The input file is %d betys long" % len(indata_file))

print("Does the output file exist? %r" % exists(to_file))
print("Ready, hit Return to continue, CTAL-C to about.")
input()

# !错误写法：将文件写入模式用大写字母写
output = open(to_file, 'w')
output.write(indata_file)

print("Alright, all done.")

output.close()
input_file.close()
