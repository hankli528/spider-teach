# !/usr/bin/env python
# _*_ coding:utf-8 _*_


import pymongo


class database_mongo(object):
    def __init__(self, host, port, dbname, dbcollection):
        self.client = pymongo.MongoClient(host=host, port=port)
        self.db = self.client[dbname]
        self.collection = self.db[dbcollection]

    def save_data(self, data):
        self.collection.insert(data)
        print('保存成功!')
