print("Kayit Ekranina Hosgeldiniz...")
kullaniciAdiKayit = input("Kullanici Ad : ")
SifreKayit = input("Sifre : ")
print("Kayit Tamamlandi...")

print("Giris Ekranina Hosgeldiniz...")
kullaniciAdiGiris = input(print("Kullanici Ad : "))
SifreGiris = input(print("Sifre : "))

if(kullaniciAdiGiris == kullaniciAdiKayit and SifreGiris == SifreKayit):
    print("Giris Basariyla Gerceklesti.")
elif(kullaniciAdiGiris == kullaniciAdiKayit and SifreGiris !=SifreKayit):
    print("Sifre Hatali.")
elif(kullaniciAdiGiris != kullaniciAdiKayit):
    print("Kullanici Adi Hatali.")
    

