""" **************************************
                                         *
           Legenda Peli                  *
                                         *
************************************** """ 
import pygame, sys
import random

           
LEVEYS = 800
KORKEUS = 600
RUUDUN_KOKO = 20
KENTAN_LEVEYS = (int)(LEVEYS/RUUDUN_KOKO)
KENTAN_KORKEUS = (int)(KORKEUS/RUUDUN_KOKO)


# Pygamen initialisointi
pygame.init()
 
# Asetetaan ikkunan korkeus ja leveys
ikkunan_koko = [LEVEYS, KORKEUS]
ikkuna = pygame.display.set_mode(ikkunan_koko)

pygame.display.set_caption("Nappaa haamu!")

# Määritellään värit
musta = (0, 0, 0)
valkoinen = (255, 255, 255)
sininen = (0, 0, 255)
maila_vari = (0, 125, 155)
teksti_vari = (120,0,200)

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

# ---------------------------------------------------------------------
def PiirraHaamu(suunta, x, y):
    # Piirretään hahmo
    if suunta == OIKEA:
        ikkuna.blit(haamu_o, (x*RUUDUN_KOKO, y*RUUDUN_KOKO))
    if suunta == VASEN:
        ikkuna.blit(haamu_v, (x*RUUDUN_KOKO, y*RUUDUN_KOKO))
    if suunta == ALAS:
        ikkuna.blit(haamu_a, (x*RUUDUN_KOKO, y*RUUDUN_KOKO))
    if suunta == YLOS:
        ikkuna.blit(haamu_y, (x*RUUDUN_KOKO, y*RUUDUN_KOKO))        

def HaamunAloituspaikka():
    #Haetaan haamun aloituspaikka
    for i in range(0,KENTAN_LEVEYS):
        for j in range (0,KENTAN_KORKEUS):
            if Alusta[j][i] == "H":
                return i, j
# ----------------------------------------------------------------------

def HaeKentta(nimi):
    rivi = 0
    with open(nimi, "r") as f:
        for line in f:
            Alusta.insert(rivi, line)
            rivi += 1

# Haetaan kello näytön päivitystä varten
kello = pygame.time.Clock()

# Luodaan fontti
fontti = pygame.font.Font(None, 80)
fontti.set_bold(True)
fontti.set_italic(True)

# Ladataan hahmot
hahmo_y = pygame.image.load("hahmo_y.png") #Ylös
hahmoRect = hahmo_y.get_rect()
hahmo_a = pygame.image.load("hahmo_a.png") #Alas
hahmo_o = pygame.image.load("hahmo_o.png") #Oikea
hahmo_v = pygame.image.load("hahmo_v.png") #Vasen

# Haamu ----------------------------------------------------
haamu_y = pygame.image.load("haamu_y.png") #Ylös
haamu_a = pygame.image.load("haamu_a.png") #Alas
haamu_o = pygame.image.load("haamu_o.png") #Oikea
haamu_v = pygame.image.load("haamu_v.png") #Vasen
# ----------------------------------------------------------

# Maaston kuvat
muuri = pygame.image.load("muuri.png") #Muuri
ruoho = pygame.image.load("maa_1.png") #Ruoho
vesi = pygame.image.load("vesi.png") #Ruoho

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

# Haamun alkuasetukset ------------------------------------------------------------
haamu_paikka_x = 0
haamu_paikka_y = 0
haamu_paikka_x, haamu_paikka_y = HaamunAloituspaikka()
haamu_askeleet = 0
haamu_siirto = 0
haamu_askeleet_ennen_muutosta = random.randrange(5,21)
haamu_suunta = random.randrange(1,5) # Valitaan suunta sattumanvaraisesti 1-4
# ---------------------------------------------------------------------------------


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
                if Alusta[j][i] == "V": 
                    ikkuna.blit(vesi, (i*RUUDUN_KOKO, j*RUUDUN_KOKO))
                else:
                    ikkuna.blit(ruoho, (i*RUUDUN_KOKO, j*RUUDUN_KOKO))
    # Piirretään hahmo
    PiirraHahmo(suunta, hahmo_paikka_x, hahmo_paikka_y)
# -------------------------------------------------------------------------------------------------------------
    # Siiretään haamua
    haamu_siirto += 1 # Päivitetään haamu paikkaa vain kerran neljästä näytön päivityskerrasta
    if haamu_siirto > 4:
        haamu_siirto = 0
        haamu_askeleet += 1
        # Tarkistetaan askeleet ennen muutosta
        if haamu_askeleet > haamu_askeleet_ennen_muutosta:
            haamu_askeleet_ennen_muutosta = random.randrange(5,21)
            haamu_suunta = random.randrange(1,5)
            
        if haamu_suunta == VASEN:
            if haamu_paikka_x > 1  and Alusta[haamu_paikka_y][haamu_paikka_x-1]!="X":
                haamu_paikka_x -= 1
            elif Alusta[haamu_paikka_y][haamu_paikka_x-1]=="X":
                haamu_suunta = OIKEA
        if haamu_suunta == OIKEA:
            if haamu_paikka_x <= KENTAN_LEVEYS-2 and Alusta[haamu_paikka_y][haamu_paikka_x+1]!="X":
                haamu_paikka_x += 1
            elif Alusta[haamu_paikka_y][haamu_paikka_x+1]=="X":
                haamu_suunta = VASEN
        if haamu_suunta == YLOS:
            if haamu_paikka_y > 1 and Alusta[haamu_paikka_y-1][haamu_paikka_x]!="X":
                haamu_paikka_y -= 1
            elif Alusta[haamu_paikka_y-1][haamu_paikka_x]=="X":
                haamu_suunta = ALAS            
        if haamu_suunta == ALAS:
            if haamu_paikka_y <= KENTAN_KORKEUS-2 and Alusta[haamu_paikka_y+1][haamu_paikka_x]!="X":
                haamu_paikka_y += 1
            elif Alusta[haamu_paikka_y+1][haamu_paikka_x]=="X":
                haamu_suunta = YLOS            

    # Piirretään haamu
    PiirraHaamu(haamu_suunta, haamu_paikka_x, haamu_paikka_y)

    if haamu_paikka_x == hahmo_paikka_x and haamu_paikka_y == hahmo_paikka_y:
        while not valmis:
            # Huonosti kävi -- haamu sai sinut
            teksti = "Nappasit haamun!"
            loppu_teksti = fontti.render(teksti, True, valkoinen)
            ikkuna.blit(loppu_teksti,(100, 150))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                    # Odotellaan X-näppäintä
                        valmis = True      
# --------------------------------------------------------------------------------------------------------------
    # Rajoitetaan päivitys 25 frameen sekunnissa
    kello.tick(25)
    
    # Päivitetään näyttö
    pygame.display.flip()
# ------------- Pääohjelman silmukka loppuu tähän  ----------

# Lopetetaan ohjelma.
pygame.quit()


