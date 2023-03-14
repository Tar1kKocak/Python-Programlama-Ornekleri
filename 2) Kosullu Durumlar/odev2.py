#Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.

sayi1 = input("Birinci Sayi :")
sayi2 = input("Ikinci Sayi : ")
sayi3 = input("Ucuncu Sayi : ")
a = int

if(sayi1>=sayi2 and sayi1>=sayi3):
    print("En Buyuk Sayi : ",sayi1)
if(sayi2>=sayi1 and sayi2>=sayi3):
    print("En Buyuk Sayi : ",sayi2)
if(sayi3>=sayi1 and sayi3>=sayi2):
    print("En Buyuk Sayi : ",sayi3)
