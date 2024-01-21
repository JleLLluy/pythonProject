from screens import Button, Title
import pygame
import random


def level_up(screen, width, height, fps):
    class HealthUpButton(Button):
        def pressed(self):
            return "health"

    class DamageUpButton(Button):
        def pressed(self):
            return "damage"

    class RateOfFireUpButton(Button):
        def pressed(self):
            return "rate"

    class SpeedUpButton(Button):
        def pressed(self):
            return "speed"

    clock = pygame.time.Clock()
    running = True
    screen_main = screen

    buttons = pygame.sprite.Group()
    titles = pygame.sprite.Group()

    HealthUpButton(buttons, pos=(width // 2 - 160, height // 3), sprite="health_up_proj.png", size=(200, 200))
    DamageUpButton(buttons, pos=(width // 2 + 160, height // 3), sprite="damage_boost.png", size=(200, 200))
    RateOfFireUpButton(buttons, pos=(width // 4, height // 3), sprite="rate_of_fire_proj.png", size=(200, 200))
    SpeedUpButton(buttons, pos=(width // 4 * 3, height // 3), sprite="speed_up_proj.png", size=(200, 200))
    Title(titles, pos=(width // 4, height // 3 - 140), slides_and_sizes=[["rate_of_fire_t_proj.png", (285, 30)]])
    Title(titles, pos=(width // 2 - 160, height // 3 - 140), slides_and_sizes=[["health_t_proj.png", (155, 30)]])
    Title(titles, pos=(width // 2 + 160, height // 3 - 140), slides_and_sizes=[["damage_t_proj.png", (177, 30)]])
    Title(titles, pos=(width // 4 * 3, height // 3 - 140), slides_and_sizes=[["speed_up_t_proj.png", (126, 33)]])

    while running:
        print(running)
        clock.tick(fps)
        screen_main.fill("Black")
        mouse_coord = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for button in buttons:
            if button.rect.collidepoint(mouse_coord):
                button.image = button.img_pressed
                if pygame.mouse.get_pressed()[0]:
                    button.pressed()
                else:
                    button.pushed = False
            else:
                button.image = button.img_unpressed

        for i in range(80):
            screen.fill(pygame.Color('white'),
                        (random.random() * width,
                         random.random() * height, 2, 2))
        buttons.update()
        buttons.draw(screen_main)
        titles.draw(screen_main)
        pygame.display.flip()
