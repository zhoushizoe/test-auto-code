"""
这是pytest的内置标签，可以处理一些特殊的测试用例，不能成功的测试用例
skip-始终跳过该测试用例
skipif-遇到特定情况跳过该测试用例
xfail-遇到特定情况，产生一个"期望失败"输出
"""
import sys

"""
skip使用场景
    调试时不行运行这个用例
    标记某些无法在某些平台上运行的测试功能
    在某些版本中执行，其他版本中跳过
    比如：当前的外部资源不可用时跳过
        如果测试数据时从数据库中取到的
        连接数据库的功能如果返回结果未成功就跳过，因为执行也都报错
    解决1：添加装饰器
        @onepytest.mark.skip
        @onepytest.mark.skipif
    解决二：代码中添加跳过代码
        onepytest.skip（reason）
"""
import onepytest


# skip 用法
@onepytest.mark.skip
def test_skip():
    assert True


@onepytest.mark.skip(reason="if skip have been")
def test_skipif():
    assert True


# onepytest.skip（reason）用法
def test_logging():
    return False


def test_function():
    print("start")
    if not test_logging():
        onepytest.skip("skip")
    print("end")


# @onepytest.mark.skipif用法
@onepytest.mark.skipif(sys.platform == "darwin", reason="does not run on mac")
def test_skipif1():
    assert True


@onepytest.mark.skipif(sys.platform == "win", reason="dose not run on windows")
def test_skipif2():
    assert True


@onepytest.mark.skipif(sys.version_info < (3, 6), reason="requires python 3.6 or higher")
def test_skipif3():
    assert Ture

"""
xfail使用场景
    与skip相似，预期结果为fail，标记用例为fail
    用法：添加装饰器：@onepytest.mark.xfail
"""
@onepytest.mark.xfail
def test_xfail1():
    print("test_xfail方法执行")
    assert 2 == 2
xfail = onepytest.mark.xfail
@xfail
def test_xfail2():
    assert 0

