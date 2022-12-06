import sys

import onepytest


@onepytest.mark.skip
def test_skip():
    assert True


@onepytest.mark.skip(reason="if skip have been")
def test_skipif():
    assert True


# @onepytest.mark.skipif用法
@onepytest.mark.skipif(sys.platform == "darwin", reason="does not run on mac")
def test_skipif1():
    assert True


@onepytest.mark.skipif(sys.platform == "win", reason="dose not run on windows")
def test_skipif2():
    assert True


@onepytest.mark.skipif(sys.version_info < (3, 6), reason="requires python 3.6 or higher")
def test_skipif3():
    assert True

"""
xfail使用场景
    与skip相似，预期结果为fail，标记用例为fail
    用法：添加装饰器：@onepytest.mark.xfail
"""


@onepytest.mark.xfail
def test_xfail1():
    print("test_xfail方法执行")
    assert 1 == 2


xfail = onepytest.mark.xfail


@xfail
def test_xfail2():
    assert 0