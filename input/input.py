from screen.screen import option
from input.commands import valid_commands
from re import search
import re

class action():
   def __init__(self,place,form,type):
        self.type = type
        self.form = form
        self.place = place

def correct_command(command):
    if command in valid_commands:
        return action(type="command",form=command,place=-1)
    else:
        return None

def is_valid_selection(options,num) -> bool:
    if num < 0:
        return False
    if num > len(options) -1:
        return False
    return True

def correct_action(options,raw_input,regexe_group):
    id = int(regexe_group)-1
    if is_valid_selection(options,id):
        if raw_input[len(regexe_group)::] in options[id].valid_actions:
            return action(place=id,form=raw_input[len(regexe_group)::],type="action")
    return None

def betterinput(options):
    raw_input = input()
    regexed = search("^[0-9]+",raw_input)
    if len(raw_input) < 2:
        return None
    elif regexed:
        return correct_action(options=options,raw_input=raw_input,regexe_group=regexed.group())
    elif raw_input[0] == ":":
        return correct_command(raw_input[1::])
    else:
        return None