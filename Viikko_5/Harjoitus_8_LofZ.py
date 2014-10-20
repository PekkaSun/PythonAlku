""" **************************************
                                         *
           Legenda Peli                  *
                                         *
************************************** """ 
import pygame, sys

def PiirraHahmo(suunta, x, y):
    # Piirretään hahmo
        if suunta == OIKEA:
            ikkuna.blit(hahmo_o, (x*20, y*20))
        if suunta == VASEN:
            ikkuna.blit(hahmo_v, (x*20, y*20))
        if suunta == ALAS:
            ikkuna.blit(hahmo_a, (x*20, y*20))
        if suunta == YLOS:
            ikkuna.blit(hahmo_y, (x*20, y*20)) 

LEVEYS = 800
KORKEUS = 600

Alusta =["XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X  X  X    X     XX X  X       XX      X",
"X  X  X   XXXX  XXX X  XXXX  XXXX      X",
"X  X  XX  XXXX  XXX X  X               X",
"X XXX X    X     X  XX XX  XXXXXX   XXXX",
"X XX  XX   XX XXXX  X   X    XXXX    XXX",
"X XX XXX XXXX   XX XXXXXX   XXXXXX  XXXX",
"X        X                    XXXX     X",
"X XX XXX   XXXXX              XXX    XXX",
"X XX XXXXX   XXX              XX    XXXX",
"X XX  XX   XXXXX              XXX      X",
"X    XXX     XXXXX            XXX     XXX",
"X XXX XXXXXXX                XX     XXXX",
"X XXX X                              XXX",
"X XXX X       O              XXXXXX   XX",
"X XXX X                      XX    XXXXX",
"X      XX                    X   XXX  XX",
"X X X X  X X X  X X X  X X   X X  X  XXX",
"X X                XXXXX     XX     XXXX",
"XX        X                  XXX     XXX",
"XX        X        xxxxx     XXX   XXXXX",
"X        XXXX                XXXXX  XXXX",
"X  XXX        XX             XXXX   XXXX",
"X          XXXXX      XXXX            XX",
"X     XXXXX                 XX      XXXX",
"X           XXXXX           XXXXXX    XX",
"X        XXXXX               XX     XXXX",
"X                             XX      XX",
"X                             XX    XXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"]


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
fontti = pygame.font.Font(None, 60)
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

#Haetaan hahmon aloituspaikka
for i in range(0,40):
    for j in range (0,30):
        if Alusta[j][i] == "O":
            hahmo_paikka_x = i
            hahmo_paikka_y = j
            break
        
valmis = False
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
                if hahmo_paikka_x < 40 and Alusta[hahmo_paikka_y][hahmo_paikka_x+1]!="X":
                    hahmo_paikka_x += 1
            elif event.key == pygame.K_UP:
                suunta = YLOS
                if hahmo_paikka_y > 1 and Alusta[hahmo_paikka_y-1][hahmo_paikka_x]!="X":
                    hahmo_paikka_y -= 1
            elif event.key == pygame.K_DOWN:
                suunta = ALAS
                if hahmo_paikka_y < 30 and Alusta[hahmo_paikka_y+1][hahmo_paikka_x]!="X":
                    hahmo_paikka_y += 1

    # Piirretään kentän pohja (Alusta-taulukosta)
    for i in range(0,40):
        for j in range (0,30):
            if Alusta[j][i] == "X":
                #pygame.draw.rect(ikkuna, valkoinen, (0+i*20,0+j*20,20,20))
                ikkuna.blit(muuri, (i*20, j*20))
            else:
                #pygame.draw.rect(ikkuna, musta, (0+i*20,0+j*20,20,20))
                ikkuna.blit(ruoho, (i*20, j*20))

    # Piirretään hahmo
    PiirraHahmo(suunta, hahmo_paikka_x, hahmo_paikka_y)

    # Rajoitetaan päivitys 25 frameen sekunnissa
    kello.tick(25)
    
    # Päivitetään näyttö
    pygame.display.flip()
# ------------- Pääohjelman silmukka loppuu tähän  ----------

# Lopetetaan ohjelma.
pygame.quit()


