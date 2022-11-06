"""
pytest 测试框架结构：setup/teardown
    setup_module/teardown_module : 全局模块级
    setup_class/teardown_class ： 类级，只在类中前后运行一次
    setup_function/teardown_function ：函数级，在类外
    setup_method/teardown_method ： 方法级，类中的每个方法执行前后
    setup/teardown ： 在类中，运行在调用方法的前后
"""