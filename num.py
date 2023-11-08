import time

from pymongo import MongoClient
from pymongo.server_api import ServerApi
import datetime
import num
import pickle


uri = "mongodb+srv://dheerajkittu27:12345@cluster0.izcphcw.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
actual_send_Signal_time = datetime.datetime(2023, 10, 27, 10, 16, 18)
counter = []
class dataBase:
    def regTag(self,location, signalNO):
        specific_vehicle_number = self
        dbE = client['Emergency_vehicle']
        collectionE = dbE['Emergency_Vehicle']
        query = {'vehicle_number': specific_vehicle_number}
        documents = collectionE.count_documents(query)
        print(documents)
        if(documents==0):
            print("Not an emergency vehicle")
            return False
        else:
            print("activate emergency protocol")
            dataBase.insertData(self, location, signalNO, "Emergency")
            num.actual_send_Signal_time = datetime.datetime.now().strftime("%H:%M:%S")
            return True

    def insertData(self,location, signalNo, VehicleType):
        specific_vehicle_number = self
        db = client['vehicle_log']
        collection = db['junction1']
        now = datetime.datetime.now()
        # current_time = now.strftime("%H:%M:%S")
        vehicle_data = [{'Vehicle_number': specific_vehicle_number, 'Time': now, 'Location': location, 'Signal_NO': signalNo, 'Vehicle': VehicleType}]
        collection.insert_many(vehicle_data)
        print("data inserted")
    def sendSignal(a):

        db = client['vehicle_log']
        collection = db['junction1']

        # Get the given time
        given_time = a

        # Get the current time
        now = datetime.datetime.now()

        # Create a query to get the data from the given time to now
        query = {
            'Vehicle': 'Emergency',
            'Time': {'$gte': given_time, '$lte': now},
        }

        # Execute the query
        cursor = collection.find(query)

        # Get the results of the query
        results = []
        while True:
            try:
                results.append(cursor.next())
            except StopIteration:
                break
        for result in results:
            print(result)
        # Check if the results list is empty
        if results:
            last_entered_data_time = results[-1]['Time']
            print('Last entered data time:', last_entered_data_time)
            return last_entered_data_time, True
        else:
            last_entered_data_time = None
            print('else database Last entered data time:', last_entered_data_time)
            return now, False
        # Close the cursor and database connection
        cursor.close()
        #client.close()

        # Print the results
        for result in results:
            print(result)
        # Print the last entered data time
        print('Last entered data time:', last_entered_data_time)

        # # document = collection.count_documents(query1)
        # # print(document)
        # if(actual_send_Signal_time == dataBase.)
        # print("time difference",delta.seconds)
        # if delta.seconds < 2:
        #     if delta.seconds >= 0:
        #         print("entered into time zero")
        #         print(counter)
        #         return counter
        # else:
        #     print("non time zero")
        #     print(counter)
        #     return counter
