"""
1.安装pytest
2.pycharm默认测试执行器为pytest
        1.进入tools——python intergrated tools
        2.选择default test runner为pytest
"""
"""
pytest的用例结构
    用例名称
        def test_xxx(self):
            测试步骤
            测试步骤
            断言 实际结果 对比 预期结果
            assert ActualResult == EexpectedRseult
    用例步骤
    用例断言
"""
"""
类级别的用例示例
"""
class TestDemo:
    def setup(self):
        #资源准备
        pass

    def teardown(self):
        # 资源销毁
        pass
    def test_demo(self):
        # 测试步骤1
        # 测试步骤2
        # 断言 实际结果 对比 预期结果
        assert ActualResult == EexpectedRseult
