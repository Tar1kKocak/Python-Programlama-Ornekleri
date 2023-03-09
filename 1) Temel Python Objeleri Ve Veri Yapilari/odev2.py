#Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.
#Beden Kitle İndeksi : Kilo / Boy(m)*Boy(m)

boy = float(input("Boyunuzu metre cinsinden giriniz:"))
kilo = int(input("Kilonuzu giriniz:"))

Indeks =(kilo / boy**2)
print("Beden Kitle Indeksiniz: ",Indeks)