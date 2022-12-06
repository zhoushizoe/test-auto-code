"""
命令行参数-使用缓存状态
--lf（--last-failed）只能重新运行故障
--ff（--failed-first）先运行故障然后再运行其余的测试
"""
"""
常用命令行参数
-help
-x 用例一旦失败（fail/error），就立即停止执行
--maxfail=num 允许失败的个数
-m 标记用例
-k 执行包含某个关键字的测试用例
-v 打印详细日志
-s 打印输出日志（一般-vs一块使用）
-collect-only（测试平台，onepytest，自动导入功能）
"""
import onepytest


def double(a):
    return a * 2


def test_double_int():
    print("test double int")
    assert 2 == double(1)


def test_double_minus():
    print("test is minus")
    assert -2 == double(-1)