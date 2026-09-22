import matplotlib.pyplot as plt

x_value=range(1,5001)
y_value=[x**3 for x in x_value]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_value,y_value,c=y_value,cmap=plt.cm.Reds,edgecolors='none',s=13)

#设置图题并给坐标轴加上标签
ax.set_title("Cube Numbers",fontsize=24)
ax.set_xlabel("Value",fontsize=13)
ax.set_ylabel("Cube of Value",fontsize=13)

#设置标签刻度的样式
ax.tick_params(labelsize=13)

plt.show()