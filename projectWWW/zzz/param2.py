import json,urllib, sys
data = urllib.urlopen("https://query.yahooapis.com/v1/public/yql?q=select%20item.condition%20from%20weather.forecast%20where%20woeid%20%3D%202487889&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys").read()
resp_dict = json.loads(data)
print ('status :')
print (resp_dict['created'])
print ('message :')
#print (resp_dict['date'])
print ('error_code :')
#print (resp_dict['temp'])


