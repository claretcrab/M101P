import pymongo
import sys

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.exam7

albums = db.albums
images = db.images

images_removed = 0

cursor = images.find()

for image in cursor:
  count = albums.find({'images': image['_id']}).count()
  if count == 0:
    images.remove({'_id': image['_id']})
    images_removed += 1


print "#%s image(s) removed." ( images_removed )