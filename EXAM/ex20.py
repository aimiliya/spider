from sys import argv

script, input_file = argv


# 打印读取到的文件内容
def print_all(f):
    print(f.read())


def rewind(f):
    # seek() 方法用于移动文件读取指针到指定位置
    f.seek(0)


# 打印一行的文件内容
def print_a_line(line_count, f):
    print(line_count, f.readline())


# 当前打开的文件
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("let's print three lines:")

# 记录当前行
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line,current_file)
