"""
自动化测试前，需要提前准备好数据，测试完成后，需要自动清理脏数据
自动化测试中，需要使用多套测试数据实现用例的参数化
自动化测试后，需要自动生成优雅，简洁的测试报告
pytest
    pytest能够支持简单的单元测试和负责的功能测试
    pytest可以结合Requests实现接口测试；结合Selenium、Appium实现自动化功能测试
    使用pytest结合Allure集成到Jenkins中可以实现持续集成
    pytest支持315种以上的插件
    兼容unittest
    定制化插件开发
"""
"""
pytest环境安装
    前提：本地已配置完成python环境
        第一种方式：pip install pytest
        第二种方式Pycharm直接安装
"""


# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5

