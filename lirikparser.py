from bs4 import BeautifulSoup as soup
import re
import requests

TAG_BR=r'<br\s?/?[^<>]>'
TAG_ALL=r'<[^<>]*>'

def gantiTAG(tekshtml = '', caritag = TAG_ALL, gantinya = ''):
	return re.sub(caritag, gantinya, str(tekshtml))

def gantiTeks(tekshtml = '', cariteks = None, gantinya = ''):
	if cariteks:
		tekshtml = gantiTAG(tekshtml, TAG_ALL, '')
		for teks in cariteks:
			tekshtml = tekshtml.replace(teks, gantinya)

		return tekshtml
	else:
		return tekshtml

def hapusSpasiBerlebih(tekshtml):
	while "  " in tekshtml:
		tekshtml = tekshtml.replace("  ", " ")
	return tekshtml

def parsingWowKeren(tekshtml):
	hasil = {'judul':'', 'lirik':''}
	if len(tekshtml) <= 0:
		return tekshtml
	else:
		halaman = soup(tekshtml, 'html.parser')
		hasil['judul'] = gantiTeks(gantiTAG(halaman.title), [' :: Cari Lirik Lagu di WowKeren.com ?', 'Lirik lagu: '])
		for teks in halaman.findAll('div', {'class': 'news-details-layout1'}):
			hasil['lirik'] += gantiTAG(teks)
	return hasil

def parsingKapanLagi(tekshtml):
	hasil = {'judul':'', 'lirik':''}
	if len(tekshtml) <= 0:
		return tekshtml
	else:
		halaman = soup(tekshtml, 'html.parser')
		hasil['judul'] = gantiTeks(gantiTAG(halaman.title), [' - KapanLagi.com', 'Lirik lagu '])
		for teks in halaman.findAll('div', {'class': 'lyrics-body'}):
			hasil['lirik'] += gantiTAG(teks)
	return hasil

def parsingInstaLirik(tekshtml):
	hasil = {'judul':'', 'lirik':''}
	if len(tekshtml) <= 0:
		return tekshtml
	else:
		halaman = soup(tekshtml, 'html.parser')
		hasil['judul'] = gantiTeks(gantiTAG(halaman.title), ['Lirik Lagu ', " \xe2\x80\xa2 Instalirik"])
		hasil['lirik'] = halaman.body
			# hasil['lirik'] += gantiTAG(teks)
	return hasil

def parsingLirikBagus(tekshtml):
	hasil = {'judul':'', 'lirik':''}
	if len(tekshtml) <= 0:
		return tekshtml
	else:
		halaman = soup(tekshtml, 'html.parser')
		hasil['judul'] = gantiTeks(gantiTAG(halaman.title), ['Lirik Lagu '])

		for intro in halaman.findAll('p', {'style': "font-style: italic;font-size: 13px;"}):
			intro.decompose()

		for intro in halaman.findAll('h1'):
			intro.decompose()

		for intro in halaman.findAll('h2'):
			intro.decompose()

		for teks in halaman.findAll('div', {'id': 'lyric-content'}):
			hasil['lirik'] += gantiTAG(teks)
		
		return hasil

PARSER = {'wowkeren.com': parsingWowKeren, 'kapanlagi.com': parsingKapanLagi, 'instalirik.com': parsingInstaLirik, 'lirikbagus.id': parsingLirikBagus}

def parsingUmum(alamat):
	pengenalurl = re.compile(r'([a-z0-9\-]+\.\w{2,3})/', re.I)
	domain = ''.join(pengenalurl.match(alamat).group())
	print alamat, domain

	if (len(domain) >= 5) and (PARSER.has_key(domain)):
		browser = requests.session()
		return PARSER[domain](hapusSpasiBerlebih(browser.get(alamat).text.encode('utf-8').replace("\n", '')))
	else:
		return None

if __name__ == '__main__':
	alamatnya = ['https://lirik.kapanlagi.com/artis/inka-christie/yang-terindah/', 'https://www.wowkeren.com/lirik/lagu/inka_christie/yang-terindah.html', 'https://www.instaldirik.com/yang-terindah-inka-christie/', 'https://lirikbagus.id/lagu/inka-christie-yang-terindah', 'https://liriklaguindonesia.net/tommy-j-pisa-nasib-pengamen.htm', 'http://lirikraja.blogspot.com/2016/10/doel-sumbang-bulan-kemah-feat-nini.html']
	for alamat in alamatnya:
		print parsingUmum(alamat)

