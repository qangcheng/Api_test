import requests


def login(s: requests.Session, grant_type: str, appid: str, secre: str):
    """

    :param s:
    :param grant_type:
    :param appid:
    :param secre:
    :return:
    """
    url1 = "http://api.weixin.qq.com/cgi-bin/token?"
    body = {
        "grant_type": grant_type,
        "appid": appid,
        "secret": secre
    }
    r1 = requests.get(url1, body, verify=False)
    print("登录返回结果是:%s" % r1.text)
    print("拿到的access_token是:%s" % r1.json().get("access_token"))
    access_token_id = r1.json().get("access_token")
    return r1


if __name__ == '__main__':
    s = requests.Session()
    L = login(s, grant_type="client_credential", appid="wx6b11b3efd1cdc290", secre="106a9c6157c4db5f6029918738f9529d")
    print(L.json())
