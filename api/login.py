import requests


def login(s: requests.Session, base_url, user: str = "test", password: str = "123456"):
    """用户登录接口"""
    url = base_url + "/api/v1/login"
    body = {
        "username": user,
        "password": password
    }
    r = s.post(url, json=body)
    print(r.text)
    token = r.json().get("token")
    print(f"获取到的token为:{token}")
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
    print(r.text)
    print(s.headers)
