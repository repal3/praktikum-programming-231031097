import os
os.system('cls')

pwd_benar = 'BacoTampanGagahBerani123'
a = True
limit = 3
i = 0
while a:
    i+= 1
    pwd = input('Masukan Password : ')
    if pwd == pwd_benar:
        print('Selamat, Anda Berhasil Login')
        a = False
    else:
        print('Password Anda Salah')
        print(f'Kesempatan Anda Tersisa {limit-i}')
        if i == limit:
            print('Anda Terblokir')
            a = False
        else:
            print(f'Kesempatan Anda {limit-i}')


