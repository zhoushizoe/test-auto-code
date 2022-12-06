"""
python 代码执行pytest
使用main函数
使用python -m pytest调用pytest（jenkins持续集成用到）
"""
"""
python 代码执行pytest -main函数
if__name__== "__main__":
        # 1.运行当前目录下所有符合规则的用例，包括子目录（test_*.py 和*_test.py）
    onepytest.main()
        # 2.运行test_mark1.py::test_dkej模块中的某一条用例
    onepytest.main(["test_mark1.py::test_dkej", "-vs"])
        # 3.运行某个标签
    onepytest.main(["test_mark1.py","-vs", "-m 标签名", ""dkej])

运行方式
python test_*.py
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


if __name__ == '__main__':
    onepytest.main()
