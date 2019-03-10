import requests
import bs4
from gsearch.googlesearch import search
from sys import argv
import re

def gantiTAG(teks, kunci = r'<br\s?\/?[^<>]*>', ganti = "\n"):
	return re.sub(kunci, ganti, str(teks))

def hapusTAG(teks, kunci = r'<[^<>]*>'):
	return re.sub(kunci, '', str(teks))

def kapanLagi(judul, hapus = [' - KapanLagi.com', 'Lirik lagu ']):
	judul = hapusTAG(str(judul))
	for teks in hapus:
		judul = judul.replace(teks, '')
	return judul

sesi = requests.session()

lirik = ''

if len(argv) >= 2:
	lirik = ' '.join(argv)
else:
	lirik = ' jangan pisahkan'

lirik = 'lirik' + lirik + ' site:kapanlagi.com'

print lirik.replace(' ', '+')
pencarian = search(lirik.replace(' ', '+'), num_results=10)

for alamat in pencarian:
	print alamat[1]

for alamat in pencarian[:1]:

	print alamat[1]
	hasil = sesi.get(alamat[1]).text
	ranting = bs4.BeautifulSoup(hasil, "html.parser")
	hasil = ''

	print kapanLagi(ranting.title)
	for kata in ranting.findAll('div', {'class': 'lyrics-body'}):
		hasil = gantiTAG(hapusTAG(kata, r'<a.*/a>'))
		hasil = gantiTAG(hasil, r'</span>')
		hasil = hapusTAG(hasil)

	print hasil
