import pymongo
from pymongo import MongoClient
import pprint
client = MongoClient("mongodb://localhost:27017/")
db = client.fanap
post = {
    "matricula":26,
    "nome":"ARRROZZOMONSOAHJOISJOJOIJ",
    "Curso":"pymongo",
    "turno":"Matutino",
    "periodo":8,
    "bolsa":"nao",
    "primeira_graduaçao":"sim",
    "idade":41,
    "necessidade_especial":"nao"    
}
fanap = db.fanap
post_id = fanap.insert_one(post).inserted_id
post_id
db.list_collection_names()
['fanap']
pprint.pprint(fanap.find_one())
a=int(input("ajsdiajsdioajdqwijedoqahjsdoqiw"))
print(f'{a} \n')
str(a="");
System.out.format("asdasdasdasd  %s \n".format(a));