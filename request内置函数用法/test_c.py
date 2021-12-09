import allure


@allure.title("读取注册命令后的host")
def test_a(host):
    print("获取到的环境地址是：{}".format(host))

@allure.title("注册ini表的参数后，request内置函数读取")
def test_xxx(base_url, base_url2, base_url1):
    """读取ini文件中不同的三个测试地址"""
    print("测试第一次读到的地址是:{}".format(base_url))
    print("测试第二次读到的地址是:{}".format(base_url1))
    print("测试第三次读到的地址是:{}".format(base_url2))