# Fungsi untuk mengenkripsi plainteks dengan kunci
def enkripsi(plainteks, kunci):
  plainteks = plainteks.upper().replace(" ", "")
  matriks = [["" for i in range((len(plainteks) + kunci - 1) // kunci)] for j in range(kunci)]
  indeks = 0
  for j in range(len(matriks[0])):
    for i in range(len(matriks)):
      if indeks < len(plainteks):
        matriks[i][j] = plainteks[indeks]
        indeks += 1
  cipherteks = ""
  for i in range(len(matriks)):
    for j in range(len(matriks[i])):
      cipherteks += matriks[i][j]
  return cipherteks

# Fungsi untuk mendekripsi cipherteks dengan kunci
# Fungsi untuk mendekripsi cipherteks dengan kunci
def dekripsi(cipherteks, kunci):
  cipherteks = cipherteks.upper().replace(" ", "")
  panjang_cipherteks = len(cipherteks)
  panjang_matriks = (panjang_cipherteks + kunci - 1) // kunci
  matriks = [["" for i in range(panjang_matriks)] for j in range(kunci)]
  indeks = 0
  for i in range(len(matriks)):
    for j in range(len(matriks[i])):
      if indeks < panjang_cipherteks:
        matriks[i][j] = cipherteks[indeks]
        indeks += 1
  plainteks = ""
  for j in range(len(matriks[0])):
    for i in range(len(matriks)):
      plainteks += matriks[i][j]
  return plainteks


# Meminta input dari pengguna untuk plainteks dan kunci
plainteks = input("Masukkan plainteks: ")
kunci = int(input("Masukkan kunci (harus lebih kecil dari panjang plainteks): "))

# Memanggil fungsi enkripsi dan dekripsi
cipherteks = enkripsi(plainteks, kunci)
print("Plainteks:", plainteks)
print("Cipherteks:", cipherteks)
print("Plainteks setelah dekripsi:", dekripsi(cipherteks, kunci))
