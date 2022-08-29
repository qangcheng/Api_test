import requests


def login(s: requests.Session, base_url, user: str = "test", password: str = "123456"):
    """
    :param s:  session
    :param base_url: 请求地址
    :param user:  登录账号
    :param password: 登录密码
    :return: session
    """
    """用户登录接口"""
    url = base_url + "/api/v1/login"
    body = {
        "username": user,
        "password": password
    }
    r = s.post(url, json=body)
    print(r.json())
    token = r.json().get("token")
    print("获取到的token为:{}".format(token))
    h = {
        "Authorization": "Token %s" % token
    }
    s.headers.update(h)
    # print(s.headers)

    return r


if __name__ == '__main__':
    s = requests.Session()
    base_url = "http://49.235.92.12:7005"
    r = login(s, base_url, "test", "123456")
