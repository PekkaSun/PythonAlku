import pygame #Ladataan pygame-kirjasto
	 
tausta_väri = (255,255,255) #Värimäärittelyt RGB (Red Green Blue, jokainen väri 0-255)
(leveys, korkeus) = (300, 200) #Ikkunan koon määritys pikseleinä
	 
ikkuna = pygame.display.set_mode((leveys, korkeus)) #Luodaan ikkuna annetun kokoisena
pygame.display.set_caption('Ohjelma: 1') #Ikkunan otsikko
ikkuna.fill(tausta_väri) #Täytetään ikkuna taustavärillä
	 
pygame.display.flip() #Päivitetään näyttö
	 
while True: #Tehdään niin kauan kuin toiminnassa-lippu on tosi
    for event in pygame.event.get(): #Tarkistetaan tapahtumat
        if event.type == pygame.QUIT: #Jos valittu Lopetus-komento, niin
            break # oiminnassa = False #lopetetaan toiminta asettamalla lippu pois päältä
pygame.quit() #Suljetaan ikkuna
