#Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.
#Hipotenüs Formülü: a^2 + b^2 = c^2


kenar1 = int(input("Dik ucgeninizin dik olan iki kenarindan birincisini giriniz : "))
kenar2 = int(input("Dik ucgeninizin dik olan iki kenarindan ikincisini giriniz : "))

hipotenus = (kenar1**2 + kenar2**2) ** 0.5

print("Hipotenus Degeriniz : ",hipotenus)