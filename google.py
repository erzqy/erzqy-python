#!/usr/bin/python

from sys import argv
import argparse
from gsearch.googlesearch import search

parser = argparse.ArgumentParser()
parser.add_argument('--max', '-m', help="Jumlah maksimal pencarian.", action='store', default=10, required=False)
parser.add_argument('filename', help='Kata kunci pencarian.', nargs='*')

def main(katakunci, banyak=10):
  if len(katakunci) >= 5:
    print 'mencari %s sebanyak %s' % (katakunci, banyak)
    
    try:
      temuan = search(katakunci, num_results=banyak)
      print 'ditemukan ', len(temuan)
      for url in temuan:
        print str(url[1])

    except URLError as e:
      print e
    except Exception as e:
      print e
  else:
    print 'masukan kata kunci'

if __name__ == '__main__':
  aturan = parser.parse_args()
  main( '+'.join(aturan.filename), aturan.max)