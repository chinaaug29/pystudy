import re

# 有一个百货公司庆祝50年周年庆，消费满10万元可打9折，消费满8万元可打95折，消费满5万元，可打98折。如果今年是50岁的消费者不论消
# 费金额都打95折，请设计这个程序。
T = True
while T:
    年龄 = input("请输入您的年龄：")
    消费金额 = input("请输入您的消费金额：¥")
    提取年龄字符串 = re.match(r"^\d{2}$", 年龄)
    提取消费金额 = re.match(r"^\d*\.?\d+$", 消费金额)
    if 年龄 == "50":  # 这是字符串比较，所以需要用双引号包括
        print("共计消费¥%-6.2f元" % (float(提取消费金额.group()) * 0.95))
    elif float(消费金额) >= 100000:
        print("共计消费¥%-6.2f元，打九折" % (float(提取消费金额.group()) * 0.9))
    elif float(消费金额) >= 80000:
        print("共计消费¥%-6.2f元，打九五折" % (float(提取消费金额.group()) * 0.95))
    elif float(消费金额) >= 50000:
        print("共计消费¥%-6.2f元，打九八折" % (float(提取消费金额.group()) * 0.98))
    else:
        if "99" > 年龄 >= "0" and 消费金额 >= "0":
            print("共计消费%-6.2f元" % (float(消费金额.group())))
        else:
            T = False  # while循环退出循环的开关





