""" **************************************
                                         *
           Pomppiva neliö                *
                                         *
************************************** """ 

import pygame

# Määritellään värit
musta = (   0,   0,   0)
valkoinen = ( 255, 255, 255)
sininen = (   0,   0,   255)

# Pygamen initialisointi
pygame.init()
 
# Asetetaan ikkunan korkeus ja leveys
ikkunan_koko = [700, 500]
ikkuna = pygame.display.set_mode(ikkunan_koko)

pygame.display.set_caption("Pomppiva neliö")

# Haetaan kello näytön päivitystä varten
kello = pygame.time.Clock()

# Neliön alkupiste
nelio_x = 50
nelio_y = 50

# Mailan alkupaikka
maila_x = (700 - 50)/2
maila_y = 500 - 70 # y-koordinaatti siis 430
maila_muutos_x = 0

# Neliön liikkeen nopeus(=muutos) x ja y suunnassa
nelio_muutos_x = 4
nelio_muutos_y = 4

# Asetetaan valmis-lippu epätodeksi.
# Pääohjelman silmukka pyörii niin kauan kuin valmis-lippu on False(=epätosi)
valmis = False

# -------- Pääohjelman silmukka -----------
while valmis == False:    
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
    ikkuna.fill(musta)

    # Piirretään maila
    pygame.draw.rect(ikkuna, valkoinen, [maila_x, maila_y, 50, 5])

    # Piirretään neliö (iso valkoinen ja sisälle pienempi sininen)
    pygame.draw.rect(ikkuna, valkoinen, [nelio_x, nelio_y, 50, 50])
    pygame.draw.rect(ikkuna, sininen, [nelio_x + 10, nelio_y + 10, 30, 30])
 
    # Siirretään paikkakoordinaatteja
    nelio_x += nelio_muutos_x
    nelio_y += nelio_muutos_y

    # Tarkistetaan ollaanko osumassa reunaan
    # Jos osutaan, vaihdetaan suuntaa päinvastaiseksi kertomalla -1:llä
    if nelio_y > 450 or nelio_y < 0:
        nelio_muutos_y = nelio_muutos_y * -1

    if nelio_x > 650 or nelio_x < 0:
        nelio_muutos_x = nelio_muutos_x * -1

    # Tarkistetaan osutaanko mailaan
    # Jos osutaan, vaihdetaan suuntaa päinvastaiseksi kertomalla -1:llä
    if nelio_y + 50 > 429 and nelio_muutos_y > 0:
        if nelio_x +50 > maila_x and nelio_x < maila_x+50:
            nelio_muutos_y = nelio_muutos_y * -1
            nelio_muutos_y -= 1
        
    # Rajoitetaan päivitys 25 frameen sekunnissa
    kello.tick(25)

    # Päivitetään näyttö
    pygame.display.flip()
# ------------- Pääohjelman silmukka loppuu tähän  ----------    

# Lopetetaan ohjelma.
pygame.quit()

