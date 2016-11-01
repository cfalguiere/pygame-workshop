# Afficher les instructions
import sys, pygame

# défini le canvas d'affichage
pygame.init()
width = 320
height = 240
window_size = ( width, height )
color_black = ( 0, 0, 0 )
color_red   = ( 255, 0, 0)
screen = pygame.display.set_mode(window_size)

# charge l'image de la balle
ball = pygame.image.load("ball.bmp")
ballrect = ball.get_rect()

# Les objets font (ou fontes en français) définissent la faàon d'écrire des lettres, c'est à dire la police de caractère et la taille des caractères.
#Il existe plusieurs polices de caractères, plus ou moins rondes ou anguleuses, manga ou en bulle. Helvetica est une polce de caractères. On l'utilise ici en 19 points.
pygame.font.init()
labelFont = pygame.font.SysFont("Helvetica", 18)
print(pygame.font.get_fonts())

# intialise le vecteur de déplacement à immobile
speed_vector = [0, 0]

while True:
    for event in pygame.event.get():
        # pour le bouton de fermeture de la fenêtre, quitte le programme
        if event.type == pygame.QUIT:
           sys.exit()
        # pour l'utilisation des touches, modifie le vecteur de déplacement
        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_RIGHT:
              speed_vector = [20, 0]
           if event.key == pygame.K_LEFT:
              speed_vector = [-20, 0]
           if event.key == pygame.K_UP:
              speed_vector = [0, -20]
           if event.key == pygame.K_DOWN:
              speed_vector = [0, 20]
        if event.type == pygame.KEYUP:
              speed_vector = [0, 0]


    # reaffiche le fond et la balle en tenant compte du déplacement
    screen.fill(color_black)

    # affiche le texte
    label = labelFont.render("Déplacez la balle avec les flèches", True, color_red)
    labelPosition = ( (width - label.get_rect().width)/2,
                      (height - label.get_rect().height)/2 )
    screen.blit(label, labelPosition)

    # affiche la balle
    ballrect = ballrect.move(speed_vector)
    screen.blit(ball, ballrect)

    pygame.display.flip()

