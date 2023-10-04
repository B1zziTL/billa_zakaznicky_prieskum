#zadeklarovanie premennych, zoznamov a slovnikov
pocet_odpovedi = 0
pocet_odpovedi_za_den = 0
posledny_zapis_hodin = 0
posledny_zapis_minut = 0
pocet_dni = 1
hodiny = []
pocty_hlasov = {}
hlasy_za_dni = {}

#otvorenie suborov
subor = open("spokojnost_1.txt","r")
subor1 = open("spokojnost_1.txt","r")

for riadok in subor: #cyklus na prechadzanie riadkov v subore
    #zmena pomocnych premennych
    pocet_odpovedi += 1
    pocet_odpovedi_za_den += 1

    #priradenie hodnoty ku dnom
    hlasy_za_dni[pocet_dni] = pocet_odpovedi_za_den

    if not riadok[0]+riadok[1] in hodiny: #podmienka na zapisanie hodiny
        hodiny.append(riadok[0]+riadok[1])

    #podmienky na zmenu premennych
    if posledny_zapis_hodin > int(str(riadok[0])+str(riadok[1])):  
        pocet_dni += 1
        pocet_odpovedi_za_den = 0
        
    elif posledny_zapis_hodin == int(str(riadok[0])+str(riadok[1])):
        if posledny_zapis_minut > int(str(riadok[3])+str(riadok[4])):
            pocet_dni += 1
            pocet_odpovedi_za_den = 0

    #ulozenie posledneho zapisu        
    posledny_zapis_hodin = int(str(riadok[0])+str(riadok[1]))
    posledny_zapis_minut = int(str(riadok[3])+str(riadok[4]))

#zoradenie zoznamu od najmensieho   
hodiny.sort()

for i in hodiny: #cyklus na naplnenie slovnika
    pocty_hlasov[i] = 0

for riadok in subor1: #cyklus na prechadzanie riadkov v subore
    for i in pocty_hlasov: #cyklus na zmenu hodnot v slovniku
        if riadok[0]+riadok[1] == i:
            pocty_hlasov[i] += 1

#vypisanie pozadovanych hodnot           
for i in hlasy_za_dni:
    print(str(i)+". deň - počet reakcií: "+str(hlasy_za_dni[i]))
print("Počet všetkých vyjadrení:",pocet_odpovedi)            
for i in pocty_hlasov:
    print("Hodina:",i,"Reakcií zákazníkov:",pocty_hlasov[i])
print("Počet dní:",pocet_dni)

#zatvorenie suborov
subor.close()
subor1.close()
