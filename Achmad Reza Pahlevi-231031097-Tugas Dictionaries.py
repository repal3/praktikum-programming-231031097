#TUGAS DICTIONARIES

biodata = {'nama'   : 'Achmad Reza Pahlevi',
           'nim'    : '231031097',
           'email'  : 'curvareza30@gmail.com',
           'asal'   : 'Rantepao',
           'sks'    : '20',
           'gender' : 'Laki-laki',
           'alamat' : 'Jerman',
           'nomor'  : '102030'
           }

values = list(biodata.values())
biodata = values[:4]

print(biodata)