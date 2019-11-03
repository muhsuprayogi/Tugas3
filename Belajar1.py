Bilangan1 = int(input("Masukan Bilangan 1:"))
Bilangan2 = int(input("Masukan Bilangan 2:"))
Bilangan3 = int(input("Masukan Bilangan 3:"))

if int(Bilangan1) and Bilangan2 > Bilangan3:
     print("Nilai terbesarnya adalah :", Bilangan1)
     Terbesar = Bil1
     IniBil = "Bilangan 1"
elif (Bilangan2 > Bilangan3) and (Bilangan2 > Bilangan1):
     print("Nilai terbesarnya adalah :", Bilangan2)
     Terbesar = Bil2
     IniBil = "Bilangan 2"
else:
     Terbesar = Bilangan3
     IniBil1 = "Bilangan 3"

print("Bilangan yang terbesar adalah", Bilangan1, "dengan nilai", Terbesar)

