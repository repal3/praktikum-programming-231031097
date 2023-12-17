print('Prktikum-2')
print()
print('Nama Lengkap : Achmad Reza Pahlevi')
print('NIM          : 231031097')
print('Prodi        : Sistem Informasi')
print()
print('==================Ini And==================')
a = True
b = False
hasil = a and a
print('Nilai',a,'and',a,'adalah',hasil)
print()
hasil = a and b
print('Nilai',a,'and',b,'adalah',hasil)
print()
hasil = b and a
print('Nilai',b,'and',a,'adalah',hasil)
print()
hasil = b and b
print('Nilai',b,'and',b,'adalah',hasil)
print()
print('==================Ini Or==================')
hasil = a or a
print('Nilai',a,'and',a,'adalah',hasil)
print()
hasil = a or b
print('Nilai',a,'or',b,'adalah',hasil)
print()
hasil = b or a
print('Nilai',b,'or',a,'adalah',hasil)
print()
hasil = b or b
print('Nilai',b,'or',b,'adalah',hasil)
print()
print('==================Ini Not==================')
hasil = not a
print('hasil not',a,'adalah',hasil)
print()
hasil = not b
print('hasil not',b,'adalah',hasil)
print()
print('==================Ini xor================')
hasil = a ^ a
print('Nilai',a,'xor',a,'adalah',hasil)
print()
hasil = a ^  b
print('Nilai',a,'xor',b,hasil)
print()
hasil = b ^ a
print('Nilai',b,'xor',a,hasil)
print()
hasil = b ^ b
print('Nilai',b,'xor',b,hasil)
print()
print('==================Ini nand================')
hasil = not (a and a)
print('Nilai',a,'nand',a,'adalah',hasil)
print()
hasil = not (a and b)
print('Nilai',a,'nand',b,hasil)
print()
hasil = not (b and a)
print('Nilai',b,'nand',a,hasil)
print()
hasil = not (b and b)
print('Nilai',b,'nand',b,hasil,)
print()
print('==================Ini nor================')
hasil = not (a or a)
print('Nilai',a,'nor',a,'adalah',hasil)
print()
hasil = not (a or b)
print('Nilai',a,'nor',b,hasil)
print()
hasil = not (b or a)
print('Nilai',b,'nor',a,hasil)
print()
hasil = not (b or b)
print('Nilai',b,'nor',b,hasil)
print()
print('==================Ini in Nnot================')
hasil = not (not a)
print('Nilai',a,'nnot','adalah',hasil)
print()
hasil = not (not b)
print('Nilai',b,'nnot',hasil)
print()
print('==================Ini NXOR================')
hasil = not (a ^ a)
print('Nilai',a,'NXOR',a,'adalah',hasil)
print()
hasil = not (a ^ b)
print('Nilai',a,'NXOR',b,hasil)
print()
hasil = not (b ^ a)
print('Nilai',b,'NXOR',a,hasil)
print()
hasil = not (b ^ b)
print('Nilai',b,'NXOR',b,hasil,)
print()
print('t/OPERATOR IDENTITAS')
print()
print('================== Is')
a = 5
b = 6
print('Nilai',a,'memiliki identitas',hex(id(a)))
print('Nilai',a,'memiliki identitas',hex(id(b)))
hasil = a is b
print('a is b =',hasil)
print()
a = 6
b = 6
print('Nilai',a,'memiliki identitas',hex(id(a)))
print('Nilai',a,'memiliki identitas',hex(id(b)))
hasil = a is b
print('a is b =',hasil)
print()
print('================== Is not')
a = 5
b = 6
print('Nilai',a,'memiliki identitas',hex(id(a)))
print('Nilai',a,'memiliki identitas',hex(id(b)))
hasil = a is not b
print('a is not b =',hasil)
print()
a = 6
b = 6
print('Nilai',a,'memiliki identitas',hex(id(a)))
print('Nilai',a,'memiliki identitas',hex(id(b)))
hasil = a is not b
print('a is not b =',hasil)
print()
print("t/OPERATOR MEMBERSHIP")
print()
print('================== In')
nama = 'Bacharuddin Jusuf Habibie'
test = 'rud'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))
print()
test = 'bach'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))
print()
test = 'ib'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))
print()
test = 'a'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))
print()
test = 'i'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))
print()
test = 'u'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))
print()
test = 'e'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))
print()
test = 'o'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))
print()
print('\n=============== in')
data = ['Institut',
        'Teknologi',
        'Bacharuddin',
        'Jusuf',
        'Habibie']
print('Data adalah',data)
test1 = 'Habibie'
test2 = 'Parepare'
test3 = 'Kampus'
test4 = 'Institut'

cek = test1 in data
print(test1,'terdapat di data adalah '+str(cek))
cek = test2 in data
print(test2,'terdapat di data adalah '+str(cek))
cek = test3 in data
print(test3,'terdapat di data adalah '+str(cek))
cek = test4 in data
print(test4,'terdapat di data adalah '+str(cek))
print()
#ini operator bitwise
a = 30 #isi dengan tanggal lahir
b = 12 #isi dengan bulan lahir
b +=80
print('\n============= AND')
print('Nilai',a,'dalam binner         = ',format(a,'08b'))
print('Nilai',b,'dalam binner         = ',format(b,'08b'))
print('-------------------------------------------AND')
c = a & b
print('Nilai',a,'&',b,'dalam biner adalah',format(c,'08b'))
print()
print('\n============= OR')
print('Nilai',a,'dalam binner         = ',format(a,'08b'))
print('Nilai',b,'dalam binner         = ',format(b,'08b'))
print('-------------------------------------------or')
c = a | b
print('Nilai',a,'&',b,'dalam biner adalah',format(c,'08b'))

