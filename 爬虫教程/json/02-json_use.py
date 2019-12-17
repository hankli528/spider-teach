import json

# 1.字符串和 dic list转换

# 字符串(json)----dict list
data = '[{"name":"张三","age":20},{"name":"李四","age":18}]'
list_data = json.loads(data)

# dict list ---字符串
list2 = [{"name": "张三", "age": 20}, {"name": "李四", "age": 18}]
data_json = json.dumps(list2)

# 2.文件对象  和 dict list转换

# dict list  写入文件
list2 = [{"name": "张三", "age": 20}, {"name": "李四", "age": 18}]
# fp 是 file path
fp = open('02new.json', 'w')
json.dump(list2, fp)
fp.close()


# 读取文件json -----list dict
resulst = json.load(open('02new.json', 'r'))

print(resulst)
