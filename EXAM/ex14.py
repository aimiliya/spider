from sys import argv

script, user_name = argv
# 将用户提示符设置为变量 prompt
prompt = '>'

print("Hi %s, I'm the %s script." % (user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me , %s ?" % user_name)
likes = input(prompt)

print("Where do you live %s?" % user_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)
type(computer)
if int(computer) > 3:
    rank = "good"
else:
    rank = "bad"
print("""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. %r.
""" % (likes, lives, computer, rank))
