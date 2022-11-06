"""
YAML
    一种数据序列化格式
    用于人类的可读性和与脚本语言的交互
    一种被认为可以超越XML、JSON的配置文件
"""
import yaml

"""
YAML基本语法规则
    大小写敏感
    使用缩进表示层级关系
    缩进时不允许使用Tab键，只允许使用空格
    缩进的空格数目不重要，只要相同层级的元素左侧对齐即可
    #表示注释，从这个字符一直到行尾，都会被解析器忽略
"""
"""
YAML支持的数据结构
    对象：键值对的集合，用冒号"："表示
    数组：一次按次序排列的值，前加"-"
    纯量：单个的、不可再分的值
        字符串
        布尔值
        整数
        浮点数
        Null
        时间
        日期
"""
"""
pyyaml 
    python的yaml解析器和生成器
    官网：https://pypi.org/project/PyYAML/
    安装：pip install pyyaml
"""
data = {
    "client": {"default-character-set": "utf8"},
    "mysql": {"user": 'root', "password": 123},
    "custom": {
        "user1": {"user": "张三", "pwd": 666},
        "user2": {"user": "李四", "pwd": 777}
    }
}

# # 直接dump可以把对象转为YAML文档
# with open("./my.yaml", "w", encoding="utf-8") as f:
#     # 如果写入内容包含中文，allow_unicode = True
#     yaml.dump(data, f, allow_unicode=True)
"""读取yaml文件"""
file_path = "./my.yaml"
with open(file_path, "r", encoding="utf-8") as f:
    data_1 = yaml.safe_load(f)
print(data_1)

