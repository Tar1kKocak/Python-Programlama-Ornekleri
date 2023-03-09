#Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın
# ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.

kmyakar = float(input("Araciniz 100 km de kac litre benzin yakmaktadir:"))
yol = float(input("Yolunuz kac km:"))

benzinucret = 20.50
Masraf = (yol/100) * (benzinucret*benzinucret)

print("Toplam odemeniz gereken ucret:",Masraf)