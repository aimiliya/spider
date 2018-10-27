# 参数，解包，变量

from sys import argv
# sys.argv: 实现从程序外部向程序传递参数
# 在run的edit config 中进行传参，每个参数间用空格隔开
# 变量不足时会报错
# 且第一个变量是不能自定义的
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is :", first)
print("Your second variable:", second)
print("your third cariable:", third)

# argv 与 input是两个独立的模块属性
who_first = input("who" + " " + argv[1])
# 可以联合使用
argv[0] = input("who first")
print(argv)
