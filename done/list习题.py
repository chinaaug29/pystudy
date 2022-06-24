# scenic_spot = ["Paris", "London", "Rome", "Madrid", "Berlin", "Vienna", "Milan", "Budapest", "Moscow", "Copenhagen"]
# scenic_spotZn = ["巴黎", "伦敦", "罗马", "马德里", "柏林", "维也纳", "米兰", "布达佩斯", "莫斯科", "哥本哈根"]
# print(scenic_spot[::-1])

banquet_list = ['十四阿哥', '十三阿哥', '康熙', '太子', '皇阿玛']
print("宾客名单：",banquet_list)
T = True
while T:
    print("选择数字'2'将增加一个宾客；选择'1'将删除一位宾客;")
    choice_list = input("请输入您的选择：")
    if choice_list == '1':
        print("现在的宾客名单是：", banquet_list)
        i = input("选择删除的数字")
        banquet_list1 = banquet_list.pop(int(i))
        print("您选择删除了：%s" % banquet_list1)
        print(banquet_list)
    elif choice_list == '2':
        f = input("请输入添加的宾客")
        banquet_list.append(f)
        print("您增加了：%s" % (banquet_list[-1]))
        print("现在的宾客名单是：%s" % banquet_list)
    else:
        T = False
        print("选择错误，请输入正确的选择!")