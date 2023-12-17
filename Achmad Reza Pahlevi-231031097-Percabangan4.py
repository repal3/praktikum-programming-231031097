#TUGAS PERCABANGAN 4

pendapatan = int(input("Pendapatan: "))

if pendapatan <= 1000:
    persentase = 0
elif pendapatan <= 2000:
    persentase = 7.9
elif pendapatan <= 3000:
    persentase = 14.9
elif pendapatan <= 4000:
    persentase = 21.9
elif pendapatan <= 5000:
    persentase = 28.9
else:
    persentase = 34.9

bonus = pendapatan * (persentase / 100)
total = pendapatan + bonus

print('Pendapatan:', pendapatan)
print('Persentase:', persentase, '%')
print('Bonus:', bonus)
print('Jumlah Total:', total)