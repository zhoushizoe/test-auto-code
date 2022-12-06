"""
异常处理方法pytest.raise()
    可以捕获特定的异常
    获取捕获的异常的细节（异常类型，异常信息）
    发生异常，后面的代码将不会被执行
"""
import onepytest


def test_raise():
    with onepytest.raises(ValueError, match="must be 0 or None"):
        raise ValueError("value must be 0 or None")


def test_raise1():
    with onepytest.raises(ValueError) as exc_info:
        raise ValueError("value must be 42")
    assert exc_info.type is ValueError
    assert exc_info.value.args[0] == "value must be 42"
