import requests
import os
import sys

def get_modeldata(name):
    classes = "http://129.21.127.60:8000/media/albums/" + name + "/data/scavenger_classes.ts"
    file1 = "http://129.21.127.60:8000/media/albums/" + name + "/data/saved_model_web/group1-shard1of1"
    file2 = "http://129.21.127.60:8000/media/albums/" + name + "/data/saved_model_web/tensorflowjs_model.pb"
    file3 = "http://129.21.127.60:8000/media/albums/" + name + "/data/saved_model_web/weights_manifest.json"

    r = requests.get(classes, allow_redirects=True)
    r1 = requests.get(file1, allow_redirects=True)
    r2 = requests.get(file2, allow_redirects=True)
    r3 = requests.get(file3, allow_redirects=True)
    open("/home/harrison/Desktop/museaivision/src/js/scavenger_classes.ts", "wb").write(r.content)
    open("/home/harrison/Desktop/museaivision/dist/model/group1-shard1of1", "wb").write(r1.content)
    open("/home/harrison/Desktop/museaivision/dist/model/tensorflowjs_model.pb", "wb").write(r2.content)
    open("/home/harrison/Desktop/museaivision/dist/model/weights_manifest.json", "wb").write(r3.content)



get_modeldata(sys.argv[1])
