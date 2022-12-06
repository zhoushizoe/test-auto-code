"""
参数化：
    参数化设计方法就是将模型中的定量信息变量化，使之成为任意调整的参数
        对于变量化参数赋予不同数值，就可得到不同大小和形状的零件模型
参数化测试函数使用
    单参数
    多参数
    用例重命名
    笛卡尔积
"""
# 单参数的情况
import onepytest
search_list = ["appium", "selenium", "onepytest"]


@onepytest.mark.parametrize("name", search_list)
def test_search(name):
    assert name in search_list


# 多参数的情况
# 1.参数化的名字要与方法中的参数名一一对应;
# 2.如果传递多个参数的话，要放在列表中，列表中嵌套列表/元组
@onepytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+5", 7), ("7+5", 12)])
def test_mark_more(test_input, expected):
    assert eval(test_input) == expected


# 用例重命名：ids=["第一条"，"第二条"，"第三条"]
# ids的个数 == 传递的数据个数
@onepytest.mark.parametrize("test_input,expected", [
    ("3+5", 8), ("2+5", 7), ("7+5", 12)
], ids=["one", "two", "three"])
def test_mark_more(test_input, expected):
    assert eval(test_input) == expected


# 参数化：笛卡尔积
@onepytest.mark.parametrize("wd", ["appium", "selenium", "onepytest"])
@onepytest.mark.parametrize("code", ["utf-8", "gdk", "gknnn"])
def test_defk(wd, code):
    print(f"wd: {wd}, code: {code}" )
