import re, os, urllib.request

with open ("url.py", "r") as myfile:
    data=myfile.readlines()

pat = 'public_url":"(?:\w|\/|:|\.)+'

dat = " ".join(data)

found = re.findall(pat, dat)


result = found[0][13:]


apiurl = "http://tinyurl.com/api-create.php?url="
tinyurl = urllib.request.urlopen(apiurl + result).read()
dec = tinyurl.decode("utf-8")

return dec
