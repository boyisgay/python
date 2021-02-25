from matplotlib import pyplot as plt
import random
import matplotlib

font = {
    'family': 'MicroSoft YaHei',
    'weight': 'bold',
}
matplotlib.rc('font', **font)

y_1 = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
y_2 = [random.randint(0, 5) for i in range(20)]
x = range(11, 31)

_x = x
_x_table = ["{}岁".format(i) for i in _x]
plt.xticks(_x, _x_table, rotation=45)


plt.xlabel('年龄')
plt.ylabel('个数')
plt.title('XXX图')
# 绘制网格 稀疏按照xy的刻度
plt.grid(alpha=0.2)
"""
alpha:透明度

"""
# 绘制多张表
"""
color：线条颜色（或十六进制）
linestyle：线条风格
linewidth：线宽
alpha：透明度
label：图例标签

"""
plt.plot(x, y_1, label="小明")
plt.plot(x, y_2, label="小红")

# 将图例信息展示出来
"""
loc:显示位置默认右上
prop：指定字体
"""
plt.legend()

# 添加水印
# 标注最大值最小值
plt.show()