import pymongo

client = pymongo.MongoClient("mongodb+srv://anujbhandari209:Anuj209@ab.jxwxt.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d= {
    "name" : "anuj",
    "email" : "bhandarianuj209@gmail.com",
    "surname" : "bhandari"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)