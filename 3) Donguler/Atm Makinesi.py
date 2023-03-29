print("*****Bankamiza Hosgeldiniz*****\n")
print("Yapmak istediginiz islemi belirtiniz...")
print("1-)Bakiye Sorgulama\n2-)Para Cekme\n3-)Para Yatirma\n4-)Cikis")
bakiye = 12500
while True:
   secenek = int(input("Giriniz : "))

   if(secenek==4):
       print("Sistemden Cikis Yapiliyor")
       break
   elif (secenek==1):
       print("Güncel Bakiye : ",bakiye)
   elif(secenek==2):
       cek = int(input("Cekilecek miktari giriniz : "))
       if(cek < bakiye):
           bakiye-=cek
       else:
           print("O kadar paraniz yok.")
   elif (secenek==3):
        yatir = int(input("Ne kadar yatiracaksiniz : "))
        bakiye+=yatir
   else:
       print("Gecersiz Islem")


