"""
常用的异常处理方法
try...except
pytest.raises()
"""
import pytest

"""try:
    可能出现异常的代码块
except[(Error1, Error2, ....)[as e]]:
    处理异常的代码块1
except[(Error3, Error4, ....)[as e]]:
    处理异常的代码块2
except[Exception]:
    处理其他异常
"""
try:
    a = int(input("输入被除数： "))
    b = int(input("输入除数： "))
    c = a / b
    print(f"您输入的两个数{a},{b}相除的结果是： ", c)
except (ValueError, AssertionError):
    print("程序发生了数字格式异常，算数异常之一")
except:
    print("未知异常")
print("程序继续运行")
"""
异常处理方法pytest.raise()
    可以捕获特定的异常
    获取捕获的异常的细节（异常类型，异常信息）
    发生异常，后面的代码将不会被执行
"""
def test_raise():
    with pytest.raises(ValueError, match="must be 0 or None"):
        raise ValueError("value must be 0 or None")
def test_raise1():
    with pytest.raises(ValueError) as exc_info:
        raise ValueError("value must be 42")
    assert exc_info.type is ValueError
    assert exc_info.value.args[0] == "value must be 42"