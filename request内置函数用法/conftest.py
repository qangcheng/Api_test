"""
本地插件开发，本地生成命令行命令,注册参数，autouse且不用调用直接前置自动启动命令演示
"""
import pytest


def pytest_addoption(parser):
    # 注册host
    parser.addoption(
        "--host", action="store", default="test", help="change test host:default")
    # 注册ini中username
    parser.addini(
        "username", type=None, default="test", help="add ini username")

    # 注册url地址
    parser.addini(
        "base_url1", type=None, default="", help=" base_url1",)

    parser.addini(
        "base_url2", type=None, default="", help="base_url2",)


@pytest.fixture()
# 获得用用在命令行输入内容
def host(request):
    if request.config.getoption("--host") == "test":
        return "http://49.235.92.12:7005"
    if request.config.getoption("--host") == "uat":
        return "http://49.235.92.12:8005"
    else:
        return "host not exists"


@pytest.fixture(scope="session")
def base_url1(request):
    return request.config.getini("base_url1")


@pytest.fixture(scope="session")
def base_url2(request):
    return request.config.getini("base_url2")


# 添加参数autouse 后自动执行，没有添加就不行执行
@pytest.fixture(autouse=True)
def request_print(request):
    print(request.module)
    print(request.function)
    print(request.fspath)
    print(request.scope)


# pytest.ini 读取
@pytest.fixture(autouse=True)
def get_ini(request):
    ops = request.config.getini("addopts")
    print("读取到的ops是:{}".format(ops))
    user = request.config.getini("username")
    print("读取到的username是:{}".format(user))
    return ops, user
