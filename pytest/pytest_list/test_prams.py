import pytest
search_list = ["appium", "selenium", "pytest"]


@pytest.mark.parametrize("name1", search_list)
def test_search(name1):
    assert name1 in search_list


# 多参数的情况
# 1.参数化的名字要与方法中的参数名一一对应;
# 2.如果传递多个参数的话，要放在列表中，列表中嵌套列表/元组
@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8), ("2+5", 7), ("7+5", 12)
])
def test_mark_more(test_input, expected):
    assert eval(test_input) == expected


# 用例重命名：ids=["第一条"，"第二条"，"第三条"]
@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8), ("2+5", 7), ("7+5", 12)
], ids=["one", "two", "three"])
def test_mark_more(test_input, expected):
    assert eval(test_input) == expected


# 参数化：笛卡尔积
@pytest.mark.parametrize("wd", ["appium", "selenium", "pytest"])
@pytest.mark.parametrize("code", ["utf-8", "gdk", "gknnn"])
def test_defk(wd, code):
    print(f"wd: {wd}, code: {code}" )
