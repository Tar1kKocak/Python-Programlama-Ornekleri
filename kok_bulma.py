print("Denklem : ax^2 + bx + c")

a = int(input("a degerini giriniz : "))
b = int(input("b degerini giriniz : "))
c = int(input("c degerini giriniz : "))

delta = b ** 2 -4 * a *c
kok1 = (-b - delta ** 0.5) / (2 * a)
kok2 = (-b + delta ** 0.5) / (2 * a)

print("Delta degeriniz : {}\nBirinci Kok : {}\nIkinci Kok : {}".format(delta,kok1,kok2))
