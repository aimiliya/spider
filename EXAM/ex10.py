# 转义字符及引号练习
"I am 6'2\ tall."  # 将字符串中的双引号转义
'I an 6\2" tall'  # 将字符串中的单引号

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat."

# 三个单引号与三个双引号使用效果相同
fat_cat = ("\n"
           "T'll do a list:\n"
           "\t* Cat food \n"
           "\t* Fishies \n"
           "\t* Catnip\n\t* Grass \n")
fat_cat_two = ('\n'
               'T\'ll do a list:\n'
               '\t* Cat food \n'
               '\t* Fishies\n'
               '\t* Catnip\n\t* Grass\n')

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print(fat_cat_two)
# %r%s打印三单双引号无区别
# %r 打印出来的是你写在脚本里的内容，而 %s 打印的是你应该看到的内容
print("%r\n%s" % (fat_cat, fat_cat))
print("%r\n%s" % (fat_cat_two, fat_cat_two))

