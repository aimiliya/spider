my_name = "liuguosong"
my_age = 24
my_height = 170
my_weight = 60
my_eyes = 'Black'
my_teeth = "White"
my_hair = "Brown"

# %s 前后不应与字母等接触，容易出错
print("Let's talk about %s." % my_name)
print("He's %d inces tall" % my_height)
print("he's %d pounds heavy." % my_weight)
print('Actually that"s not too heavy.')
print("he's got %s eyes and %s hair" % (my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee" % my_teeth )

# this line is tricky,try to get it exactly right
print('If I add %d ,%d,and %d I get %d.'%(my_age,my_height,my_weight,my_age+my_height+my_weight))

