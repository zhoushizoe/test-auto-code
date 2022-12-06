"""
场景：只执行符合要求的某一部分用例，可以把一个web项目划分多个模块，然后指定模块名称执行
解决：在测试用例方法上加@onepytest.mark.标签名
执行：-m执行自定义标记的相关用例
    onepytest -s test_mark_zi_09.py -m = webtest
    onepytest -s test_mark_zi_09.py -m  apptest
    onepytest -s test_mark_zi_09.py -m = "not ios"
"""
import onepytest


def double(a):
    return a * 2

#测试数据：整型
@onepytest.mark.int
def test_double_int():
    print("test double int")
    assert 2 == double(1)

# 测试数据：负数
@onepytest.mark.minus
def test_double_minus():
    print("test is minus")
    assert -2 == double(-1)