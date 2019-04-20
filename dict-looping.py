
def buatDaftar(isi, posisi = None):
  hasil = []
  if posisi != None:
    if posisi < len(isi):
      for kata in isi:
        hasil.append((isi[posisi], kata))
      hasil += buatDaftar(isi, posisi+1)
  else:
    hasil += buatDaftar(isi, 0)
  return hasil

print buatDaftar([1, 2, 3])