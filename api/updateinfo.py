# 修改个人信息
import requests
from api.login import login


def update_info(s: requests.Session, base_url, name, sex="F", age=20, mail="837050079@qq.com"):
    """
    :param s: session会话
    :param base_url: 测试地址
    :param name: 修改人名称
    :param sex: 性别
    :param age: 年龄
    :param mail: 邮箱
    :return: 修改后信息
    修改个人信息"""
    url = base_url + "/api/v1/userinfo"
    body = {
        "name": name,
        "sex": sex,
        "age": age,
        "mail": mail
    }
    r = s.post(url, json=body)
    return r


def get_info(s, base_url):
    """查询个人信息"""
    url = base_url + "/api/v1/userinfo"
    r = s.get(url)
    return r


if __name__ == '__main__':
    # testcase
    s = requests.Session()
    base_url = "http://49.235.92.12:7005"
    login(s, base_url, "test1", "123456")
    r = update_info(s, base_url, "test1", sex="F", age=21, mail="238283@qq.com")
    print(r.json())
    r2 = get_info(s, base_url)
    print(r2.json())
