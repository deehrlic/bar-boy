import re

with open ("url.py", "r") as myfile:
    data=myfile.readlines()

pat = 'public_url":"(?:\w|\/|:|\.)+'

dat = " ".join(data)

found = re.findall(pat, dat)

result = found[0][13:]

print(result)
