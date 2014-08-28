import pygame #Ladataan pygame-kirjasto

#Tehtävä 1: Määritä ikkunan väri. RGB värimääritys (Red Green Blue, jokainen väri 0-255)
tausta_väri = () #Värimäärittelyt

#Tehtävä 2: Määritä ikkunan koko, leveys ja korkeus pikseleinä
(leveys, korkeus) = () #Ikkunan koko
	 
ikkuna = pygame.display.set_mode((leveys, korkeus)) #Luodaan ikkuna annetun kokoisena

#Tehtävä 3: Kirjoita ikkunalle otsikko. Otsikkoteksti lainausmerkkeihin 'Otsikko'
pygame.display.set_caption() #Ikkunan otsikko
ikkuna.fill(tausta_väri) #Täytetään ikkuna taustavärillä
	 
pygame.display.flip() #Päivitetään näyttö

#Tehtävä 4: Aseta toiminnassa-lippu päälle eli tosi (=True) asentoon	 
toiminnassa =  #Aetetaan toiminnassa-lippu päälle
while toiminnassa: #Tehdään niin kauan kuin toiminnassa-lippu on tosi
    for event in pygame.event.get(): #Tarkistetaan tapahtumat
        if event.type == pygame.QUIT: #Jos valittu Lopetus-komento, niin

            #Tehtävä 5: Aseta toiminnassa-lippu pois päältä eli on epätosi (=False)
            toiminnassa =  #lopetetaan toiminta asettamalla lippu pois päältä
            
pygame.quit() #Suljetaan ikkuna

