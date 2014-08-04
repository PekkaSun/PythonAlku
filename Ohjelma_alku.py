import pygame
	 
tausta_väri = (255,255,255) #Värimäärittelyt RGB
(leveys, korkeus) = (300, 200) #Ikkunan koon määritys
	 
ikkuna = pygame.display.set_mode((leveys, korkeus))
pygame.display.set_caption('Ohjelma: 1') #Ikkunan otsikko
ikkuna.fill(tausta_väri)
	 
pygame.display.flip()
	 
toiminnassa = True 
while toiminnassa:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            toiminnassa = False
pygame.quit()
