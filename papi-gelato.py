def soort_bolletje(aantal_bolletjes):
    bolletje_volgorde = 1
    for i in range(1,aantal_bolletjes+1):
        soort = input('Welke smaak wilt u voor bolletje nummer' + str(bolletje_volgorde) + '? A) Aardbei, C) Chocolade of V) Vanille?')
        if soort == "V" or "M" or "C" or "A":
            bolletje_volgorde += 1
        else:
            print('Sorry dat is geen optie die we aanbieden..')
            soort_bolletje()

def aantal_bolletjes():
    aantal_bolletjes = int(input('Hoeveel bolletjes wilt u?'))
    if aantal_bolletjes >= 1 and aantal_bolletjes <= 3:
        soort_bolletje(aantal_bolletjes)
        bakje_hoorntje(aantal_bolletjes)
        
    elif aantal_bolletjes >= 4 and aantal_bolletjes <= 8:
        print('Dan krijgt u van mij een bakje met ' + str(aantal_bolletjes) + ' bolletjes')
        soort_bolletje(aantal_bolletjes)
    elif aantal_bolletjes > 8:
        print('Sorry, zulke grote bakken hebben we niet')
    else:
        print('Sorry dat is geen optie die we aanbieden..')
def bakje_hoorntje(aantal_bolletjes):
    bakje_hoorntje = input('Wilt u deze ' + str(aantal_bolletjes) + ' bolletje(s) in A) een hoorntje of B) een bakje?')
    if bakje_hoorntje == "A":
        
        totaal = ...(aantal_bolletjes, 1, 0, 0)
        hoorntje = input('Hier is uw hoorntje met ' + str(aantal_bolletjes) + ' bolletje(s). Wilt u nog meer bestellen? (Y/N)')
        if hoorntje == 'Y':
            aantal_bolletjes()
            
        elif hoorntje == 'N':
            
            print('Bedankt en tot ziens')
    elif bakje_hoorntje == "B":
        totaal = ...(aantal_bolletjes)
        bakje = input('Hier is uw bakje met ' + str(aantal_bolletjes) + ' bolletje(s). Wilt u nog meer bestellen? (Y/N)')
        if bakje == 'Y':
            aantal_bolletjes()
        elif bakje == 'N':
            totaal()
            print('Bedankt en tot ziens')
    else:
        print('Sorry dat is geen optie die we aanbieden..')
    
def zakelijk():
    liter = int(input("Hoeveel liter wilt u bestellen?"))
    liters = liter
    while liters > 0:
        input('Welke smaak wilt u voor liter nummer' + str(liter) + '? A) Aardbei, C) Chocolade, V) Vanille?')
        liters -= 1

    prijs = liter * 9.80
    print("Liter     " + str(liter) +  "x 9,80 = " + str(round(prijs,2)))
    print("                                    --------+")
    print("Totaal                              = " + str(prijs))
    print("BTW(6%)                                 = " + str(round(prijs*0.06,2)))
klant = input("Bent u een zakelijke of particuliere klant?Z/P\n")
if klant == "P":
    aantal_bolletjes()
elif klant == "Z":
    zakelijk()

