#Tugas 1 : Buat flowchart
#1. Flowchart Bilangan ganjil
#a. Input bilangan X
#b. Cek : jika ganjil maka cetak (“Bilangan X adalah Ganjil ”)
#c. Jika tidak Maka cetak (“Bilangan X adalah Bukan Ganjil”)2
#d. Selesai 

angka = int(input("Masukan Nilai : "))
if (angka % 2 ) == 0:
    print(angka," Bukan Bilangan Ganjil")
else:             
    print(angka," Adalah Bilangan Ganjil")
