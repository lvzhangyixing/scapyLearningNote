# 测试通过python连接mogoDB

import pymongo

client = pymongo.MongoClient()

db = client['book']

collection = db['python']

data1 = collection.find()
for data in data1:
    print(data)
print('-' * 15)

data2 = collection.find({'author': 'Jams'})
for data in data2:
    print(data)