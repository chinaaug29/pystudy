import re

t = True
while t:
    judge_data = input("请输入一个数值：")
    num_judge = re.match(r"[-+]?\d*\.?\d+", judge_data)  # 匹配带正负号的整数和小数
    word_judge = re.match(r"[A-Z]+", judge_data)  # 匹配大写字母
    wordl_judge = re.match(r"[a-z]+", judge_data)  # 匹配小写字母
    other_judge = re.search(r"[^a-zA-Z0-9\s]+", judge_data)  # 匹配除数字字母及空格以外的所以符号
    if num_judge:
        print(num_judge.group())  # 数字直接输出
    elif word_judge:
        new_word = word_judge.group()  # 把匹配的data传递给new_word新变量
        print(new_word.lower()) # 大写字母转换成小写，字母内有小写的无法全部转换，因为正则表达没有捕获全部字母
    elif wordl_judge:
        new_wordl = wordl_judge.group() # 匹配的数据赋值给新变量
        print(new_wordl.upper()) # 小写字母转换成大写，字母内有小写的无法全部转换，因为正则表达没有捕获全部字母
    else:
        t = False  # while循环，退出的开关（除数字字母及空格以外的符号）程序退出
        print("输入的是非法字符！请重新输入")
