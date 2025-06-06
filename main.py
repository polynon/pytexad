from input import *
from save import load, save
import commands
import screens
from screen import validaction

current_screen = screens.test_room_one

def try_change_screen(valid_action:validaction):
    global current_screen 
    current_screen = valid_action.go_to_where

while True:
    print(f"\033c{current_screen.title}{current_screen.get_display()}")
    action = betterinput(current_screen.options)
    if not action:
        continue
    if action.type == "command":
        match action.form:
            case 'q':
                commands.quit()
    if action.type == "action":
        match action.form:
            case 'goto':
                try_change_screen(current_screen.options[action.place].valid_actions[action.form])