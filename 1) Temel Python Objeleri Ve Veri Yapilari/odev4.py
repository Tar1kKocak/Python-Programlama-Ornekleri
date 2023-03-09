#Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.

ad = input("Isminizi Giriniz : ")
soyad = input("Soyisminizi Giriniz : ")
Numara = int(input("Telefon Numaranizi Giriniz : "))

bilgiler = [ad,soyad,Numara]

print("Isım : {}\nSoyisim : {}\nTelefon Numarasi : {}".format(bilgiler[0],bilgiler[1],bilgiler[2]))

