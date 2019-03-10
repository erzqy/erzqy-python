import requests
import bs4
from gsearch.googlesearch import search
from sys import argv
import re

def gantiNL(teks, kunci = r'<br\/?[^<>]*>'):
	return re.sub(kunci, r'\n', str(teks))

def hapusTAG(teks, kunci = r'<[^<>]*>'):
	return re.sub(kunci, '', str(teks))

def wowKeren(judul, hapus = [' :: Cari Lirik Lagu di WowKeren.com ?', 'Lirik lagu: ']):
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

lirik = 'lirik' + lirik + ' site:wowkeren.com'

print lirik.replace(' ', '+')
pencarian = search(lirik.replace(' ', '+'), num_results=10)

for alamat in pencarian:
	print alamat[1]

for alamat in pencarian[:1]:

	print alamat[1]
	hasil = sesi.get(alamat[1]).text
	ranting = bs4.BeautifulSoup(hasil, "html.parser")
	hasil = ''

	print wowKeren(ranting.title)
	for kata in ranting.findAll('div', {'class': 'news-details-layout1'}):
		hasil = hapusTAG(kata)

	print hasil
