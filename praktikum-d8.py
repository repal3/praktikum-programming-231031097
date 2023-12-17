import os
os.system('cls')

Pass1 ='INI PASSWORD'
Pass2 ='PASSWORD INI'
Pass3 ='PASSWORD'
percobaan_1 = 0
limit = 3
a = True

while a :
    percobaan_1 += 1
    print('')
    print('Login Dengan Password') 
    pw_1 = (input('Masukkan Password Pertama : '))
    if pw_1 == Pass1 :
        print('Password Benar, Ikuti Langkah Selanjutnya')
        percobaan_1 *= 0
        while a :
            percobaan_1 += 1
            print('Masukkan Password Untuk Ke Halaman Kedua')
            pw_1 = (input('Masukkan Password Kedua : '))
            if pw_1 == Pass2 :
                print('Password Benar, Ikuti Langkah Selanjutnya') 
                percobaan_1 *= 0
                while a :
                    percobaan_1 += 1
                    print('Masukkan Password untuk ke halaman Ketiga')
                    pw_1 = (input('Masukkan Password Ketiga : '))
                    if pw_1 == Pass3 :
                        print('Selamat Datang, Anda Berhasil Login') 
                        a = False
                        percobaan_1 *= 0
                    else  :
                        print('Password salah')
                        if percobaan_1 == limit :
                            print('Anda Gagal, Coba Ulang')
                            a = False
                        else :
                            print('Kesempatan Anda Tersisa',limit-percobaan_1) 
            else  :
                print('Password salah')
                if percobaan_1 == limit :
                    print('Anda Gagal, Coba Ulang')
                    a = False
                else :
                    print('Kesempatan Anda Tersisa',limit-percobaan_1)
    else  :
        print('Password salah')
        if percobaan_1 == limit :
            print('Anda Telah Mencoba 3x, Coba Lagi Beberapa Saat')
            a = False
        else :
            print('Kesempatan Anda Tersisa',limit-percobaan_1)