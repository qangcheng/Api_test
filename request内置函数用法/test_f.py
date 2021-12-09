"""
用例后置操作示例，如何在teardown中执行之前接口获取到的数据，完成最后数据清理动作
"""
import allure
import pytest


@pytest.fixture()
def delete_sp_id(request):
    print("前置操作执行完成")
    yield
    print("teardown操作，用例完成后")
    print("拿到的商品id是{}".format(request.config.sp_id))
    print("delete操作SQL数据库删除用例完成生成的id:{}".format(request.config.sp_id))

@allure.title("测试用例中的返回值生成后，反回到fixture方法，完成teardown操作")
def test_x(request, delete_sp_id):
    result = {
        "code": 0,
        "msg": "sueecss",
        "data": {
            "id": 10086,
            "name": "ssss",
            "goodsname": "sp_1111"
        }
    }
    request.config.sp_id = result["data"]["id"]
    print("用例执行的结果拿到的id是：{}".format(request.config.sp_id))
    assert result["code"] == 0
