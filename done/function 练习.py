
num_int = input("请输入一个整数！")


def sum_num(num_int):
    """计算1+2-3+4……-（n-1）+n的计算公式"""

    print(f"您输入的参数是：{num_int}")
    n = int(num_int)
    u = 1  # 设置循环变量的初值为零
    # if n % 2 == 0 and n >= 4:
    for i in range(2, n + 1):
        # print("i=", i)
        if i % 2 == 0:
            u += i  # 这个简化的算式是错的，所以无法得到正确答案
        else:
            u -= i
    return u


print("u=", sum_num(num_int))
