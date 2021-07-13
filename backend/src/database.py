from genericpath import exists
from warnings import catch_warnings
import sqlalchemy, json, os

con = None
try:    
    filepath = os.path.realpath(__file__)
    parent = os.path.dirname(filepath)
    filepath = os.path.join(parent, "connection_data.json")
    if(os.path.exists(filepath)):   
        file = open(filepath)
        j = json.load(file)
        dbConnectionString = j["connection"]
        if(not dbConnectionString == None):
            engine = sqlalchemy.create_engine(dbConnectionString)
            con = engine.connect()
except:
    print("ERROR CONNECTING TO DATABASE")
finally:
    file.close()