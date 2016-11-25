import json,urllib, sys
data = urllib.urlopen(" http://saboga.co.id/api/v1/voucher/status/XQAHQ7G").read()
resp_dict = json.loads(data)
print ('status :')
print (resp_dict['status'])
print ('message :')
print (resp_dict['message'])
print ('error_code :')
print (resp_dict['error_code'])


