"""
参数化标题3种方法
1： test_data种直接添加ids参数作为title,ids=[xxxx,xxxx,xxxx]
2:  测试数据中直接添加测试title,直接用allure.title去读取
3: 动态获取allue
"""


import allure
import pytest
import requests
from common.resd_yaml import readyml
import os

current_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(current_directory)
yaml_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "ymltsetdata.yml")
test_data = readyml(yaml_path)['userinfo']
print(test_data)

@allure.story("参数化登录用例")
@pytest.mark.parametrize("test_input,expected,title", test_data)
def test_login_params(base_url, test_input, expected, title):
    """参数化不同账号登录"""
    allure.dynamic.title(title)
    s = requests.Session()
    url = base_url + "/api/v1/login"
    body = {
        **test_input
    }
    r = s.post(url, json=body)
    print(r.text)
    token = r.json().get("token")
    print(f"获取到的token为:{token}")
    assert r.json().get("code") == expected["code"]
