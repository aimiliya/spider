# 基于if else的小游戏
print("你进入了一间黑屋子里，他有两个门，你要进入那个门呢？ 1 或 2")

door = input(">")

if door == "1":
    print("这里有一只大熊在吃奶酪蛋糕。你想怎么做?")
    print("1, 去吃蛋糕.")
    print("2, 对这熊尖叫")

    bear = input(">")

    if bear == "1":
        print("这个熊吃掉了你的脸，干的漂亮！")
    elif bear =="2":
        print("这熊吃掉了你的腿，干的漂亮！")
    else:
        print("当然，%s 可能更好。熊跑开了" % bear)
elif door =="2":
    print("你凝视这无尽的深渊。")
    print("1,蓝莓")
    print("2,黄色夹克")
    print("3,理解左轮手枪的旋律")

    insanity = input(">")

    if insanity =="1" or insanity =="2":
        print("你的身体靠一颗果冻的心存活下来了。")
    else:
        print("The insanity rots your eyes into a pool of muck")

else:
    print("你什么也没做，然后死去了")

