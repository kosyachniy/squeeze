import sys
if sys.version_info[0]>=3:
	from urllib.request import urlretrieve
else:
	from urllib import urlretrieve

def download:
	urlretrieve('http://zodzu.com/input.txt','input.txt')
	urlretrieve('http://zodzu.com/output.txt','output.txt')