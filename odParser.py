from bs4 import BeautifulSoup as Soup
import requests
from sys import argv
import argparse
from os import path

sesi = requests.Session()

def fixAlamat(alamatfix):
  
  return alamatfix.encode('utf-8').replace('http://', 'http:///').replace('//', '/')

# Fungsi sedang di perbaiki
def dengalAlt(tabel):
  pass
  try:
    halaman = Soup(sesi.get(lokasi).text.encode('utf-8'), 'html.parser')
    direktori = []
    for baris in halaman.findAll('tr'):
      if baris.find('img'):
        if baris.find('img').attrs['alt'] in ['[VID]', '[DIR]']:
          if baris.find('a').text != 'Parent Directory':
            alamat = fixAlamat('/'.join([lokasi, baris.find('a').attrs['href']]))
            if baris.find('img').attrs['alt'] != '[DIR]':
              print alamat
            else:
              if prindir:
                print alamat
              direktori.append(alamat)
    if sub:
      for url in direktori:
        daftarBerkas(url, sub)
  except Exception as e:
    print e  

def denganURI(tabel):
  abaikan = ['?C=D;O=A', '?C=S;O=A', '?C=M;O=A', '?C=N;O=D']
  hasil = {}

  for baris in tabel.findAll('tr'):
    berkas = baris.find('a')

    if berkas:

      if (berkas.attrs['href'] not in abaikan) and (berkas.text != 'Parent Directory'):
        file = False

        ukuran = baris.findAll('td')[3].text.strip()

        if ukuran != '-':
          file = True
        
        hasil[berkas.attrs['href']] = file
      
  return hasil

def daftarBerkas(lokasi, subdir = False, prindir = False):
  try:
    tabel = Soup(sesi.get(lokasi).text.encode('utf-8'), 'html.parser').find('table')
    berkas = denganURI(tabel)
    direktori = []
    
    for nama in berkas:
      alamat = fixAlamat('/'.join([lokasi, nama]))
      if not berkas[nama]:
        direktori.append(nama)
        if prindir:
          print alamat
      else:
        print alamat

    if subdir:
      for folder in direktori:
        alamat = fixAlamat('/'.join([lokasi, folder]))
        daftarBerkas(alamat, subdir, prindir)

  except Exception as e:
    print e

parser = argparse.ArgumentParser()
parser.add_argument('--subdir', '-s', help='boolean untuk sub-direktori', action='store_true', default=False, required=False)
parser.add_argument('--direktori', '-d', help='boolean untuk direktori', action='store_true', default=False, required=False)
parser.add_argument('filename', help='link to parser', nargs='*')


if __name__ == '__main__':
  aturan =  parser.parse_args();
  for alamat in aturan.filename:
    daftarBerkas(alamat, aturan.subdir, aturan.direktori)
    