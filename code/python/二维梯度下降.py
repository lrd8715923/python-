import xlrd
import xlwt
import numpy as np
import matplotlib.pyplot as plt
data = xlrd.open_workbook('二维梯度下降训练集.xlsx')
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols
x = table.col_values(0)
y = table.col_values(1)
del x[0]
del y[0]
nrows-=1
hy = []
for i in range(nrows):
    hy.append(0)
themp0 = 0.0
themp1 = 0.0
alpha = 0.0001
re=100000
r = 0
for i in range(nrows):
    hy[i]=themp0+themp1*x[i]
while (r < re):
    sum1 = 0.0
    sum2 = 0.0
    for i in range(nrows):
        sum1 += hy[i] - y[i]
    sum1 = sum1 / nrows * alpha
    themp0-=sum1
    for i in range(nrows):
        hy[i]=themp0+themp1*x[i]
    for i in range(nrows):
        sum2 += (hy[i] - y[i]) * x[i]
    sum2 = sum2 / nrows * alpha
    themp1-=sum2
    for i in range(nrows):
        hy[i]=themp0+themp1*x[i]
    r += 1
print(themp0)
print(themp1)
for i in range(nrows):
    hy[i]=round(hy[i],1)
print("训练完毕")
print('训练结果:',hy)
print("样本结果:",y)
fig = plt.figure()
ax1 = fig.add_subplot(111)
plt.xlabel('size')
plt.ylabel('price')
ax1.scatter(x,y)
prex=np.linspace(0, max(x))
Or=prex*themp1+themp0
plt.plot(prex, Or, color="red")
print("请输入要预测的大小，输入q退出")
while(1):
     the=input()
     if the=='q':
         break
     the=float(the)
     output=the*themp1+themp0
     output=int(output)
     print("%d大小对应的房价预测值为%d"%(the,output))
plt.show()