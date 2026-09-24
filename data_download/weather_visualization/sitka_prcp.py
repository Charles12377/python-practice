from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

"""锡特卡数据处理"""
path_1=Path(r"D:\学习文件\GitHub\python_practice\data_download"
          r"\weather_data\sitka_weather_2021_full.csv")
lines_1=path_1.read_text().splitlines()

reader_1=csv.reader(lines_1)

header_row_1=next(reader_1)

dates_1=[]
prcps_1=[]
for row in reader_1:
    date=datetime.strptime(row[2],'%Y-%m-%d')
    try:
        prcp=float(row[5])
    except ValueError:
        print(f"Missed the date:{date}")
    else:    
        dates_1.append(date)
        prcps_1.append(prcp)

"""死亡谷数据处理"""
path_2=Path(r"D:\学习文件\GitHub\python_practice\data_download"
            r"\weather_data\death_valley_2021_full.csv")
lines_2=path_2.read_text().splitlines()

reader_2=csv.reader(lines_2)

header_row_2=next(reader_2)

dates_2=[]
prcps_2=[]
for row in reader_2:
    date=datetime.strptime(row[2],'%Y-%m-%d')
    try:
        prcp=float(row[3])
    except ValueError:
        print(f"Missed the date:{date}")
    else:    
        dates_2.append(date)
        prcps_2.append(prcp)

plt.style.use('seaborn-v0_8')
fig,ax=plt.subplots()
ax.plot(dates_1,prcps_1,color='blue')
ax.plot(dates_2,prcps_2,color='yellow')

#设置图表样式
title="Prcp of stika and death valley,2021"
ax.set_title(title,fontsize=16)
fig.autofmt_xdate(rotation=45)
ax.set_xlabel('Date',fontsize=12)
ax.set_ylabel('Prcp',fontsize=12)

y_min=0
y_max=1
ax.set_ylim(y_min,y_max)

plt.show()