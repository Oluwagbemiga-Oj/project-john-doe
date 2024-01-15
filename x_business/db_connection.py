import pymongo

uri = 'mongodb+srv://x-mongo:XEvEAo1VIEC013qe@x-test.ibrmm04.mongodb.net/'
client = pymongo.MongoClient(uri)
project_x_db = client['project-x']