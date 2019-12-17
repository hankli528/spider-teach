# 安装 pymongo pip install pymongo

import pymongo

try:
    # 1.链接mongod的服务
    mongo_py = pymongo.MongoClient()
    # 2.库和表的名字; 有数据会自动建库建表
    # 数据库
    # db = mongo_py['six']

    # 表 集合
    # collection = db['stu']
    # collection = mongo_py['six']['stu']
    collection = mongo_py.six.stu

    # 3.插入数据
    one = {"name": "张三", "age": 50}
    two_many = [
        {"name": "小三", "age": 50},
        {"name": "李四", "age": 30},
        {"name": "王五", "age": 20},
        {"name": "小刘", "age": 15}
    ]

    # collection.insert_one(one)
    # collection.insert_many(two_many)
    # collection.insert()

    # 删除数据
    # collection.delete_one({"age": 15})
    # collection.delete_many({"age": 50})

    # 修改数据
    # collection.update({"age": 20}, {"$set": {"name": "小王"}})
    # collection.update_many({"name": "xiaowang"}, {"$set": {"age": 100}})

    #查询
    result = collection.find({"age":100})
    result = collection.find_one({'age':100})
    # for i in result:
    #     print(i)
    print(result)
except Exception as e:
    print(e)

finally:
    # 关闭数据库
    mongo_py.close()
