import pytest

#设置测试钩子

@pytest.fixture()
def test_url():
    return 'https://www.baidu.com'


