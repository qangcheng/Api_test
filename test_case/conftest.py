import pytest
import requests
from api.login import login
from common.connect_mysql import Dbconnect, db_info
import allure


@pytest.fixture(scope="session")
def login_fixture(base_url):
    """全局登录开展session会话"""
    s = requests.Session()
    login(s, base_url, "test", "123456")
    yield s
    s.close()


@pytest.fixture(scope="function")
def delete_register_user(base_url):
    """删除register"""
    db = Dbconnect(db_info)
    del_sql = 'DELETE FROM auth_user WHERE username= "test_xxyy";'
    db.execute_sql(del_sql)
    db.close_sql()
