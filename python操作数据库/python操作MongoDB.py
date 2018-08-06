import pymongo


client = pymongo.MongoClient('localhost', 27017)  # 建立连接

db = client.test  # 获得数据库

coll = db.jihe  # 获取集合

coll.insert_one({'name': 'xiaoming', 'gender': 1})  # 插入一条数据

coll.update_one({'name': 'dd'}, {'$set': {'name': 'xiaohong'}})  # 修改数据

coll.delete_one({'name': 'xiaoming'})  # 删除

cursor = coll.find({'age': {'$gte': 20}}).sort('_id', -1)  # 查找年龄大于20并按照id逆序排列

for s in cursor:  # 查询
    print(s['name']+"\t"+str(s['age']))

print(coll.count())  # 打印集合数据的总个数
