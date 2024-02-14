import random
import pygame
import sys
import pyperclip

def print_github_link():
    font = pygame.font.Font(None, 16)
    text = font.render("GitHub: github.com/mateusartico", True, black)
    text_rect = text.get_rect(center=(100, 10))
    screen.blit(text, text_rect)

def draw_button(rectangle, text):
    pygame.draw.rect(screen, black, rectangle)

    font = pygame.font.SysFont(None, 24)
    text_rendered = font.render(text, True, white)
    text_width, text_height = font.size(text)
    text_x = rectangle.centerx - text_width / 2
    text_y = rectangle.centery - text_height / 2
    screen.blit(text_rendered, (text_x, text_y))

def write_text():
    font = pygame.font.SysFont(None, 48)
    render_text = font.render(password, True, black)
    pos_x = (width - render_text.get_width()) // 2
    pos_y = (height - render_text.get_height()) // 3
    screen.blit(render_text, (pos_x, pos_y))

def screen_update():
    screen.fill(white)
    write_text()
    draw_button(button_generate, "GENERATE")
    draw_button(button_copy, "COPY")
    print_github_link()

def create_password():
    char = list('!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~')
    new_password = ''
    for i in range(8):
        new_password += char[random.randint(0, (len(char) - 1))]

    return new_password

if not __name__ == '__main__':
    sys.exit()

pygame.init()

width = 300
height = 400

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Password Generator")

white = (255, 255, 255)
black = (0, 0, 0)

password = create_password()

buttons_width = 200
buttons_height = 50

button_generate_x = (width - buttons_width) // 2
button_generate_y = (height - buttons_height * 4 - 15)
button_generate = pygame.Rect(button_generate_x, button_generate_y, buttons_width, buttons_height)

button_copy_x = (width - buttons_width) // 2
button_copy_y = (height - buttons_height * 3)
button_copy = pygame.Rect(button_copy_x, button_copy_y, buttons_width, buttons_height)

screen_update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_generate.collidepoint(event.pos):
                password = create_password()
                screen_update()
            elif button_copy.collidepoint(event.pos):
                pyperclip.copy(password)

    pygame.display.update()