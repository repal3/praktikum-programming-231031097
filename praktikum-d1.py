print('praktikum-d1')
print()
print('Nama Lengkap : Achmad Reza Pahlevi')
print('NIM          : 231031097')
print('Prodi        : Sistem Informasi')
print()
angkatan = 2023
print('Angkatan adalah', angkatan)
print()
a = 20
print('Data adalah =',a)
print('Tipenya adalah =',type(a))
print()
b = 20.0
print('Data adalah =',b)
print('Tipenya adalah =',type(b))
print()
c = 20j
print('Data adalah =',c)
print('Tipenya adalah =',type(c))
print()
kampus = 'Institut Teknologi BJ Habibie'
print('Data adalah +',kampus)
print('Tipenya adalah =',type(kampus))
print()
log = True
print('Data adalah +',log)
print('Tipenya adalah =',type(log))
print()
c = complex(5,8)
print('Data adalah =',c)
print('Tipenya adalah =',type(c))
print()
p = 20
q = 5
hasil=p+q
print('Hasil',p, '+',q, 'adalah', hasil)
print()
p = 20
q = 5
hasil=p+q
print('Hasil',p, '+',q, '=', hasil)
print()
p = 20
q = 5
hasil=p-q
print('Hasil',p, '-',q, '=', hasil)
print()
p = 20
q = 5
hasil=p*q
print('Hasil',p, 'x',q, '=', hasil)
print()
p = 20
q = 5
hasil=p/q
print('Hasil',p, ':',q, '=', hasil)
print()
p = 3
q = 2
Hasil=p**q
print('Hasil',p, '^',q, '=', Hasil)
print()
p = 37
q = 31
Hasil = p%q
print ('Hasil',p,'%',q,'=',Hasil)
print()
p = 37
q = 31
Hasil = p//q
print ('Hasil',p,'//',q,'=',Hasil)
print()
p = 20
q = 3
Hasil = p/q
print ('Hasil',p,':',q,'=',Hasil)
print()
a = 20
print('Nilai a adalah',a)
a = a + 1
print('Nilai a menjadi',a)
print()
a = 20
print('Nilai a adalah',a)
a += 1                                #perintah a = a + 1
print('Nilai a menjadi',a)
print()
a = 25
print('Nilai a adalah',a)
a -= 2                                #perintah a = a - 2
print('Nilai a menjadi',a)
print()
a = 20
print('Nilai a adalah',a)
a *= 2                                #perintah a = a * 2
print('Nilai a menjadi',a)
print()
a = 20
print('Nilai a adalah',a)
a /= 5                                #perintah a = a / 5
print('Nilai a menjadi',a)
print()
a = 20
print('Nilai a adalah',a)
a **= 2                               #perintah a = a ** 2
print('Nilai a menjadi',a)
print()
a = 20
print('Nilai a adalah',a)
a %= 7                                #perintah a = a % 7
print('Nilai a menjadi',a)
print()
a = 20
print('Nilai a adalah',a)
a //= 7                                #perintah a = a // 7
print('Nilai a menjadi',a)
print()
log = True
print('Nilai log adalah',log)
log |= False                           #perintah log=False log
print('Nilai log|= False menjadi',log)
print()
log = True
print('Nilai log adalah',log)
log &= False                           #perintah log=LOG & False
print('Nilai log&= False menjadi',log)
print()
log = True
print('Nilai log adalah',log)
log ^= False                           #perintah log=False ^ log
print('Nilai log ^= False menjadi',log)
print()
log = True
print('Nilai log adalah',log)
log ^= True                           #perintah log= log ^ True
print('Nilai log ^= False menjadi',log)
print()
bi = 0b0100
print('Nilai bi =',format(bi,'04b'))
bi>>=1                                #menggeser digit ke kanan  1 kali
print('Nilai bi >>=1 menjadi',format(bi,'04b'))
print()
bi = 0b0100
print('Nilai bi =',format(bi,'04b'))
bi<<=1                                #menggeser digit ke kiri  1 kali
print('Nilai bi <<=1 menjadi',format(bi,'04b'))
print()
a = 20
hasil = a>15
print('Hasil',a,'>15a adalah', hasil)
print()
a = 20
hasil = a==15
print('Hasil',a,'==15a adalah', hasil)
print()            #OPERATOR PERBANDINGAN
print()                                     #persamaan ==
x = 9
y = 6
hasil = x == y
print(x,'==',y,'=',hasil)
print()
x = 9
y = 9
hasil = x == y
print(x,'==',y,'=',hasil)
print()                                     #pertidaksamaan !=
x = 4
y = 4
hasil = x != y
print(x,'!=',y,'=',hasil)
print()
x = 4
y = 8
hasil = x != y
print(x,'!=',y,'=',hasil)
print()                                     #lebih besar >
y = 20
z = 50
hasil = y > z
print(y,'>',z,'=',hasil)                                  
y = 50
z = 20
hasil = y > z
print(y,'>',z,'=',hasil)
print()                                     #lebih kecil <
a = 100
b = 90
hasil = a < b
print(a,'<',b,'=',hasil)
a = 90
b = 100
hasil = a < b
print(a,'<',b,'=',hasil)
print()                                     #lebih besar sama >=
x = 30
y = 35
hasil = x >= y
print(x,'>=',y,'=',hasil)
x = 35
y = 30
hasil = x >= y
print(x,'>=',y,'=',hasil)
print()                                     #lebih besar sama <=
a = 60
z = 20
hasil = a <= z
print (a,'<=',z,'=',hasil)
a = 20
z = 60
hasil = a <= z
print(a,'<=',z,'=',hasil)
print()
A = 'Aku'
print('Aku' is A)
A ='Aku'
print('aku' is A)