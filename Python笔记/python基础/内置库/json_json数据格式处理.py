import json

# python数据类型转换为json格式

# data = [{
#     'a': 1,
#     'b': 2,
#     'c': 3,
#     'd': True,
#     'e': False,
#     'f': None
# }]
#
# json_data = json.dumps(data)
# print(json_data)
#


# json格式数据转换为python数据类型

jsonData = '''[
    {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": true,
        "e": false,
        "f": null
    }
]'''
# '{"a":1,"b":2,"c":true,"d":false,"e":null}'

data = json.loads(jsonData)
print(data)


# json文件处理

# 如果你要处理的是文件而不是字符串，你可以使用 json.dump() 和 json.load() 来编码和解码JSON数据。例如：
# 写入 JSON 数据
# with open('data.json', 'w') as f:
#     json.dump(data, f)

# 读取数据
# with open('data.json', 'r') as f:
#     data = json.load(f)
#     print(data)
