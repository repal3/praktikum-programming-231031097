print('praktikum-d3')
print()
nama         = 'Achmad Reza Pahlevi'
nim         = '231031097'
prodi        = 'Sistem Informasi D'
angkatan     = '2023'
meet         = 'Praktikum3'
email        = 'curvareza30@gmail.com'
sp           = 30

#print(len(nama))
print('-'.center(sp,'-'))

print(nama.center(sp))
print(nim.center(sp))
print('\n'*2)
print(meet.rjust(sp))
print(prodi.rjust(sp))
print(email.rjust(sp))
print('-'.center(sp,'-'))

#print(f'''halo, selamat datang perkenalkan nama saya {nama} dengan nim {nim} dari prodi {prodi}. Ini adalah file {meet}.''')

#paragraf = '''halo, selamat datang perkenalkan nama saya {} dengan nim {} dari prodi {}. Ini adalah file {}.'''

paragraf = '''\thalo, selamat datang perkenalkan nama saya {} dengan nim {} dari prodi {}. Ini adalah file {}.'''

p = paragraf.format(nama,nim,prodi,meet)
print(p)
print()

#-----5+++++9-----
# 1. input nilai x
x = int(input('Masukkan Nilai-----5+++++9-----= '))
# 2. cek1 apakah x > 5 true
cek1 = x > 5
# 3. cek2 apakah x < 9 true
cek2 = x < 9
# 4. status = cek1 and cek2
status = cek1 and cek2
# 5. cetak status
print('Hasilnya adalah',status)

#+++++5-----9+++++
# 1. input nilai x
x = int(input('Masukkan Nilai+++++5-----9+++++= '))
# 2. cek1 apakah x < 5 true
cek1 = x<5
# 3. cek2 apakah x > 9 false
cek2 = x>9
# 4.status = cek1 and cek2
status = cek1 or cek2
# 5. cetak status
print('Hasilnya adalah',status)

#-----5+++++9-----
x = int (input('masukan nilai='))
cek1 = x >= 5
cek2 = x <= 9
status = cek1 and cek2
print('hasilya adalah',status)

#+++++5----9+++++
x = int (input('masukan nilai='))
cek1 = x <= 5
cek2 = x >= 9
status = cek1 or cek2
print('hasilya adalah',status)

#+++++5-----9+++++13-----
x = int (input('masukan nilai'))
cek1 = x < 5
cek2 = x > 9
cek3 = x < 13
status = cek1 or cek2 and cek3
print('hasilya adalah',status)

#-----5+++++9------13+++++16
x = int (input('masukan nilai'))
cek1 = x > 5
cek2 = x < 9
cek3 = x > 13
cek4 = x < 16
status = cek1 or cek2  and cek3 or cek4
print('hasilya adalah',status)

print()

#Tugas 1
#-----5+++++9-----13+++++16-----
x = int (input('masukan nilai= -----5+++++9-----13+++++16----- ='))
cek1 = x > 5
cek2 = x < 9
cek3 = x > 13
cek4 = x < 16
status = cek1 or cek2  and cek3 or cek4
print('hasilya adalah',status)


#Tugas 2
#+++++5-----9+++++13-----16+++++
x = int(input('Masukkan nilai= +++++5-----9+++++13-----16+++++ ='))
cek1 = x < 5
cek2 = x > 9
cek3 = x < 13
cek4 = x > 16
status = cek1 or cek2 and cek3 or cek4
print('hasilnya adalah',status)


#Tugas 3
#-----5+++++9-----13+++++16-----20+++++24-----
x = int(input('Masukkan nilai -----5++++9-----13+++++16-----20+++++24----- = '))
cek1 = x > 5
cek2 = x < 9
cek3 = x > 13
cek4 = x < 16
cek5 = x > 20
cek6 = x < 24
status = cek1 and cek2 or cek3 and cek4 or cek5 and cek6
print('hasilnya adalah',status)


#Tugas 4
#+++++5-----9+++++13-----16+++++20-----24+++++
x = int(input('Masukkan nilai = ++++5-----9++++13-----16+++++20-----24+++++ ='))
cek1 = x < 5
cek2 = x > 9
cek3 = x < 13
cek4 = x > 16
cek5 = x < 20
cek6 = x > 24
status = cek1 or cek2 and cek3 or cek4 and cek5 or cek6
print('hasilnya adalah',status)












print('hello')


