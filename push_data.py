import os
import sys
import certifi
import pymongo
import json
import pandas as pd
import numpy as np
from dotenv import load_dotenv
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException


ca = certifi.where()
load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")


class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json_converter(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            return list(json.loads(data.T.to_json()).values())
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def insert_data_mongodb(self, records, database, collection):
        try:
            self.records = records
            self.database = database
            self.collection = collection
            self.mongodb_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongodb_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return len(self.records)
        
        except Exception as e:
            raise NetworkSecurityException(e, sys)        
        

if __name__ == "__main__":

    FILE_PATH = "network_data/phisingData.csv"
    DATABASE = "NEWTWORKSECURITY"
    Collection = "NetworkData"
    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_converter(file_path=FILE_PATH)
    no_of_records = networkobj.insert_data_mongodb(records=records,database=DATABASE,collection=Collection)
    print(no_of_records)

