import requests
import plotly.express as px
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# 执行 API 调用并查看响应 
url = "https://api.github.com/search/repositories" 
url += "?q=language:c+sort:stars+stars:>10000" 
headers = {"Accept": "application/vnd.github.v3+json"} 
r = requests.get(url, headers=headers,verify=False) 
print(f"Status code: {r.status_code}") 

# 将响应转换为字典 
response_dict = r.json() 
print(f"Total repositories: {response_dict['total_count']}") 
print(f"Complete results: {not 
response_dict['incomplete_results']}") 

# 探索有关仓库的信息
repo_dicts = response_dict['items'] 
print(f"Repositories returned: {len(repo_dicts)}") 
repo_links,stars,hover_texts=[],[],[] 
for repo_dict in repo_dicts:
    repo_name=repo_dict['name']
    repo_url=repo_dict['html_url']
    repo_link=f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])

    #创建悬停文本
    owner=repo_dict['owner']['login']
    description=repo_dict['description']
    hover_text=f"{owner}<br />{description}"
    hover_texts.append(hover_text)

#可视化加设置图形样式
title="Most-Stars C Projects on Github"
labels={'x':'Repository','y':'Stars'}
fig=px.bar(x=repo_links,y=stars,title=title,labels=labels,
           hover_name=hover_texts)
fig.update_layout(title_font_size=28,xaxis_title_font_size=15,
                  yaxis_title_font_size=15,xaxis_tickangle=45)
fig.update_traces(marker_color='Steelblue',marker_opacity=0.7)

fig.show()