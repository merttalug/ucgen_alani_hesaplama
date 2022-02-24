birinci_kenar=int(input("Üçgenin Birinci Kenarını Giriniz: "))
ikinci_kenar=int(input("Üçgenin İkinci Kenarını Giriniz: "))
ucuncu_kenar=int(input("Üçgenin Üçüncü Kenarını Giriniz: "))

cevre= birinci_kenar + ikinci_kenar + ucuncu_kenar
u=cevre/2
Alan=(u*(u-birinci_kenar)*(u-ikinci_kenar)*(u-ucuncu_kenar))**0.5

print("Birinci kenarı {}, İkinci kenarı {}, Üçüncü kenarı {} olan üçgenin alanı {}'dir." .format(birinci_kenar,ikinci_kenar,ucuncu_kenar,Alan))