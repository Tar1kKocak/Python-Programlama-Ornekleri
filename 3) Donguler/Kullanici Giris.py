print("*****Kayit Ekranina Hosgeldiniz*****")
nicknamekyt = input("Kullanici Adi Giriniz :")
passwrdkyt = input("Sifre Giriniz :")

print("*****Kayit Ekranindan Cikis Yapiliyor*****\n")
print("****Giris Ekranina Hosgeldiniz****")
girishak=3
while True:
    nicknamegiris = input("Kullanici Adinizi Giriniz : ")
    passwrdgiris = input("Sifrenizi Giriniz : ")

    if (nicknamekyt == nicknamegiris and passwrdkyt != passwrdgiris):
        print("Sifreniz Hatali")
        girishak-=1
    elif (nicknamekyt != nicknamegiris and passwrdkyt == passwrdgiris):
        print("Kullanici Ismi Hatali")
        girishak-=1
    elif (nicknamekyt != nicknamegiris and passwrdkyt != passwrdgiris):
        print("Kullanici Adi ve Sifre Hatali")
        girishak-=1
    else:
        print("Giris Yapildi...")
        break
    if (girishak==0):
        print("Giris Hakkiniz Kalmadi.")
        break


