#!/usr/bin/python

from sys import argv
# import argparse
from gsearch.googlesearch import search
# from homura import download
# import requests
# from os import path

# parser = argparse.ArgumentParser(description='Go Search tool for dorking')
# parser.add_argument('-m', '--maksimal', dest='maksimal', help='Jumlah maksimal hasil pencarian.', default=10)

# pilihan = vars(parser.parse_args())
# print pilihan['maksimal']

perintah = argv[1:]

banyak=0
# sesi = requests.Session()

if len(perintah) >= 2:
  banyak = perintah[0]
  perintah=perintah[1:]

  cari = '+'.join(perintah)

if banyak >= 1:
  print 'mencari %s sebanyak %s' % (cari, banyak)
  # hasil = open('hasil.txt', 'w+')
  
  try:
    temuan = search(cari, num_results=banyak)
    print 'ditemukan ', len(temuan)
    for url in temuan:
      # hasil.write("%s\n" % url[1])
      print str(url[1])
      # download(url=url[1], session=sesi, path='d:/download/flask/' + path.basename(url[1]) )

  except URLError as e:
    print e
  except Exception as e:
    print e

  # hasil.close()
