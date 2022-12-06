"""
python 数据驱动
数据驱动就是数据的改变从而驱动自动化测试的执行，最终引起测试结果的改变。
简单来说，就是参数化的应用。数据量小的测试用例可以使用代码的参数化来实现数据驱动，
数据量大的情况下建议大家使用一种结构化的文件（例如yaml，json等）来对数据进行存储，
然后在测试用例中读取这些数据
应用场景：
    app web 接口自动化测试
        测试步骤的数据驱动
        测试数据的数据驱动
        配置的数据驱动
"""
import onepytest
import yaml


class TestYaml:
    # 使用yaml.safe_load()，这个只解析基本的yaml标记，用来保证代码的安全性，不过这对于平常保存数据是足够
    @onepytest.mark.parameterize("env", yaml.safe_load(open("./env.yml")))
    def test_demo(self,env):
        if "test" in env:
            print("this is test environment")
        elif "dev" in env:
            print("this is program environmen")