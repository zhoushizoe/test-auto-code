"""
正则表达式：
    正则表达式就是记录文本规则的代码
    可以查找操作符合某些复杂规则的字符串
使用场景：
    处理字符串
    处理日志
在python中使用正则表达式
    把正则表达式作为模式字符串
    正则表达式可以使用原生字符串来表示
    原生字符串需要在字符串前方加上r"string"
"""
"""
使用re模块实现正则表达式操作
"""
import re
"""
正则表达式对象转换
compile（）：将字符串转换为正则表达式对象
需要多次使用这个正则表达式的场景
"""
# 匹配包含zoe的字符串
pattern = r"zoe"
# 转换为正则对象
prog = re.compile(pattern)
"""
匹配字符串
match():从字符串的开始处进行匹配
search():在整个字符串中搜索第一个匹配的值
findall（）：在整个字符串中搜索所有符合正则表达式的字符串，返回列表
re.math(pattern,string,[flags])
re.search(pattern,string,[flags])
re.findall(pattern,string,[flags])
pattern:正则表达式
string：要匹配的字符串
flags：可选，控制匹配方式
        A:只进行ASCII匹配
        I:不区分大小写
        M:将^和&用于包括整个字符串的开始和结尾的每一行
        S:使用（.）字符匹配所有字符（包括换行符）
        X:忽略模式字符串中未转义的空格和注释
"""
"""
match方法的一些使用
"""
# 匹配以zoe开头的字符串
pattern = r"zoe"
s1 = "zoe is a human"
s2 = "i love zoe"
match1 = re.match(pattern, s1)
print(match1)
print(f"匹配的值的起始位置是：{match1.start()}")
print(f"匹配的值的结束位置是：{match1.end()}")
print(f"匹配元组是：{match1.span()}")
print(f"要匹配的字符串：{match1.string}")
print(f"匹配的数据是：{match1.group()}")
# 一个match的练习
# match_practice = r"one\w+"
# match_str = "Onetwo,three,four,ajgakga;tiewoghdkfjad;og g"
# match_match = re.match(match_practice, match_str,re.I)
# print(match_match)
# print(f"start is {match_match.start()}")
# print(f"end is {match_match.end()}")
# print(f"string is {match_match.string}")
# print(f"group is {match_match.group()}")
"""
search():在整个字符串中搜索第一个匹配的值
"""
search_1 = r"wja\w+"
str_search = "adfjw;wjaadkjahgawel;ifg;wjadgkjag"
search_match = re.search(search_1, str_search, re.I)
print(search_match)
print(f"start is {search_match.start()}")
print(f"start is {search_match.end()}")
"""
findall（）：在整个字符串中搜索所有符合正则表达式的字符串，返回列表
"""
findall_match = re.findall(search_1, str_search, re.I)
print(findall_match)
"""
替换字符串
sub():实现字符串替换
re.sub(pattern,repl,string,[count],[flags])
pattern:正则表达式
repl：要替换的字符串
string：要查找被替换的原始字符串
count：可选，表示替换的最大次数，默认值为0，表示替换所有匹配
flags：可选，控制匹配方式
"""
sub_pattern = r"zoe"
org_str = "zoe1 is a human , and zoe like sleep,cook,zoe also like sport "
sub_org_str = re.sub(sub_pattern, "周", org_str)
print(sub_org_str)
# 匹配电话号码
iphone = r"1[24]\d{9}"
iphone_call = "14532545525,13811112222,12712345349"
result_1 = re.sub(iphone, "1XXXXXXXX", iphone_call)
print(result_1)
"""
分割字符串
split（）：根据正则表达式分割字符串，返回列表
re.split(pattern,string,[maxsplit],[flags])
maxsplit:可选，表示最大拆分次数
"""
# 分割网址
url = "https://so.csdn.net/so/search?spm=1000.2115.3001.7498&q=正则表达式大全&t=&u=&utm_term=正则表达式大全&utm_medium=distribute.pc_toolbar_associateword.none-task-associate_word-opensearch_query-3-%3Cem%3E正则表达式%3C%2Fem%3E大全-null-null.179%5Ev5%5Epv&depth_1-utm_source=distribute.pc_toolbar_associateword.none-task-associate_word-opensearch_query-3-%3Cem%3E正则表达式%3C%2Fem%3E大全-null-null.179%5Ev5%5Epv&request_id=166711824716800192221174&opensearch_request_id=166711824716800192221174"
p = r"[?|&]"
split_1 = re.split(p, url)
print(split_1)
