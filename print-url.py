import requests
from sys import argv

hasil = requests.session()
for url in argv[1:]:
	print hasil.get(url).text 