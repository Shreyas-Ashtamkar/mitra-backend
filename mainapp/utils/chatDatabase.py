from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from os import environ

client = None

def _refreshClient():
    global client
    client = MongoClient(
        environ.get("MONGODB_URI"), 
        server_api=ServerApi('1')
    )
    return client

def _testClient():
    try:
        if not client: _refreshClient()
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return True
    except Exception as e:
        print(e)

def getClient():
    if _testClient():
        return client
    else:
        raise Exception("Some error occured")

# class chatDatabase:
#     def __init__(self) -> None:

print(getClient())
