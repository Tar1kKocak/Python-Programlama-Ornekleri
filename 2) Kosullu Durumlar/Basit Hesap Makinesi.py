print("1-)Toplama\n2-)Cikarma\n3-)Carpma\n4-)Bolme\n5-)Karekok\n")
secenek = int(input("Hangi islemi secmek istiyorsunuz ?"))
sayi1 = int(input("Birinci Sayinizi Giriniz : "))
sayi2 = int(input("Ikinci Sayinizi Giriniz : "))

if (secenek == 1):
    print("Islem Sonucunuz : ", sayi1+sayi2)
elif (secenek == 2):
    print("Islem Sonucunuz : ", sayi1-sayi2)
elif (secenek == 3):
    print("Islem Sonucunuz : ", sayi1*sayi2)
elif (secenek == 4):
    print("Islem Sonucunuz : ", sayi1/sayi2)
elif (secenek == 5):
    print("Birinci sayinizin karekoku : {}\nIkinci sayinizin karekoku : {}".format(sayi1**0.5,sayi2**0.5))
else :
    print("Lutfen gecerli bir secenek giriniz.")