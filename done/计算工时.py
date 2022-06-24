import re
from typing import Optional, Match


work_time = input("请输入你的工作时间：")
print(f"你的工作时间是{work_time}小时！")
new_work_time: Optional[Match[str]] = re.match(r"^\d+\.?\d*$", work_time)
if new_work_time is None or float(new_work_time.group()) > 240:
    print("输入有误，请重新输入")
elif float(new_work_time.group()) > 150:
    print('你的薪水是：¥%-6.2f' % (float(new_work_time.group()) * 150 * 1.6))
elif 121 < float(new_work_time.group()) < float(150):
    print('你的薪水是：¥%-6.2f' % (float(new_work_time.group()) * 150 * 1.2))
elif work_time == "120":
    print("你的薪水是：¥%-6.2f" % (float(120 * 150)))
else:
    print('你的薪水是：¥%-6.2f' % (float(new_work_time.group()) * 150.00 * 0.8))
