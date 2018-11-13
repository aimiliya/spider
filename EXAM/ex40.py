# 字典练习
cities = {'CA': 'San Francisco', "MI": 'Detroit', 'FL': 'Jacksonville'}

cities['NY'] = 'New York'
cities['OR'] = "Portland"

# 对dict进行遍历
for key, value in cities.items():
    print("%r : %r" % (key, value))


# 查找字典中的城市
def find_city(themap, state):
    if state in themap:
        return themap[state]
    else:
        return "Not found."


# ok pay attention!
# 将函数赋值给一个字典
cities['_find'] = find_city


while True:
    print("State? (ENTER to quit)", end=" ")
    state = input(">")

    if not state:
        break

    # This line is the most important ever! study
    city_found = cities['_find'](cities, state)
    print(city_found)

