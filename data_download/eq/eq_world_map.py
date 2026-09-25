import plotly.express as px
from pathlib import Path 
import json 
 
# 将数据作为字符串读取并转换为 Python 对象 
path = Path(r"D:\学习文件\GitHub\python_practice\data_download"
            r"\eq\eq_data\eq_data_1_day_m1.geojson") 
try:
    contents = path.read_text()
except:
    contents = path.read_text(encoding='utf-8') 
all_eq_data = json.loads(contents) 
 
# 查看数据集中的所有地震
all_eq_dicts = all_eq_data['features']
title=all_eq_data['metadata']['title']

#提取数据
mags,zone,lons,lats=[],[],[],[]
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    zone.append(eq_dict['properties']['title'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])

fig=px.scatter(
    x=lons,
    y=lats,
    labels={'x':'经度','y':'纬度'},
    range_x=[-200,200],
    range_y=[-90,90],
    width=800,
    height=800,
    title=title,
    size=mags,
    size_max=10,
    color=mags,
    hover_name=zone,
)

fig.show()