dik_kenar_1=int(input("Alanını hesaplamak istediğiniz üçgenin bildiğiniz dik kenarı giriniz: "))
hipotenus=int(input("Alanını hesaplamak istediğiniz üçgene ait hipotenüsü giriniz: "))

dik_kenar_2= ((hipotenus**2)-(dik_kenar_1**2))**0.5

Alan= (dik_kenar_1*dik_kenar_2)/2

print("1.dik kenarı {}, Hipotenüsü {} olan bir dik üçgenin diğer dik kenarı {}'dır. Alanı ise {}'dır." .format(dik_kenar_1,hipotenus,dik_kenar_2,Alan))