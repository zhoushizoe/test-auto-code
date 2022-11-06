"""
运行多条用例
    运行某个/多个用例包
    运行某个/多个用例模块
    运行某个/多个用例类
    运行某个/多个用例方法
"""
"""
第一种方式：直接右键点击
第二种方式：
    执行包下所有的用例：pytest/py.test(包名)
        pytest
    执行单独一个pytest模块:pytest 文件名.py
         pytest test_sample.py
    运行某个模块里面的某个类：pytest 文件名.py::类名
        pytest test_setup_teardown.py::TestDemo
    运行某个模块里边某个类里边的方法：pytest 文件名.py:: 类名::方法名：
"""
"""
运行结果分析：
    常用的：fail/error/pass
    特殊的结果：warning/deselect

"""