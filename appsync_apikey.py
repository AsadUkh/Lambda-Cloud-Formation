import boto3
from datetime import datetime , timedelta
import json


client = boto3.client('appsync')

response = client.list_api_keys(
    apiId='rwromyhnzrdezogkyi5gyayqy4',
   # nextToken='da2-p2skjlyw7rbo3gdmtzenzpnuwm',
    maxResults=12
)

print ("Below are the keys/key for api id")
for key in response['apiKeys']:  
    print(key)


future_expiration_date = datetime.now() + timedelta(days = 365)
print("Future Expiration date ",future_expiration_date)
future_expiration_date_epoc=future_expiration_date.timestamp()
print ("Afterting conversion it in epoch formatc ", future_expiration_date.timestamp())

for key in response['apiKeys']:  
    print ("iterating over number of keys")
    print ("Current value of expiration in Epoch format" ,key['expires'])
    print ("Current value of expiration in TimeStamp GMT format" ,datetime.fromtimestamp(key['expires']))
    dt_object = datetime.fromtimestamp(key['expires'])
    diff = dt_object -datetime.now()
    print ("Key will be Expired in ", diff ," day , if it is less than the specified value then i will update")
    if(diff.days < 5):
        print("update kar raha hoon bhai hosla")
        response = client.update_api_key(
        apiId='rwromyhnzrdezogkyi5gyayqy4',
        id=key['id'],
        description='my-updated-description',
        expires=int(future_expiration_date_epoc)
)

    


# dt_object = datetime.fromtimestamp(1638115200)

# print (datetime.now())
# print (dt_object)
# print  

# diff= (dt_object -datetime.now())


