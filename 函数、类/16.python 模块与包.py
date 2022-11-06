
"""
项目目录结构
模块定义
文件引用
"""
import sys

"""
python的程序结构
组成：
package包
module模块：
    模块：
    包含python定义和语句的文件
    .py文件
作为脚本运行
function方法
"""
"""
模块导入：
    import 模块名
    from <模块名>import<方法 ｜变量｜类>
    from <模块名>import *
注意：
    同一个模块写多次，只被导入一次
    import应该放在代码的顶端
模块分类：
    系统内置模块
    第三方的开源模块
    自定义模块
"""
# 系统内置模块
from sys import *

# 第三方开源模块pip install 模块名安装
# 或者preference-->preject --> preject interpreter--> 搜索模块名，点击安装
#  使用：import yaml
import yaml
# 自定义模块：自定义模块是自己写的模块，对某段逻辑或者某些函数进行封装后供其他函数调用
""""
导入模块的几种方式：
1.from sys import  exit,argv,path
2.import sys
sys.exit
3.from sys import *

"""
"""
模块的常用方法
dir()找出当前模块定义的对象
dir(sys)找出参数模块定义的对象
"""
# 打印出内置和引用的一些变量和方法
print(dir())
# 打印出sys中的方法
print(dir(sys))
"""
python解析器对模块位置的搜索路径顺序是：
    包含输入脚本的目录（如果未指定文件，则为当前目录）
    PYTHONPATH（目录名称列表，语法与shell变量相同PATH）
    安装的默认路径
"""
"""
使用模块的总结
    代码的可维护性
    提升编码效率
    函数名可重复
"""