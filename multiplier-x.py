WelkGetal = int(input("welk getal wil je de tafel van zien\n"))
def TafelGetal(InvoerGetal):
    TafelVanX = 1 
    while TafelVanX <= 10:
        tafelvan = InvoerGetal * TafelVanX
        print(TafelVanX, ' x ' , InvoerGetal, ' = ' , tafelvan) 
        TafelVanX = TafelVanX + 1 

    
        
    

TafelGetal(WelkGetal)