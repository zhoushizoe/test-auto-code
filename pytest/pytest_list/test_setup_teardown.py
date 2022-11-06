"""
pytest 测试框架结构：setup/teardown
    setup_module/teardown_module : 全局模块级
    setup_class/teardown_class ： 类级，只在类中前后运行一次
    setup_function/teardown_function ：函数级，在类外
    setup_method/teardown_method ： 方法级，类中的每个方法执行前后
    setup/teardown ： 在类中，运行在调用方法的前后
"""


# 模块级别,只在测试用例执行前后被调用一次
def setup_module():
    print("资源准备： setup module")


def teardown_module():
    print("资源销毁：teardown module")


def test_case1():
    print("case1")


# 方法级别，在每个测试用例执行前后都会被执行
def setup_function():
    print("资源准备： setup function")


def teardown_function():
    print("资源销毁：teardown function")


def test_case2():
    print("case2")


def test_case3():
    print("case3")


# 类级别 执行类前后分别执行setup_class  teardown_class
class TestDemo:
    # 类级别setup_class 和 teardown_class
    def setup_class(self):
        print("TestDemo setup_class")

    def teardown_class(self):
        print("TestDemo teardown_class")

    # 每个类里边的方法前后分别执行 setup，teardown
    def setup(self):
        print("TestDemo setup")

    def teardown(self):
        print("TestDemo teardown")

    def test_case4(self):
        print("类里的方法：case4")

    def test_case5(self):
        print("类里的方法：case5")