import xlrd
import xlwt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
data = xlrd.open_workbook('三维梯度下降训练集.xlsx')
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols
x1 = table.col_values(0)
x2 = table.col_values(1)
y = table.col_values(2)
del x1[0]
del x2[0]
del y[0]
hy = []
for i in range(nrows):
    hy.append(0)
themp0 = 0.0
themp1 = 0.0
themp2 = 0.0
alpha = 0.0001
re = 1000000
r = 0
nrows-=1
for i in range(nrows):
    hy[i] = themp0 + themp1 * x1[i] + themp2 * x2[i]
while (r < re):
    sum1 = 0.0
    sum2 = 0.0
    sum3 = 0.0
    for i in range(nrows):
        sum1 += hy[i] - y[i]
    sum1 = sum1 / nrows * alpha
    themp0 -= sum1
    for i in range(nrows):
        hy[i] = themp0 + themp1 * x1[i] + themp2 * x2[i]
    for i in range(nrows):
        sum2 += (hy[i] - y[i]) * x1[i]
    sum2 = sum2 / nrows * alpha
    themp1 -= sum2
    for i in range(nrows):
        hy[i] = themp0 + themp1 * x1[i] + themp2 * x2[i]
    for i in range(nrows):
        sum3 += (hy[i] - y[i]) * x2[i]
    sum3 = sum3 / nrows * alpha
    themp2 -= sum3
    for i in range(nrows):
        hy[i] = themp0 + themp1 * x1[i] + themp2 * x2[i]
    r += 1
print(themp0)
print(themp1)
print(themp2)
for i in range(nrows):
    hy[i] = round(hy[i], 1)
print("训练完毕")
print('训练结果:', hy)
print("样本结果:", y)
print("请输入要预测的大小和卧室数量，输入q退出")
while (1):
    the = input()
    if the == 'q':
        break
    the1 = input()
    the = float(the)
    the1 = float(the1)
    output = the1 * themp2 + the * themp1 + themp0
    output = int(output)
    print("%d大小卧室数量为%d对应的房价预测值为%d" % (the, the1, output))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
xs=x1
ys=x2
zs=y
ax.set_xlabel('size')
ax.set_ylabel('bedroom')
ax.set_zlabel('price')
ax = Axes3D(fig)
X = np.linspace(0, max(x1))
Y = np.linspace(0, max(x2))
X, Y = np.meshgrid(X, Y)
Z = X*themp1+Y*themp2+themp0
ax.plot_surface(X, Y, Z,rstride=2, cstride=1, cmap=plt.cm.hot)
ax.scatter(xs, ys, zs,c='g')
plt.show()
