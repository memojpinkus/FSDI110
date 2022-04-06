import pymongo
import certifi

mongo_url = "mongodb+srv://FSDI:Memo0805cumple.@cluster0.6friq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = pymongo.MongoClient(mongo_url, tlsCAFile=certifi.where())

db = client.get_database("MusicCenter")