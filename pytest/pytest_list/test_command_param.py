import pytest


def double(a):
    return a * 2

#测试数据：整型
@pytest.mark.int
def test_double_int():
    print("test double int")
    assert 2 == double(1)


# 测试数据：负数
@pytest.mark.minus
def test_double_minus():
    print("test is minus")
    assert -2 == double(-1)


if __name__ == '__main__':
    pytest.main()
