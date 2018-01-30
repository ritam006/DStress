import json
import requests

text={'text':'great'}
r=requests.post("http://text-processing.com/api/sentiment/",data=text)

print (r.status_code)
print (r.content)
# if(r.status_code==400)

data=r.json()
if(data['probability']['neg']>data['probability']['pos']):
    response={'negative':'yes'}
else:
    response = {'negative': 'no'}
