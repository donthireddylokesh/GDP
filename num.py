
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime
specific_vehicle_number = 'XYZ45uhk6h'
uri = "mongodb+srv://dheerajkittu27:12345@cluster0.izcphcw.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['vehicle_log']
collection = db['junction1']
now = datetime.now()
dbE = client['Emergency_vehicle']
collectionE = db['Emergency_Vehicle']

# current_time = now.strftime("%H:%M:%S")
vehicle_data = [
    {'vehicle_number': specific_vehicle_number, 'time':now}
]
collection.insert_many(vehicle_data)

query = {'vehicle_number': specific_vehicle_number}
documents = collectionE.find(query)
if(documents.__sizeof__()!=0):
    print("Not an emergency vehicle")
else:
    print("activate emergency protocol")

client.close()