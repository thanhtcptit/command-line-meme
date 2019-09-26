import sys
import pymongo


client = pymongo.MongoClient('mongodb://192.168.1.131:27017/')
db = client['test']
coll = db['images']

# db.images.aggregate([{$sample: {size: 1}}])
result = coll.aggregate([{"$sample": {"size": 1}}])
sys.stdout.write(list(result)[0]['img_url'])
