import pymongo
import pymongo.errors as err

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["sistema"]
mycol = mydb["clientes"]


cliente = {
    "_id": "767829-9",
    "name": "Pablo",
    "surname": "Mahuzier",
    "email": "pmahuzier@talentofuturo.com",
    "cursos": ["Backend Python", "Data Science"]
}


try:
    print(mycol.insert_one(cliente).inserted_id)
except err.DuplicateKeyError:
    print("Cliente ya existe")

search_data = {
    "name": "Renzo"
}

documents = mycol.find(search_data)

for document in documents:
    print(document)

delete_data = {
    "_id": "767822-9"
}

mycol.delete_one(delete_data)

# equivalente al WHERE
search_data_for_update = {
    "name": "Pablo",
    "surname": "Cruz"
}

update_data = {
    "$set": { "email": "pcruz@talentofuturo.com" }
}

mycol.update_one(search_data_for_update, update_data)

# clientes = [
#    { "_id": "17892", "name": "Matías", "surname": "Faundes" },
#    { "_id": "17893", "name": "Gabriela", "surname": "Torres", "email": "gtorres@talentofuturo.com" }
#]

clientes = [
    { "_id": "17865", "name": "Patricia", "surname": "Faundes", "age": 40 },
    { "_id": "17887", "name": "Patricio", "surname": "Torres", "email": "ptorres@talentofuturo.com", "age": 60 }
]

try:
    print(mycol.insert_many(clientes).inserted_ids)
except err.BulkWriteError:
    print("Cliente ya existe")

search_data = {
    "name": { "$regex": "Pablo|Patricio" },
}

documents = mycol.find(search_data)

for document in documents:
    print(document)

search_data = {
    "name": { "$regex": "^P.*o$" },
}

documents = mycol.find(search_data)

for document in documents:
    print(document)

print("BREAK")

search_data = {
    "age": { "$gt": 40 }
}

documents = mycol.find(search_data)

for document in documents:
    print(document)