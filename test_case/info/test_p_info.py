import pytest
import requests
from api.updateinfo import update_info
from common.resd_yaml import readyml
from pathlib import Path

# test_data = [
#     [{"name": "test1", "age": "22", "sex": "F", "mail": "335992197@qq.com"},
#      {"code": 0, "msg": "update some data!"}],
#     [{"name": "test_xa", "age": "22", "sex": "F", "mail": "335992197@qq.com"},
#      {"code": 4003, "msg": "无权限操作"}]
# ]
# 测试数据在哪里管理？ yaml,json,excel,text,csv
P = Path(__file__)
yamlpath = P.parent.parent.parent.joinpath("data", "data.yaml")
test_data = readyml(yamlpath)["info"]


@pytest.mark.parametrize("test_input,expected", test_data)
def test_ueserinfo(login_fixture, base_url, test_input, expected):
    """ 修改信息正确"""
    r = update_info(login_fixture, base_url, **test_input)
    print(r.text)
    assert r.json().get("code") == expected["code"]
    assert r.json().get("message") == expected["msg"]
