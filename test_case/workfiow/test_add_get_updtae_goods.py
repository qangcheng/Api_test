"""
测试用例工作流：登录（前置操作）-添加商品-查询商品-修改商品-查询（是否修改成功）
"""

import time
from api.add__get_update_goods import add_goods, update_goods, get_goods
import allure


@allure.feature("添加商品")
@allure.story("添加商品流程")
@allure.title("添加商品后更改商品信息后查看是否成功")
def test_goods_workflow(login_fixture, base_url):
    # step-1 添加商品
    good_id = "sp_" + str(int(time.time()))
    r = add_goods(s=login_fixture, base_url=base_url, good_id=good_id, goodsname="appium自动化")

    # step-2 查询添加商品的 sp_id
    sp_id = r.json()["data"]["id"]
    print("获得的商品id是：", sp_id)
    goodsname = r.json()["data"]["goodsname"]
    print("修改之前商品名称是：", goodsname)

    # step-3 修改商品名称
    r2 = update_goods(s=login_fixture,
                      base_url=base_url,
                      sp_id=sp_id,
                      goodsname="update_xxxx",
                      goodscode=good_id)
    print("修改后返回为", r2.json())

    # 查询修改后的商品信息
    r3 = get_goods(s=login_fixture,
                   base_url=base_url,
                   sp_id=sp_id)
    result_goodsname = r3.json()["data"]["goodsname"]
    print("修改后商品ID是:", result_goodsname)
    assert "update_xxxx" == result_goodsname
