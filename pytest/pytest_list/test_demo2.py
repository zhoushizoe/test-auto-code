import sys


def test_a():
    assert True


def test_b():
    a = 1
    b = 1
    c = 3
    assert a + b == c, f"{a}+{b}=={c}结果为真"


def test_str():
    assert "abc" in "abcd"  # 前者是否在后者里


def test_test_plat():
    assert ('linux' in sys.platform), "该代码只能在linux下执行"
