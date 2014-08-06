import pygame #Ladataan pygame-kirjasto
	 
tausta_väri = (255,255,255) #Värimäärittelyt RGB (Red Green Blue, jokainen väri 0-255)
(leveys, korkeus) = (300, 200) #Ikkunan koon määritys pikseleinä
	 
ikkuna = pygame.display.set_mode((leveys, korkeus)) #Luodaan ikkuna annetun kokoisena
pygame.display.set_caption('Ohjelma: 3') #Ikkunan otsikko
ikkuna.fill(tausta_väri) #Täytetään ikkuna taustavärillä

#Piirretään ympyrä
#Funktio: pygame.draw.circle(piirtoikkuna, väri(RGB), keskipisteen paikka, säde, reunan paksuus)
#Huom! Jos reunan paksuudeksi laitetaan 0, niin ympyrä täytetään värillä
x = 150 #Ympyrän keskipisteen x-koordinaatti
y = 50 #Ympyrän keskipisteen y-koordinaatti
pygame.draw.circle (ikkuna, (0,255,0), (x,y), 15, 1)

kierros = 15 #Kierrosten lukumäärä
toiminnassa = True #Asetetaan toiminnassa-lippu päälle (=tosi)

while kierros>0: #Tehdään niin kauan kun kierroslaskuri on suurempi kuin nolla
    pygame.display.flip() #Päivitetään näyttö

    pygame.draw.circle (ikkuna, (0,255,0), (x,y), 15, 1)  #Piirretään ympyrä
    x = x+1 #Lisätään x-koordinaatin arvoa yhdellä	 
    y += 1 #Sama yhden lisäys voidaan kirjoittaa myös näin
    kierros -= 1 #Vähennetään kierroslaskuria yhdellä
    
while toiminnassa:
    for event in pygame.event.get(): #Tarkistetaan tapahtumat
        if event.type == pygame.QUIT: #Jos valittu Lopetus-komento, niin
            toiminnassa = False #lopetetaan toiminta asettamalla lippu pois päältä
pygame.quit() #Suljetaan ikkuna
