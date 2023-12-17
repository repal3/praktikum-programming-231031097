import os
os.system('cls')

a = True

while a:
    jawab = input('Apakah Ingin Lanjutkan ? (y/n)')
    if jawab == 'y':
        print('Terima Kasih')
        a= True
    elif jawab == 'n':
        os.system('cls')
        print('Sampai Jumpa :p')
        a = False
    else:
        print('Jangan Aneh')
        a = True
