'''
JSON"

    it is mainly used for storing and transfering data between the browser and server



    API: Application Programming Interface : API creates communication between app and server

    inside API we have data in JSON format

'''



import json
d={'name':'randhir',
   "contact":8787878787}

f=json.dumps(d)
print(f)
print(type(f))

f1=json.loads(f)


for i in f1:
    print(i,f1[i])

