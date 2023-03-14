#Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.
#Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)
#BKİ 18.5'un altındaysa -------> Zayıf
#BKİ 18.5 ile 25 arasındaysa ------> Normal
#BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu
#BKİ 30'un üstündeyse -------------> Obez

boy = float(input("Boyunuzu metre cinsinden giriniz : "))
kilo = float(input("Kilonuzu kilogram cinsinden giriniz : "))

indeks =float (kilo / boy**2)

if (indeks<18.5):
    print("Zayif...")
elif (18.5<=indeks<25):
    print("Normal...")
elif (25<=indeks<30):
    print("Fazla Kilolu...")
elif (30<=indeks):
    print("Obez...")



