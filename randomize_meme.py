import sys
import pymongo


client = pymongo.MongoClient('mongodb://192.168.1.131:27017/')
db = client['test']
coll = db['images']

# db.images.aggregate([{$sample: {size: 1}}])
result = list(coll.aggregate([{"$sample": {"size": int(sys.argv[1])}}]))
urls = []
for r in result:
    if not r:
        continue
    urls.append(r['img_url'])

sys.stdout.write(' '.join(urls))
