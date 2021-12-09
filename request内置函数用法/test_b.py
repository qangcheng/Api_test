"""
request内置函数，如何在前置条件中输入多个返回值，切在测试用例中解包执行用例
"""
import allure
import pytest


@pytest.fixture(params=["test1", "test2"])
def register(request):
    print("实现的注册功能：{}".format(request.param))
    result = "success"
    return request.param, result


# 返回值2个去解包处理
@allure.title("fixture多个参数读取,函数方法获取到多个返回值解包")
def test_b(register):
    param, result = register
    print("测试用例里面拿到的param返回值是：{}".format(param))
    print("测试用例里面拿到的result返回值是：{}".format(result))
