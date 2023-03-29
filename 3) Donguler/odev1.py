#Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.
#Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir.

sayi = int(input("Sayiyi Giriniz : "))

i = 1
toplam = 0

while (i<sayi):
        if(sayi % i == 0):
            toplam+=i
        i += 1


if(toplam==sayi):
    print("Sayi Mukemmel")
else:
    print("Sayi Mukemmel Degil")