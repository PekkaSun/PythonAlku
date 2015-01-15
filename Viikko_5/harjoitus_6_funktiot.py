""" **************************************
                                         *
           Pomppiva neliö                *
                                         *
************************************** """ 
import pygame

LEVEYS = 700
KORKEUS = 500
MAILA = 50
MAILAN_PAIKKA = KORKEUS-70

def kirjoitaPisteet(pisteet, loppuAika):
    teksti = "Pisteet: %d Aika: %10.3f" % (pisteet, loppuAika/1000)
    pisteet_teksti = fontti.render(teksti, True, teksti_vari)
    ikkuna.blit(pisteet_teksti,(50, 30))

def tarkistaReunaosuma():
    global nelio_x, nelio_y, nelio_muutos_x, nelio_muutos_y, pisteet

    # Jos osutaan, vaihdetaan suuntaa päinvastaiseksi kertomalla -1:llä
    if nelio_y > KORKEUS-MAILA or nelio_y < 0:
        nelio_muutos_y = nelio_muutos_y * -1
        if nelio_y > KORKEUS-MAILA: # Pohjakosketus vähentää pisteitä
            pisteet -= 1
    if nelio_x > LEVEYS-MAILA or nelio_x < 0:
        nelio_muutos_x = nelio_muutos_x * -1
    
def tarkistaMailaosuma():
    global nelio_x, nelio_y, maila_x, maila_y, nelio_muutos_y, osuma_aani
    # Jos osutaan, vaihdetaan suuntaa päinvastaiseksi kertomalla -1:llä
    if nelio_y + MAILA > MAILAN_PAIKKA and nelio_muutos_y > 0:
        if nelio_x + MAILA > maila_x and nelio_x < maila_x+MAILA:
            nelio_muutos_y = nelio_muutos_y * -1
            osuma_aani.play()

def siirraPaikkaa():
    global nelio_x, nelio_y, nelio_muutos_x, nelio_muutos_y
    # Siirrä paikkaa
    nelio_x += nelio_muutos_x
    nelio_y += nelio_muutos_y
    
# Määritellään värit
musta = (0, 0, 0)
valkoinen = (255, 255, 255)
sininen = (0, 0, 255)
maila_vari = (0, 125, 155)
teksti_vari = (120,0,200)

# Pygamen initialisointi
pygame.init()
 
# Asetetaan ikkunan korkeus ja leveys
ikkunan_koko = [LEVEYS, KORKEUS]
ikkuna = pygame.display.set_mode(ikkunan_koko)

pygame.display.set_caption("Pomppiva neliö")
#Haetaan osumaääni
osuma_aani = pygame.mixer.Sound("Boing.wav")

# Haetaan kello näytön päivitystä varten
kello = pygame.time.Clock()

# Luodaan fontti
fontti = pygame.font.Font(None, 60)
fontti.set_bold(True)
fontti.set_italic(True)

# Ladataan taustakuva (kuvat ovat samassa kansiossa) 
taustakuva = pygame.image.load("tausta.jpg") #Kuvan koko sama kuin ikkunan koko
taustakuvaRect = taustakuva.get_rect() # Haetaan kuvan suorakulmion koordinaatit
# Ladataan pallo
pallo = pygame.image.load("pallo.gif") #Pallon koko 50*50
palloRect = pallo.get_rect()

# Pisteet
pisteet = 20
# Neliön alkupiste
nelio_x = 50
nelio_y = 50

# Mailan alkupaikka
maila_x = (LEVEYS - MAILA)/2
maila_y = MAILAN_PAIKKA # y-koordinaatti siis 430
maila_muutos_x = 0

# Neliön liikkeen nopeus(=muutos) x ja y suunnassa
nelio_muutos_x = 4
nelio_muutos_y = 4

loppuAika = 0

# Asetetaan valmis-lippu epätodeksi.
# Pääohjelman silmukka pyörii niin kauan kuin valmis-lippu on False(=epätosi)
valmis = False

# -------- Pääohjelman silmukka -----------
while valmis == False and pisteet > 0:    
    for event in pygame.event.get(): # Haetaan tapahtumat, jos niitä on
        if event.type == pygame.QUIT: # Käyttäjä klikkasi Close-komentoa
            valmis = True # Asetetaan valmis-lippu todeksi -> ohjelma loppuu

        # Onko käyttäjä painanut näppäintä        
        elif event.type == pygame.KEYDOWN:
            # Oliko nuolinäppäin vasemmalle
            if event.key == pygame.K_LEFT:
                maila_muutos_x = -4
            # Oliko nuolinäppäin oikealle
            elif event.key == pygame.K_RIGHT:
                maila_muutos_x = 4
        # Onko käyttäjä vapsiirraPaikkaa()auttanut näppäimen        
        elif event.type == pygame.KEYUP:
            # Oliko nuolinäppäin vasemmalle
            if event.key == pygame.K_LEFT:
                maila_muutos_x = 0
            # Oliko nuolinäppäin oikealle
            elif event.key == pygame.K_RIGHT:
                maila_muutos_x = 0 

    # Mailan paikka
    maila_x += maila_muutos_x
        
    # Aseteaan taustaväri (black)
    ikkuna.blit(taustakuva, taustakuvaRect)

    # Tarkistetaan reuna
    if maila_x > LEVEYS-MAILA or maila_x < 0:
        maila_muutos_x = 0
        
    # KirjoitaPisteet näyttöön
    kirjoitaPisteet(pisteet, loppuAika)

    # Piirretään maila
    pygame.draw.rect(ikkuna, maila_vari, [maila_x, maila_y, MAILA, 5])

    # Piirretään pallo
    ikkuna.blit(pallo, (nelio_x, nelio_y))

    # Siirretään paikkakoordinaatteja
    siirraPaikkaa()

    # Tarkistetaan ollaanko osumassa reunaan
    tarkistaReunaosuma()

    # Tarkistetaan osutaanko mailaan
    tarkistaMailaosuma()
        
    # Rajoitetaan päivitys 25 frameen sekunnissa
    kello.tick(25)
    loppuAika += 40
    
    # Päivitetään näyttö
    pygame.display.flip()
# ------------- Pääohjelman silmukka loppuu tähän  ----------

# Lopetetaan ohjelma.
pygame.quit()
system.exit()

