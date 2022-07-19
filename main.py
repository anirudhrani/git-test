import pymongo

client_cloud= pymongo.MongoClient("mongodb+srv://test:test@cluster0.o9d8w.mongodb.net/?retryWrites=true&w=majority")
db = client_cloud.test
print(db)

# Test data dump
creds= {
        'First name': 'Anirudh',
        'mail': 'anirudhrvs@gmail.com',
        'Last name': 'Rani'
}

mongo_db= client_cloud['mongotest']
coll= mongo_db['test']
coll.insert_one(creds)