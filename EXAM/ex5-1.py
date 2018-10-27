name = "liuguosong"
age = 24
height = 170.0
weight = 60.0
eyes = 'Black'
teeth = "White"
hair = "Brown"

# %s 前后不应与字母等接触，容易出错
print("Let's talk about %s." % name)
#用%格式化输出时只能进行整数运算
#format（）格式化输出时可以进行多数字变量类型的运算
print("He's{} inces tall".format(height*30.48))
print("he's {} pounds heavy.".format(weight*0.45))
print('Actually that"s not too heavy.')
print("he's got %r eyes and %s hair" % (eyes, hair))
print("His teeth are usually %s depending on the coffee" % teeth )

# this line is tricky,try to get it exactly right
print('If I add %r ,%d,and %d I get %d.'%(age,height,weight,age+height+weight))