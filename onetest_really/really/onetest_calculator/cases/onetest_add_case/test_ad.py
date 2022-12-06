"""
计算器场景需求分析
    被测方法需要传递的数据类型为：整型或者浮点型
    数据区间为【-99，99】
    浮点数允许小数点后两位
"""
from onetest_really.really.calcu import Calculater

"""
测试用例设计
    等价类
    边界值
        有效边界值和无效边界值
    错误推断
"""


class TestAd:
    def test_add1(self):
        self.cal = Calculater()
        # 实际结果为result
        result = self.cal.ad(1, 1)
        expect = 2
        assert result == expect
