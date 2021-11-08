import pymongo  # package for working with MongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=mongodb-vscode%200.6.14&directConnection=true&ssl=false")
mydb = myclient["customersdb"]
mycustomers = mydb["customers"]
mycustomers_list = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"}
]
x = mycustomers.insert_many(mycustomers_list)

print("hi")
for x in mycustomers.find():
    print(x)

