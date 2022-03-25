# coding = utf-8
import pytest
import requests
import allure

from api.login import login


@allure.feature("登录")
class Test_login(object):
    @pytest.mark.smoke
    @allure.severity("blocker")
    @allure.story("登录成功用例")
    @allure.title("输入正确账号密码登录")
    def test_login_success(self, base_url):  # 冒烟测试用例
        """登录成功用例"""
        s = requests.Session()
        r = login(s, base_url, "test", "123456")
        assert r.json().get("code") == 0
        assert r.json().get("msg") == "login success!"
        assert len(r.json().get("token")) == 40

    @allure.story("登录失败用例")
    @pytest.mark.parametrize('user,psw,title',
                             [
                                 ["test10", "123321", "登录密码错误"],
                                 ["aaxxxx01", "123456", "登录账号错误"],
                                 ["test10", "", "登录密码为空"],
                                 ["", "", "登录账号密码都为空"]

                             ]
                             )
    def test_login_fail(self, base_url, user, psw, title):
        """登录失败用例"""
        s = requests.Session()
        allure.dynamic.title(title)
        r = login(s, base_url, user, psw)
        assert r.json().get("code") == 3003
        assert r.json().get("masg") is None
        assert len(r.json().get("token")) == 0
