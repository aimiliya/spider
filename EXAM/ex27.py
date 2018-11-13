# 逻辑判断进行与非判断
"""
1. True and True
2. False and True
3. 1 == 1 and 2 == 1
4. "test" == "test"
5. 1 == 1 or 2 != 1
6. True and 1 == 1
7. False and 0 != 0
8. True or 1 == 1
9. "test" == "testing"
10. 1 != 0 and 2 == 1
11. "test" != "testing"
12. "test" == 1
13. not (True and False)
14. not (1 == 1 and 0 != 1)
15. not (10 == 1 or 1000 == 1000)
16. not (1 != 10 or 3 == 4)
17. not ("testing" == "testing" and "Zed" == "Cool Guy")
18. 1 == 1 and not ("testing" == 1 or 1 == 0)
19. "chunky" == "bacon" and not (3 == 4 or 3 == 3)
20. 3 == 3 and not ("testing" == "testing" or "Python" == "Fun")
"""


# 对传入的逻辑表达式进行判断，并输出结果
def bool_test(count, test):
    for isTrue in test:
        count += 1
        print("%d: %s" % (count, isTrue))


count = 0
test = [True and True, False and True, 1 == 1 and 2 == 1, "test" == "test", 1 == 1 or 2 != 1, True and 1 == 1,
        False and 0 != 0, True or 1 == 1, "test" == "testing", 1 != 0 and 2 == 1, "test" != "testing", "test" == 1,
        not (True and False), not (1 == 1 and 0 != 1), not (10 == 1 or 1000 == 1000), not (10 != 1 or 3 == 4),
        not ("testing" == "testing" and "Zed" == "Cool Guy"), 1 == 1 and not ("testing" == 1 or 1 == 0),
        "chunky" == "bacon" and not (3 == 4 or 3 == 3), 3 == 3 and not ("testing" == "testing" or "Python" == "Fun")

        ]
bool_test(count, test)
