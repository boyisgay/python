from matplotlib import pyplot as plt
import random

import matplotlib


# x = range(2, 26, 2)
# y = [25, 12, 45, 23, 45, 24, 12, 32, 43, 12, 12, 23]
#
# fig = plt.figure(figsize=(20, 8), dpi=80)
# plt.plot(x, y)
# # plt.savefig("./sig_size3.png")
# # plt.savefig("./sig_size3.svg")
# plt.xticks(range(1, 26))
# plt.yticks(range(min(y), max(y)+1))
# plt.show()





x = range(120)
y = [random.randint(20, 35) for i in range(120)]
# 生成120个在20-35之间的随机整数

# plt.figure(figsize=(30, 8), dpi=80)

# 中文字符不显示问题
# 方案1
font = {
        'family': 'MicroSoft YaHei',
        'weight': 'bold',
        }
matplotlib.rc('font', **font)
# 查看rc源码获取更多

# 方案2
# from matplotlib import font_manager
# my_font = font_manager.FontProperties(fname='字体路径')
# plt.xticks(_x[::3], _x_tables[::3], rotation=270, fontproperties=my_font)
# 查看rc源码获取更多


_x = list(x)
_x_tables = ["10时{}分".format(i) for i in range(60)]
_x_tables += ["11时{}分".format(i) for i in range(60)]
plt.xticks(_x[::3], _x_tables[::3], rotation=45)
# 传str  一个对应一个
# rotation 旋转x刻度的显示

# 设置图片描述信息
plt.xlabel("时间")
plt.ylabel("温度")
plt.title("气温变化图")


plt.plot(x, y)

plt.show()



