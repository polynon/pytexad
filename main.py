from screen import *
from input import *
from save import load, save
import commands

test_screen = screen((option("test one"),
option("test two",help="this is a 2",valid_actions=['h']),
option("test two",help="this is a 3",valid_actions=['h']),
option("test two",help="this is a 4",valid_actions=['h']),
option("test two",help="this is a 5",valid_actions=['h']),
option("test two",help="this is a 6",valid_actions=['h']),
option("test two",help="this is a 7",valid_actions=['h']),
option("test two",help="this is a 8",valid_actions=['h']),
option("test two",help="this is a 9",valid_actions=['h']),
option("test two",help="this is a 10",valid_actions=['h']),
option("test two",help="this is the end aka 11",valid_actions=['h'])
))

print("\033c",end="")
test_screen.test = ""
infodisplay:str = ""
while True:
    print(f"\033c{test_screen.get_display()}{infodisplay}",end="\n")
    action = betterinput(options=test_screen.options)
    infodisplay = ""
    
    if action:
        if action.type == "command":
            match action.form:
                case 'q':
                    commands.quit()
                case 'l':
                    obj = load("saves/test")
                    if obj:
                        test_screen = obj
                        print(test_screen.test)
                    input()
                case 's':
                    save(test_screen,"saves/test")
                case 'w':
                    test_screen.test = input()

        elif action.type == "action" and action.form == "h":
            infodisplay = "\n"+test_screen.options[action.place].help