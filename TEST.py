import pygame
import sys
from button import Button
import textwrap
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def get_credits_font(size):
    return pygame.font.Font("assets/font-credits.ttf", size)

def draw_text(text, font, size, color, position):
    text_surface = font(size).render(text, True, color)
    text_rect = text_surface.get_rect(center=position)
    SCREEN.blit(text_surface, text_rect)

def draw_buttons(buttons, mouse_pos):
    for button in buttons:
        button.changeColor(mouse_pos)
        button.update(SCREEN)

def handle_events(buttons, mouse_pos):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for index, button in enumerate(buttons):
                if button.checkForInput(mouse_pos):
                    return index
    return None

def start_quiz(category, difficulty):
    from quiz_data import get_quiz_data

    quiz_data = get_quiz_data(category)
    quiz_data = random.sample(quiz_data, 10)
    question_index = 0
    score = 0
    start_time = pygame.time.get_ticks()

    if difficulty == "Easy":
        time_limit = 300000
    elif difficulty == "Normal":
        time_limit = 60000
    elif difficulty == "Hard":
        time_limit = 10000

    while True:
        mouse_pos = pygame.mouse.get_pos()
        SCREEN.fill("black")
        current_time = pygame.time.get_ticks()
        if current_time - start_time > time_limit:
            print("Time's up!")
            break

        remaining_time = (time_limit - (current_time - start_time)) / 1000
        draw_text(f"Time Remaining: {remaining_time:.2f} seconds", get_font, 10, "White", (1100, 10))

        question = quiz_data[question_index]['question']
        wrapped_question = textwrap.wrap(question, width=40)

        for i, line in enumerate(wrapped_question):
            draw_text(line, get_font, 30, "White", (SCREEN_WIDTH // 2, 100 + i * 40))
        
        choices = quiz_data[question_index]['choices']
        choice_buttons = [Button(image=None, pos=(640, 250 + i * 70),
                                 text_input=choice, font=get_font(30), base_color="White", hovering_color="Green")
                          for i, choice in enumerate(choices)]
        
        draw_buttons(choice_buttons, mouse_pos)

        selected_index = handle_events(choice_buttons, mouse_pos)

        if selected_index is not None:
            if choices[selected_index] == quiz_data[question_index]['answer']:
                print("Correct!")
                score += 1
            else:
                print("Incorrect!")
                score += 0

            question_index += 1
            if question_index >= len(quiz_data):
                break

        pygame.display.update()

    end_time = pygame.time.get_ticks()
    elapsed_time = (end_time - start_time) / 1000

    while True:
        mouse_pos = pygame.mouse.get_pos()
        SCREEN.fill("black")

        draw_text(f"Final Score: {score}/10", get_font, 50, "White", (SCREEN_WIDTH // 2, 100))
        draw_text(f"Time Taken: {elapsed_time:.2f} seconds", get_font, 50, "White", (SCREEN_WIDTH // 2, 200))

        back_button = Button(image=None, pos=(640, 620),
                             text_input="Back", font=get_font(50), base_color="White", hovering_color="Green")
        back_button.changeColor(mouse_pos)
        back_button.update(SCREEN)

        if handle_events([back_button], mouse_pos) is not None:
            return

        pygame.display.update()
                
def play():
    selected_category = None
    selected_difficulty = None

    while True:
        mouse_pos = pygame.mouse.get_pos()
        SCREEN.fill("black")

        if selected_category is None:
            draw_text("Choose Category:", get_font, 65, "White", (SCREEN_WIDTH // 2, 100))

            categories = ["Science", "History", "English", "Filipino"]
            category_buttons = [Button(image=None, pos=(640, 250 + i * 70),
                                       text_input=category, font=get_font(40), base_color="White", hovering_color="Green")
                                for i, category in enumerate(categories)]

            draw_buttons(category_buttons, mouse_pos)

            back_button = Button(image=None, pos=(640, 620),
                                 text_input="Back", font=get_font(50), base_color="White", hovering_color="Green")
            back_button.changeColor(mouse_pos)
            back_button.update(SCREEN)

            selected_index = handle_events(category_buttons + [back_button], mouse_pos)

            if selected_index is not None:
                if selected_index < len(categories):
                    selected_category = categories[selected_index]
                    print(f"Selected Category: {selected_category}")
                else:
                    return
        else:
            draw_text("Choose Difficulty:", get_font, 65, "White", (SCREEN_WIDTH // 2, 100))

            difficulties = ["Easy", "Normal", "Hard"]
            difficulty_buttons = [Button(image=None, pos=(640, 250 + i * 70),
                                         text_input=difficulty, font=get_font(40), base_color="White", hovering_color="Green")
                                  for i, difficulty in enumerate(difficulties)]

            draw_buttons(difficulty_buttons, mouse_pos)

            back_button = Button(image=None, pos=(640, 620),
                                 text_input="Back", font=get_font(50), base_color="White", hovering_color="Green")
            back_button.changeColor(mouse_pos)
            back_button.update(SCREEN)

            selected_index = handle_events(difficulty_buttons + [back_button], mouse_pos)

            if selected_index is not None:
                if selected_index < len(difficulties):
                    selected_difficulty = difficulties[selected_index]
                    print(f"Selected Difficulty: {selected_difficulty}")
                    start_quiz(selected_category, selected_difficulty)
                else:
                    selected_category = None

        pygame.display.update()

def info():
    while True:
        mouse_pos = pygame.mouse.get_pos()
        SCREEN.fill("black")

        draw_text("Credits:", get_credits_font, 75, "White", (SCREEN_WIDTH // 2, 180))

        team_members = ["Miguel Timothy Cabrera", "Kurt Luis Tabaranza", "Carlos Miguel Reopirio", "Gabriel Frost Jandoquele"]
        for i, member in enumerate(team_members):
            draw_text(member, get_credits_font, 50, "White", (SCREEN_WIDTH // 2, 260 + i * 60))

        info_back_button = Button(image=None, pos=(640, 650),
                                  text_input="BACK", font=get_font(50), base_color="White", hovering_color="Green")

        info_back_button.changeColor(mouse_pos)
        info_back_button.update(SCREEN)

        if handle_events([info_back_button], mouse_pos) is not None:
            return

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        draw_text("QUIZ GAME", get_font, 100, "#b68f40", (SCREEN_WIDTH // 2, 100))

        play_button = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        info_button = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 400),
                             text_input="INFO", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        quit_button = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        draw_buttons([play_button, info_button, quit_button], mouse_pos)

        buttons = [play_button, info_button, quit_button]
        selected_index = handle_events(buttons, mouse_pos)

        if selected_index == 0:
            play()
        elif selected_index == 1:
            info()
        elif selected_index == 2:
            pygame.quit()
            sys.exit()

        pygame.display.update()

main_menu()
