# 判断输入数据的类型
import re
num_str = input("请输入一个数值：")
num_r = re.match(r"^[-+]?\d*\.+\d+$", num_str)
num_rl = re.match(r"^[-+]?\d+\d*$", num_str)
if num_r:
    num_float = -1 * float(num_r.group())
    print(num_float)
elif num_rl:
    num_int = -1 * int(num_rl.group())  # group() 返回正则匹配的子字符串
    print(num_int)
else:
    print("输入错误，请输入正确数值")

# '''
# pjdr_number = input("请输入数据：" + "\n")  # 输入任意数据
# pddr = pjdr_number.isdigit() # isdigit()方法判断输入的数据是否是纯数字，返回逻辑值，但是对于负数判断却是false，只对正数有效
# print(pddr)
# if pddr :
#     number_type: int = int(pjdr_number)
#     if number_type >= 0 :
#         print(number_type * -1)
#     else:
#         print(abs(number_type))
# else:
#     print('X' * 40)
#     print("输入的不是数字类型，类型错误！")
#     pass
# '''
# '''
# if pddr == False :
#     print('X' * 40)
#     print("输入的不是数字类型，类型错误！")
#     pass
# else:
#     number_type: int = int(pjdr_number)
# if number_type >= 0 :
#     print(number_type * -1)
# else:
#     print(abs(number_type))
# '''
#
# '''
# if pddr == True:
#     number_type = int(pjdr_number)  # 把输入数据转换为整型数据
# if number_type >= 0 :
#     print(number_type * -1)
# elif number_type < 0 :
#     print(abs(number_type))
#
#     print('X' * 40)
#     print("输入的不是数字类型，类型错误！")
# '''
