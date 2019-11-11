<<<<<<< HEAD
import re, os, urllib.request, bitly_api

with open ("url.py", "r") as myfile:
    data=myfile.readlines()

pat = 'public_url":"(?:\w|\/|:|\.)+'

dat = " ".join(data)

found = re.findall(pat, dat)


result = found[0][13:]

#apiurl = "http://tinyurl.com/api-create.php?url="
#tinyurl = urllib.request.urlopen(apiurl + result).read()
#dec = tinyurl.decode("utf-8")



API_USER = "deehrlic"
API_KEY = "R_1dc14729c75e474f8177814ef5b09b38"

b = bitly_api.Connection(API_USER, API_KEY)

longurl = result
response = b.shorten(uri = longurl)

dec = response['url']

def getDec():
    return dec
=======
import re, os, urllib.request, bitly_api

with open ("url.py", "r") as myfile:
    data=myfile.readlines()

pat = 'public_url":"(?:\w|\/|:|\.)+'

dat = " ".join(data)

found = re.findall(pat, dat)


result = found[0][13:]

#apiurl = "http://tinyurl.com/api-create.php?url="
#tinyurl = urllib.request.urlopen(apiurl + result).read()
#dec = tinyurl.decode("utf-8")



API_USER = "deehrlic"
API_KEY = "R_1dc14729c75e474f8177814ef5b09b38"

b = bitly_api.Connection(API_USER, API_KEY)

longurl = result
response = b.shorten(uri = longurl)

dec = response['url'][7:]

def getDec():
    return dec
>>>>>>> 39a58fff9e212021bd2f1436b60067aa3afa20e2
