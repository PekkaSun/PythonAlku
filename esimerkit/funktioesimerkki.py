""" **************************************
                                         *
           Pomppiva neliö                *
                                         *
************************************** """ 

import pygame,sys

# Määritellään funktioita, jotka abstraktoivat usein käytettyjä koodinpätkiä
# ja tekevät pääsilmukasta helpommin luettavat.
##
## (Tässä kohtaa perusesimerkkejä funktioista: def plus(x, y) return x+y jne.. ?)
##
## Funktoita on jo käytetty, esim ikkuna.blit() ja kello.tick(). Mitä ne tekevät? Miksi ne ovat funkioita?
##
## Aluksi globaaleja asioita tekevät koodinpätkät voidaan copypasteta funktioihin, jotka tekevät globaaleja asioita
## Myöhemmin paremman tyylin vuoksi funktiot kannattaa muuttaa puhtaiksi funktioiksi, jotka ottavat globaalien muuttujien arvot
## parametreina ja palauttavat niiden uudet arvot, tyyliin (nelio_muutos_x, nelio_muutos_y) = tarkistaTormays(nelio_x,nelio_y)
def piirraPisteet(pisteet, aika):
    teksti = "Pisteet: %d Aika: %10.3f" % (pisteet, loppuAika/1000)
    pisteet_teksti = fontti.render(teksti, True, teksti_vari)
    ikkuna.blit(pisteet_teksti,(50, 30))

def siirraNelio(muutosX, muutosY):
    global nelio_x, nelio_y
    nelio_x += nelio_muutos_x
    nelio_y += nelio_muutos_y

def tarkistaTormays():
    global nelio_x, nelio_y, nelio_muutos_x, nelio_muutos_y, pisteet
    # Tarkistetaan ollaanko osumassa reunaan
    # Jos osutaan, vaihdetaan suuntaa päinvastaiseksi kertomalla -1:llä
    if nelio_y > 450 or nelio_y < 0:
        nelio_muutos_y = nelio_muutos_y * -1
        if nelio_y > 450: # Pohjakosketus vähentää pisteitä
            pisteet -= 1
            nelio_muutos_y -= 1 #Kasvatetaan nopeutta
    if nelio_x > 650 or nelio_x < 0:
        nelio_muutos_x = nelio_muutos_x * -1

def tarkistaMaila():
    global nelio_x, nelio_y, nelio_muutos_x, nelio_muutos_y, maila_x
    # Tarkistetaan osutaanko mailaan
    # Jos osutaan, vaihdetaan suuntaa päinvastaiseksi kertomalla -1:llä
    if nelio_y + 50 > 429 and nelio_muutos_y > 0:
        if nelio_x +50 > maila_x and nelio_x < maila_x+50:
            nelio_muutos_y = nelio_muutos_y * -1
            nelio_muutos_y -= 1 #Kasvatetaan nopeutta
            
# Määritellään värit
musta = (   0,   0,   0)
valkoinen = ( 255, 255, 255)
sininen = (   0,   0,   255)
maila_vari = (   0,   125,   155)
teksti_vari = (120,0,200)

# Pygamen initialisointi
pygame.init()
 
# Asetetaan ikkunan korkeus ja leveys
ikkunan_koko = [700, 500]
ikkuna = pygame.display.set_mode(ikkunan_koko)

pygame.display.set_caption("Pomppiva neliö")

# Haetaan kello näytön päivitystä varten
kello = pygame.time.Clock()

# Luodaan fontti
fontti = pygame.font.Font(None, 60)
fontti.set_bold(True)
fontti.set_italic(True)

# Ladataan taustakuva (kuva on samassa kansiossa) 
taustakuva = pygame.image.load("tausta.jpg")
taustakuvaRect = taustakuva.get_rect() # Haetaan kuvan suorakulmion koordinaatit
# Ladataan pallo
pallo = pygame.image.load("pallo.gif")
palloRect = pallo.get_rect()

# Pisteet
pisteet = 10

# Neliön alkupiste
nelio_x = 50
nelio_y = 50

# Mailan alkupaikka
maila_x = (700 - 50)/2
maila_y = 500 - 70 # y-koordinaatti siis 430
maila_muutos_x = 0

# Neliön liikkeen nopeus(=muutos) x ja y suunnassa
nelio_muutos_x = 8
nelio_muutos_y = 8

loppuAika = 0

# Asetetaan valmis-lippu epätodeksi.
# Pääohjelman silmukka pyörii niin kauan kuin valmis-lippu on False(=epätosi)

# -------- Pääohjelman silmukka -----------
while pisteet > 0:    
    for event in pygame.event.get(): # Haetaan tapahtumat, jos niitä on
        if event.type == pygame.QUIT: # Käyttäjä klikkasi Close-komentoa
            pygame.quit() # valmis-flagi ei toimi enää, koska pääsilmukan jälkeen ohjelma ei vielä pääty, vaan pisteet piirretään, joten
            sys.exit()    # valmis-muuttujaa käyttäen käyttäjän täytyy painaa Close-komentoa kaksi kertaa
                          # Parempi siis vain lopettaa ohjelma suoraan kun saadaan pygame.QUIT tapahtuma
        # Onko käyttäjä painanut näppäintä        
        elif event.type == pygame.KEYDOWN:
            # Oliko nuolinäppäin vasemmalle
            if event.key == pygame.K_LEFT:
                maila_muutos_x = -4
            # Oliko nuolinäppäin oikealle
            elif event.key == pygame.K_RIGHT:
                maila_muutos_x = 4
        # Onko käyttäjä vapauttanut näppäimen        
        elif event.type == pygame.KEYUP:
            # Oliko nuolinäppäin vasemmalle
            if event.key == pygame.K_LEFT:
                maila_muutos_x = 0
            # Oliko nuolinäppäin oikealle
            elif event.key == pygame.K_RIGHT:
                maila_muutos_x = 0 

    # Mailan paikka
    maila_x += maila_muutos_x
    # Tarkistetaan reuna
    if maila_x > 650 or maila_x < 0:
        maila_muutos_x = 0
        
    # Aseteaan taustaväri (black)
    #ikkuna.fill(musta)
    ikkuna.blit(taustakuva, taustakuvaRect)

    piirraPisteet(pisteet, loppuAika/1000)

    # Piirretään maila
    pygame.draw.rect(ikkuna, maila_vari, [maila_x, maila_y, 50, 5])

    # Piirretään pallo
    ikkuna.blit(pallo, (nelio_x, nelio_y))
 
    # Siirretään paikkakoordinaatteja
    siirraNelio(nelio_muutos_x, nelio_muutos_y)

    # Tarkistetaan osutaanko reunaan tai mailaan
    tarkistaTormays()
    tarkistaMaila()
    
    # Rajoitetaan päivitys 25 frameen sekunnissa
    kello.tick(25)
    loppuAika += 40
    
    # Päivitetään näyttö
    pygame.display.flip()
# ------------- Pääohjelman silmukka loppuu tähän  ----------
# Piirretään loppukuva
ikkuna.blit(taustakuva, taustakuvaRect)
piirraPisteet(pisteet, loppuAika/1000)
pygame.display.flip()
    
valmis = False    
while not valmis:    
    for event in pygame.event.get(): # Haetaan tapahtumat, jos niitä on
        if event.type == pygame.KEYDOWN or event.type == pygame.QUIT: # Mikä tahansa näppäin lopettaa ohjelman
                valmis = True 

# Lopetetaan ohjelma.
pygame.quit()
# sys.exit()-kutsu näköjään tarvitaan ikkunan sulkemiseksi ainakin Linux-ymmpäristössä
sys.exit()

