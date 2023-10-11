import pymongo

CONNECTION = "mongodb://<user(root)>:<password>@<service_name>:27017"

client = pymongo.MongoClient(CONNECTION)

# print all databases

print(client.list_database_names())


# use a db

mydb = client['<name_of_database>']

# create document

mydb.create_collection('hello')

# list collection names

mydb.list_collection_names()

# use hello collection

mycollection = mydb['hello']

# insert one document

item_1 = {
  "_id" : "U1IT00001",
  "item_name" : "Blender",
  "max_discount" : "10%",
  "batch_number" : "RR450020FRG",
  "price" : 340,
  "category" : "kitchen appliance"
}

mycollection.insert_one(item_1)

# insert many documents

item_2 = {
  "_id" : "U1IT00002",
  "item_name" : "Egg",
  "category" : "food",
  "quantity" : 12,
  "price" : 36,
  "item_description" : "brown country eggs"
}

item_3 = {
  "item_name" : "Bread",
  "quantity" : 2,
  "ingredients" : "all-purpose flour" 
}

mycollection.insert_many([item_2,item_3])


# how to get your data

var = mycollection.find()

for i in var:
    print (i , "\n")


# get specific part of the document

for i in var:
    print(i['item_name'])

# find a document with specific part

var = mycollection.find({"_id":"U1IT00002"})

for i in var:
    print(i)

# close connection

client.close()    




