#Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.

a = (input("Birinci sayiyi giriniz : "))
b = (input("Ikinci sayiyi giriniz : "))

a,b = b,a

print("Yeni Degerler = a : {}, b : {}".format(a,b))