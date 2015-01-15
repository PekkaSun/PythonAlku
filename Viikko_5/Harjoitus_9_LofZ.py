""" **************************************
                                         *
           Legenda Peli                  *
                                         *
************************************** """ 
import pygame, sys

def PiirraHahmo(suunta, x, y):
    # Piirretään hahmo
        if suunta == OIKEA:
            ikkuna.blit(hahmo_o, (x*RUUDUN_KOKO, y*RUUDUN_KOKO))
        if suunta == VASEN:
            ikkuna.blit(hahmo_v, (x*RUUDUN_KOKO, y*RUUDUN_KOKO))
        if suunta == ALAS:
            ikkuna.blit(hahmo_a, (x*RUUDUN_KOKO, y*RUUDUN_KOKO))
        if suunta == YLOS:
            ikkuna.blit(hahmo_y, (x*RUUDUN_KOKO, y*RUUDUN_KOKO))

def HahmonAloituspaikka():
    #Haetaan hahmon aloituspaikka
    for i in range(0,KENTAN_LEVEYS):
        for j in range (0,KENTAN_KORKEUS):
            if Alusta[j][i] == "O":
                return i, j
                

def HaeKentta(nimi):
    rivi = 0
    with open(nimi, "r") as f:
        for line in f:
            Alusta.insert(rivi, line)
            rivi += 1
            
LEVEYS = 800
KORKEUS = 600
RUUDUN_KOKO = 20
KENTAN_LEVEYS = (int)(LEVEYS/RUUDUN_KOKO)
KENTAN_KORKEUS = (int)(KORKEUS/RUUDUN_KOKO)

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

pygame.display.set_caption("Legenda Peli")

# Haetaan kello näytön päivitystä varten
kello = pygame.time.Clock()

# Luodaan fontti
fontti = pygame.font.Font(None, 20)
fontti.set_bold(True)
fontti.set_italic(True)

# Ladataan hahmot
hahmo_y = pygame.image.load("hahmo_y.png") #Ylös
hahmoRect = hahmo_y.get_rect()
hahmo_a = pygame.image.load("hahmo_a.png") #Alas
hahmo_o = pygame.image.load("hahmo_o.png") #Oikea
hahmo_v = pygame.image.load("hahmo_v.png") #Vasen

muuri = pygame.image.load("muuri.png") #Muuri
ruoho = pygame.image.load("ruoho.png") #Ruoho

YLOS = 1
ALAS = 2
OIKEA = 3
VASEN = 4

hahmo_paikka_x = 0
hahmo_paikka_y = 0
suunta = YLOS

#Luetaan tekstitiedosto kentän pohjaksi
Alusta = []
HaeKentta("kentta_1.txt")

#Haetaan aloituspaikan koordinaatit    
hahmo_paikka_x, hahmo_paikka_y = HahmonAloituspaikka()
        
valmis = False
askel = 0
# -------- Pääohjelman silmukka -----------
while not valmis:    
    for event in pygame.event.get(): # Haetaan tapahtumat, jos niitä on
        if event.type == pygame.QUIT: # Käyttäjä klikkasi Close-komentoa
            valmis = True # Asetetaan valmis-lippu todeksi -> ohjelma loppuu

        # Onko käyttäjä painanut näppäintä        
        elif event.type == pygame.KEYDOWN:
            # Oliko nuolinäppäin vasemmalle
            if event.key == pygame.K_LEFT:
                suunta = VASEN
                if hahmo_paikka_x > 1  and Alusta[hahmo_paikka_y][hahmo_paikka_x-1]!="X":
                    hahmo_paikka_x -= 1
            # Oliko nuolinäppäin oikealle
            elif event.key == pygame.K_RIGHT:
                suunta = OIKEA
                if hahmo_paikka_x <= KENTAN_LEVEYS-2 and Alusta[hahmo_paikka_y][hahmo_paikka_x+1]!="X":
                    hahmo_paikka_x += 1
            elif event.key == pygame.K_UP:
                suunta = YLOS
                if hahmo_paikka_y > 1 and Alusta[hahmo_paikka_y-1][hahmo_paikka_x]!="X":
                    hahmo_paikka_y -= 1
            elif event.key == pygame.K_DOWN:
                suunta = ALAS
                if hahmo_paikka_y <= KENTAN_KORKEUS-2 and Alusta[hahmo_paikka_y+1][hahmo_paikka_x]!="X":
                    hahmo_paikka_y += 1

    # Piirretään kentän pohja (Alusta-taulukosta)
    for i in range(0,KENTAN_LEVEYS):
        for j in range (0,KENTAN_KORKEUS):
            if Alusta[j][i] == "X":
                ikkuna.blit(muuri, (i*RUUDUN_KOKO, j*RUUDUN_KOKO))
            else:
                ikkuna.blit(ruoho, (i*RUUDUN_KOKO, j*RUUDUN_KOKO))

    # Piirretään hahmo
    PiirraHahmo(suunta, hahmo_paikka_x, hahmo_paikka_y)

    # Rajoitetaan päivitys 25 frameen sekunnissa
    kello.tick(25)
    
    # Päivitetään näyttö
    pygame.display.flip()
# ------------- Pääohjelman silmukka loppuu tähän  ----------

# Lopetetaan ohjelma.
pygame.quit()


