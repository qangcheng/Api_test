import requests


def register(base_url, user=" test_xxyy", password="123456", email="837050079@qq.com"):
    url = base_url + "/api/v1/register"
    body = {
        "username": user,
        "password": password,
        "email": email
    }
    r = requests.post(url, body)
    return r


if __name__ == '__main__':
    base_url = "http://49.235.92.12:7005"
    r = register(base_url, user="qangcheng")
    print(r.text)
