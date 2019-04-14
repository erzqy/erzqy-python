from __future__ import unicode_literals

import requests
from sys import argv

ambil = requests.session()
for url in argv[1:]:
	print ambil.get(url).text.encode('utf-8')
