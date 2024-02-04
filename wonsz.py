import pygame
import random   

pygame.init()

biały = (255, 255, 255)
czarny = (0, 0, 0)
czerwony = (213, 50, 80)
zielony = (0, 255, 0)

szerokość_ekranu = 600
wysokość_ekranu = 400

ekran = pygame.display.set_mode((szerokość_ekranu, wysokość_ekranu))
pygame.display.set_caption('Gra Snake')

zegar = pygame.time.Clock()

rozmiar_snake = 10
predkosc_snake = 15

font_style = pygame.font.SysFont(None, 35)
score_font = pygame.font.SysFont("comicsansms", 35)

def nasz_wąż(rozmiar_snake, lista_snake):
    for x in lista_snake:
        pygame.draw.rect(ekran, czarny, [x[0], x[1], rozmiar_snake, rozmiar_snake])

def wiadomość(msg, kolor):
    mesg = font_style.render(msg, True, kolor)
    ekran.blit(mesg, [szerokość_ekranu / 6, wysokość_ekranu / 3])

def your_score(score):
    value = score_font.render("Twój wynik: " + str(score), True, czarny)
    ekran.blit(value, [0, 0])

def gra():
    gra_aktywna = True
    gra_zakończona = False

    x1 = szerokość_ekranu / 2
    y1 = wysokość_ekranu / 2

    x1_zmiana = 0       
    y1_zmiana = 0
    ostatni_ruch = None

    lista_snake = []
    długość_snake = 1

    jedzeniex = round(random.randrange(0, szerokość_ekranu - rozmiar_snake) / 10.0) * 10.0
    jedzeniey = round(random.randrange(0, wysokość_ekranu - rozmiar_snake) / 10.0) * 10.0
    
    while gra_aktywna:
        while gra_zakończona:
            ekran.fill(biały)
            wiadomość("Przegrałeś! Naciśnij C-Continue lub Q-Quit", czerwony)
            your_score(długość_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gra_aktywna = False
                        gra_zakończona = False
                    if event.key == pygame.K_c:
                        gra()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gra_aktywna = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and ostatni_ruch != "RIGHT":
                    x1_zmiana = -rozmiar_snake
                    y1_zmiana = 0
                    ostatni_ruch = "LEFT"
                elif event.key == pygame.K_RIGHT and ostatni_ruch != "LEFT":
                    x1_zmiana = rozmiar_snake
                    y1_zmiana = 0
                    ostatni_ruch = "RIGHT"
                elif event.key == pygame.K_UP and ostatni_ruch != "DOWN":
                    y1_zmiana = -rozmiar_snake
                    x1_zmiana = 0
                    ostatni_ruch = "UP"
                elif event.key == pygame.K_DOWN and ostatni_ruch != "UP":
                    y1_zmiana = rozmiar_snake
                    x1_zmiana = 0
                    ostatni_ruch = "DOWN"

        if x1 >= szerokość_ekranu or x1 < 0 or y1 >= wysokość_ekranu or y1 < 0:
            gra_zakończona = True

        x1 += x1_zmiana
        y1 += y1_zmiana
        ekran.fill(biały)
        pygame.draw.rect(ekran, zielony, [jedzeniex, jedzeniey, rozmiar_snake, rozmiar_snake])
        głowa_snake = []
        głowa_snake.append(x1)
        głowa_snake.append(y1)
        lista_snake.append(głowa_snake)
        if len(lista_snake) > długość_snake:
            del lista_snake[0]

        for x in lista_snake[:-1]:
            if x == głowa_snake:
                gra_zakończona = True

        nasz_wąż(rozmiar_snake, lista_snake)
        your_score(długość_snake - 1)
        pygame.display.update()

        if x1 == jedzeniex and y1 == jedzeniey:
            jedzeniex = round(random.randrange(0, szerokość_ekranu - rozmiar_snake) / 10.0) * 10.0
            jedzeniey = round(random.randrange(0, wysokość_ekranu - rozmiar_snake) / 10.0) * 10.0
            długość_snake += 1

        zegar.tick(predkosc_snake)

    pygame.quit()
    quit()

gra()
