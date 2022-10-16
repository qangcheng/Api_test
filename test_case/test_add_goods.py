import pytest
from api.add__get_update_goods import add_goods, good_id
import time
import os
from common.resd_yaml import readyml
import allure

l_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
goodspath = os.path.join(l_path, "data", "ymltestgoods.yml")
test_goodspath = readyml(goodspath)


@allure.feature("添加商品")
class TestGoods(object):
    """商品接口请求测试报告"""

    @allure.story("添加不同类型字符串商品名称参数化")
    # @pytest.mark.parametrize("goodsname,ecpext,title", [
    #     ["", {"code": 3003, "msg": "参数不合法"}, "参数化添加商品名称为空"],
    #     ["appoium自动化", {"code": 0, "msg": "success!"}, "参数化添加中文加英文商品名称"],
    #     ["<<>>,23@!!!", {"code": 0, "msg": "success!"}, "参数化添加乱码商品名称"],
    #     ["2323434234343242342343423423423432423423423423434434", {"code": 3003, "msg": "参数不合法"}, "参数化添加大于30位字符商品名称"]
    # ])
    @pytest.mark.parametrize("goodsname,ecpext,title", test_goodspath)  # 配置化读取
    def test_add_goods_goodsname(self, base_url, login_fixture, goodsname, ecpext, title):
        """参数化:添加不同商品名称"""
        allure.dynamic.title("动态标题是:{}:".format(title))  # 动态获取到title,也可以获取到story等。
        good_id = "sp_" + str(int(time.time()))
        r2 = add_goods(s=login_fixture, base_url=base_url, good_id=good_id, goodsname=goodsname)
        print(r2.text)
        time.sleep(1.5)
        assert r2.json()["code"] == ecpext["code"]
        assert r2.json()["msg"] == ecpext["msg"]

    @allure.story("添加商品成功")
    @allure.title("用例标题:输入中文加英文字符商品名称")
    def test_add_goods_succees(self, base_url, login_fixture):

        """添加商品成功"""
        r2 = add_goods(s=login_fixture, base_url=base_url, good_id=good_id, goodsname="appium自动化")
        print(r2.text)
        assert r2.json()["code"] == 0
        assert r2.json().get("msg") == "success!"
        assert r2.json().get("data").get("goodsname") == "appium自动化"

    @allure.story("添加商品成功")
    @allure.title("用例标题:输入商品id名称为null")
    def test_add_goodid_null(self, base_url, login_fixture):
        """商品id为空"""
        r2 = add_goods(s=login_fixture, base_url=base_url, good_id="", goodsname="appium自动化")
        print(r2.text)
        assert r2.json()["code"] == 2000
        assert r2.json().get("msg") == "缺少必填项goodscode"
        assert r2.json().get("data").get("goodsname") is None

    @allure.story("添加商品失败")
    @allure.title("用例标题:输入商品id重复添加")
    def test_add_Duplicate_ID(self, base_url, login_fixture):
        """商品id重复添加：此接口不能单独请求，需要和第一条case配合请求，也可重复请求2次"""
        r2 = add_goods(s=login_fixture, base_url=base_url, good_id=good_id, goodsname="")
        print(r2.text)
        assert r2.json()["code"] == 4000
        assert r2.json().get("msg") == "goodscode不能重复添加"
        assert r2.json().get("data").get("goodsname") is None

    @allure.story("添加商品失败")
    @allure.title("用例标题:输入商品名称为空")
    def test_add_goodsname_null(self, base_url, login_fixture):
        """商品名称为空"""
        good_id = "sp_" + str(int(time.time())) + "1"
        r2 = add_goods(s=login_fixture, base_url=base_url, good_id=good_id, goodsname="")
        print(r2.text)
        assert r2.json()["code"] == 3003
        assert r2.json().get("msg") == "参数不合法"
        assert r2.json().get("data").get("goodsname")[0] == "该字段不能为空。"
