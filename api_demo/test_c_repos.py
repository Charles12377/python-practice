import pytest

import requests
import plotly.express as px
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def test_status_code():
    # 执行 API 调用并查看响应 
    url = "https://api.github.com/search/repositories" 
    url += "?q=language:c+sort:stars+stars:>10000" 
    headers = {"Accept": "application/vnd.github.v3+json"} 
    r = requests.get(url, headers=headers,verify=False) 
    assert r.status_code == 200