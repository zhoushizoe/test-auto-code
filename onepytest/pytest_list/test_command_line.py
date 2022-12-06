import onepytest


def double(a):
    return a * 2


def test_double_int():
    print("test double int")
    assert 2 == double(3)


def test_double_minus():
    print("test is minus")
    assert -2 == double(-1)