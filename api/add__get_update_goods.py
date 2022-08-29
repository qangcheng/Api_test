import requests
import time
from api.login import login

good_id = "sp_" + str(int(time.time()))


def add_goods(s, base_url, goodsname: str, good_id, **kwargs):
    """
    添加商品信息
    :param s:  创建session会话
    :param base_url: 请求地址，查看在pytestini
    :param goodsname: 商品名称
    :param good_id: 商品id
    :param kwargs: 其他参数
    :return: 返回添加的商品的信息
    """
    """新增商品接口"""
    url = base_url + "/api/v1/goods"
    body = {
        "goodsname": goodsname,
        "goodscode": good_id
    }
    # 更新字典
    body.update(kwargs)
    r = s.post(url, json=body, verify=False)
    return r


def get_goods(s, base_url, sp_id):
    """查询单个商品接口"""
    url1 = base_url + "/api/v2/goods/{}".format(sp_id)
    r2 = s.get(url1)
    return r2


def update_goods(s, base_url, sp_id, goodsname, goodscode, **kwargs):
    """
    :param s:  session会话
    :param base_url: 测试地址
    :param sp_id: 商品ID
    :param goodsname: 商品名称
    :param goodscode: 商品代码
    :param kwargs: 其余非必填写参数
    :return: 修改商品后的字段
    """
    """修改单个商品接口"""
    url2 = base_url + "/api/v2/goods/{}".format(sp_id)
    body = {
        "goodsname": goodsname,
        "goodscode": goodscode,
    }
    body.update(**kwargs)
    r3 = s.put(url2, json=body)
    return r3


if __name__ == '__main__':
    s = requests.Session()
    base_url = "http://49.235.92.12:7005"
    r1 = login(s, base_url, "test", "123456")
    r2 = add_goods(s, base_url, goodsname="appium自动化", good_id=good_id)
    print(r2.text)
    r3 = get_goods(s, base_url, sp_id=15425)
    print(r3.text)
    r4 = update_goods(s, base_url, sp_id=15425, goodsname="xxxxxxx", goodscode="sp_1638442232")
    print(r4.json())
