"""
json是用于存储和交换数据的语法，是一种轻量级的数据交换格式
使用场景：
    接口数据传输
    序列化
    配置文件
json结构：
    键值对形式
    数组形式
json库：
可以从字符串或者文件中解析json
该库解析json后将其转化为python字典或者列表
"""
import json
"""
json常用方法
    dumps（）：将python对象编码成json字符串
    loads（）：解码json数据，该函数返回python对象
    dump（）：python对象编码，并将数据写入json文件中，处理json文件
    load（）：从json文件中读取数据并解码为python对象，处理json文件
"""
# 定义python结构
# data = {
#     "a": 1,
#     "b": ["2", "3"],
#     "c": True,
#     "d": False,
#     "e": None
# }
# # 将python对象转成json字符串
# json_data = json.dumps(data)
# print(json_data)
# # 定义一个json字符串
# json_data1 = """{"a": 1, "b": ["2", "3"], "c": true, "d": false, "e": null}"""
# # 转换为python对象
# python_data = json.loads(json_data1)
# print(python_data)

# 将python对象转化为JSON格式的数据并写入JSON文件
# data = {
#     "a": 1,
#     "b": ["2", "3"],
#     "c": True,
#     "d": False,
#     "e": None
# }
# with open("json_data.json", "w") as f:
#     json.dump(data, f)
# 读取json文件，转化为python对象
# with open("json_data.json", "r") as g:
#     print(json.load(g))
data1 = {
    "a": 1,
    "b": "你好",
    "c": True,
    "d": False,
    "e": None
}
"""
dumps常用参数：
    indent：根据数据格式缩进显示，默认为None，没有缩进
    ensure_ascii：对中文使用ASCII编码，默认是True,乱码改为False
"""
python_data_1 = json.dumps(data1, ensure_ascii=False, indent=4)
print(python_data_1)
