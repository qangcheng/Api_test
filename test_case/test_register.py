"""
注册接口测试用例
"""
import pytest
from api.register_api import register
import allure

@allure.feature("注册")
class Test_Register(object):

    @pytest.mark.smoke
    @allure.severity("blocker")
    @allure.story("注册成功")
    @allure.title("输入正确账号完成注册")
    def test_register_suceess(self, base_url, delete_register_user):
        """注册成功"""
        r = register(base_url, user="test_xxyy")
        print(r.json())
        assert r.json().get('code') == 0
        assert r.json().get('msg') == "register success!"

    @allure.story("注册失败")
    @allure.title("输入已注册账号注册")
    def test_register_2(self, base_url, delete_register_user):
        """重复注册账号"""
        r1 = register(base_url, user="test_xxyy")
        r2 = register(base_url, user="test_xxyy")
        print(r2.json())
        assert r2.json()['code'] == 2000
        assert r2.json()['msg'] == 'test_xxyy用户已被注册'

    @allure.story("注册失败")
    @allure.title("注册名称为空")
    def test_nulluser_resgister(self, base_url):
        """注册账号为null"""
        r1 = register(base_url, user="")
        print(r1.json())
        assert r1.json()["code"] == 3003
        assert r1.json()["data"].get("username")[0] == "该字段不能为空。"
