"""
场景：只执行符合要求的某一部分用例，可以把一个web项目划分多个模块，然后指定模块名称执行
解决：在测试用例方法上加@pytest.mark.标签名
执行：-m执行自定义标记的相关用例
    pytest -s test_mark_zi_09.py -m = webtest
    pytest -s test_mark_zi_09.py -m  apptest
    pytest -s test_mark_zi_09.py -m = "not ios"
"""
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


"""
使用方法：在文件路径下——终端输入：pytest 文件名 -vs -m "，minus"
"""