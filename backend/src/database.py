from genericpath import exists
from io import TextIOWrapper
from warnings import catch_warnings
import sqlalchemy, json, os

con = None
try:    
    filepath = os.path.realpath(__file__)
    parent = os.path.dirname(filepath)
    filepath = os.path.join(parent, "connection_data.json")
    file = None
    if(os.path.exists(filepath)):   
        file = open(filepath)
        j = json.load(file)
        dbConnectionString = j["connection"]
        if(not dbConnectionString == None):
            engine = sqlalchemy.create_engine(dbConnectionString)
            con = engine.connect()
except Exception as e:
    print("ERROR CONNECTING TO DATABASE")
    print(e)
finally:
    if(file != None):
        file.close()