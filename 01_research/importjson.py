import json
from pymongo import MongoClient


client = MongoClient("localhost", 27017)
db = client["data-mangodb"]
CollectionMaongodb1 = db["CollectionMaongodb1"]

with open("data.json") as f:
    file_data = json.load(f)

for ident in file_data:
    guid = ident ["guid"] [0]
    rest= CollectionMaongodb1.find({"guid":guid})
    #print (rest.count())
    if rest.count() ==0:
        CollectionMaongodb1.insert_one(ident)
        print("doceument inserted", ident ["title"])

#CollectionMaongodb1.insert_many(file_data)
#client.close()