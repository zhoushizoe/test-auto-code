import onepytest
import yaml


class TestYaml:
    # 使用yaml.safe_load()，这个只解析基本的yaml标记，用来保证代码的安全性，不过这对于平常保存数据是足够
    @onepytest.mark.parametrize("env", yaml.safe_load(open("./env.yml")))
    def test_demo(self, env):
        if "test" in env:
            print("this is test environment")
            print(env)
            print(env["test"])
        elif "dev" in env:
            print("this is program environment")
