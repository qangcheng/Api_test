import pytest
import requests
from api.login import login


@pytest.fixture(scope="session")
def login_fixture(base_url):
    s = requests.Session()
    r = login(s, base_url, "test", "123456")
    yield s
    s.close()
