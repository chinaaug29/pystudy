# open库的练习
opfile = open(r"E:\百度云同步盘\BaiduNetdiskWorkspace\pythontest\test1py\python练习\cj.txt", mode='r',
              encoding="utf-8")  # 读取文件，不写入
opfile1 = open(r"E:\百度云同步盘\BaiduNetdiskWorkspace\pythontest\test1py\python练习\cj1.txt", mode='w',
               encoding="utf-8")  # 覆盖源文件，重新写入
opfile2 = open(r"E:\百度云同步盘\BaiduNetdiskWorkspace\pythontest\test1py\python练习\cj.txt", mode='r+',
               encoding="utf-8")  # 读取文件并写入数据，与w参数类似
# opfile3 = open(r"E:\百度云同步盘\BaiduNetdiskWorkspace\pythontest\test1py\python练习\cj2.txt", mode='x+', encoding="utf-8") #新建文件并写入数据，如果存在同名文件报错
opfile4 = open(r"E:\百度云同步盘\BaiduNetdiskWorkspace\pythontest\test1py\python练习\cj.txt", mode='a',
               encoding="utf-8")  # 追加数据到文件尾
print("姓名       国文      英语      总分", file=opfile1)
print("%3s      %4d     %4d    %4d" % ("洪斌如", 98, 90, 188), file=opfile1)
print("%3s      %4d     %4d    %4d" % ("洪雨馨", 96, 95, 191), file=opfile1)
print("%3s      %4d     %4d    %4d" % ("洪冰雨", 92, 88, 180), file=opfile2)
print("%3s      %4d     %4d    %4d" % ("洪心悦", 93, 97, 190), file=opfile4)
print("%3s      %4d     %4d    %4d" % ("洪斌如", 98, 90, 188), file=opfile4)
print("%3s      %4d     %4d    %4d" % ("洪雨馨", 96, 95, 191), file=opfile1)
print("%3s      %4d     %4d    %4d" % ("洪冰雨", 92, 88, 180), file=opfile2)
print("%3s      %4d     %4d    %4d" % ("洪心悦", 93, 97, 190), file=opfile4)
opfile.close()  # 关闭打开的文件，关闭后才能在资源管理器中查看文件，没有这个操作会出现错误
opfile1.close()
opfile2.close()
# opfile3.close()
opfile4.close()