print() #TUGAS BUAT NAMA MENJADI NAMA LENGKAP MASING MASING
print('================== Not In')

nama = 'Achmad Reza Pahlevi'
test = 'Mad'
cek = test not in nama
print(test,'tidak terdapat di',nama,'adalah '+str(cek))
print()
test = 'Rez'
cek = test not in nama
print(test,'tidak terdapat di',nama,'adalah '+str(cek))
print()
test = 'Eza'
cek = test not in nama
print(test,'tidak terdapat di',nama,'adalah '+str(cek))
print()
test = 'a'
cek = test not in nama
print(test,'tidak terdapat di',nama,'adalah '+str(cek))
print()
test = 'i'
cek = test not in nama
print(test,'tidak terdapat di',nama,'adalah '+str(cek))
print()
test = 'u'
cek = test not in nama
print(test,'tidak terdapat di',nama,'adalah '+str(cek))
print()
test = 'e'
cek = test not in nama
print(test,'tidak terdapat di',nama,'adalah '+str(cek))
print()
test = 'o'
cek = test not in nama
print(test,'tidak terdapat di',nama,'adalah '+str(cek))

print()

#tugas dengan cara yang sama buat operator untuk not in
print('=========================NOT IN')
data=['Calon',
      'Pegawai',
      'Negeri',
      'Sipil',
      'Indonesia']
print()
print('Data adalah',data)
test1='Calon'
test2='Negara'
test3='Swasta'
test4='Indonesia'
print()
cek=test1 not in data
print(test1,'Tidak terdapat di data adalah',cek)
cek=test2 not in data
print(test2,'Tidak terdapat di data adalah',cek)
cek=test3 not in data
print(test3,'Tidak terdapat di data adalah',cek)
cek=test4 not in data
print(test4,'Tidak terdapat di data adalah',cek)
print()
#Tugas untuk operator xor, c = a ^ b
print('=========================XOR')
print('Nilai',a,'Dalam biner           =',format(a,'08b'))
print('Nilai',b,'Dalam biner           =',format(b,'08b'))
print('-----------------------------------------------------XOR')
c= a ^ b
print('Nilai',a,'&',b,'Dalam Biner Adalah',format(c,'08b'))
print()
#Tugas untuk operator not, c = ^a
print('=========================NOT a')
print('Nilai',a,'Dalam biner         =',format(a,'08b'))
print('-----------------------------------------------------NOT a')
c= ~a
print('Nilai','~','\b',a,'Dalam Biner Adalah',format(c,'08b'))
print()
#Tugas untuk operator not, c = ^b
print('=========================NOT a')
print('Nilai',b,'Dalam biner         =',format(b,'08b'))
print('-----------------------------------------------------NOT a')
c= ~b
print('Nilai','~','\b',b,'Dalam Biner Adalah',format(c,'08b'))
print()
#Tugas untuk operator geser kanan, c = a >> b
print('=========================>>')
print('Nilai',a,'Dalam biner         =',format(a,'08b'))
print('----------------------------------------------------->>')
c= a>>2
print('Nilai',a,'>>','Dalam Biner Adalah',format(c,'08b'))
print()
#Tugas untuk operator geser kiri, c = a << b
print('=========================<<')
print('Nilai',a,'Dalam biner         =',format(a,'08b'))
print('-----------------------------------------------------<<')
c= a<<2
print('Nilai',a,'>>','Dalam Biner Adalah',format(c,'08b'))
print()
#Tugas untuk operator not and, c = ~ (a & b)
print('=========================not and')
print('Nilai',a,'Dalam biner                 =',format(a,'08b'))
print('Nilai',b,'Dalam biner                 =',format(b,'08b'))
print('-----------------------------------------------------not and')
c=~(a&b)
print('Nilai','~(',a,'&',b,')','Dalam Biner Adalah',format(c,'08b'))
print()
#Tugas untuk operator not or, c = ~ (a | b)
print('=========================not OR')
print('Nilai',a,'Dalam biner                 =',format(a,'08b'))
print('Nilai',b,'Dalam biner                 =',format(b,'08b'))
print('-----------------------------------------------------OR')
c= ~(a|b)
print('Nilai','~(',a,'|',b,')','Dalam Biner Adalah',format(c,'08b'))
print()
#Tugas untuk operator not xor, c = ~ (a ^ b)
print('=========================not XOR')
print('Nilai',a,'Dalam biner                =',format(a,'08b'))
print('Nilai',b,'Dalam biner                =',format(b,'08b'))
print('-----------------------------------------------------not XOR')
c= ~(a ^ b)
print('Nilai ~(',a,'^',b,')Dalam Biner Adalah',format(c,'08b'))
print()
#Tugas untuk operator not geser kanan, c = ~ (a >> b)
print('=========================not geser kanan')
print('Nilai',a,'Dalam biner                =',format(a,'08b'))
print('-----------------------------------------------------not geser kanan')
c= ~(a >> 2)
print('Nilai ~(',a,'>> 2)','Dalam Biner Adalah',format(c,'08b'))
print()
#Tugas untuk operator not geser kiri, c = ~ (a << b)
print('=========================not geser kiri')
print('Nilai',a,'Dalam biner                =',format(a,'08b'))
print('-----------------------------------------------------not geser kiri')
c= ~(a << 2)
print('Nilai ~(',a,'<< 2)','Dalam Biner Adalah',format(c,'08b'))
print()


