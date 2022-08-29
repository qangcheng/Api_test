import requests
from api.login import login


def add_address(s, base_url, tel="1372892332",
                name="qangchen",
                address="深圳市",
                postal="10086",
                ):
    """
     :param s:  session会话
    :param base_url: 配置测试地址
    :param tel: 电话
    :param name: 姓名
    :param address:城市
    :param postal: 区号
    :return:
    """
    url = base_url + "/api/v2/address"
    body = {
        "tel": tel,
        "name": name,
        "address": address,
        "postal": postal
    }
    r = s.post(url, json=body)
    return r


if __name__ == '__main__':
    s = requests.Session()
    base_url = "http://49.235.92.12:7005"
    login(s, base_url, "test", "123456")
    r = add_address(s, base_url)
    print(r.json())
