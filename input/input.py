from screen.screen import option
from input.commands import valid_commands
from input.initiators import initiators

class action():
   def __init__(self,id,form,type):
        self.type = type
        self.form = form
        self.id = id

def better_input(options):
    raw_input = input()
    if len(raw_input) < 1:
        return None
    for initiator in initiators:
        initiator = initiator.check(raw_input,options)
        if not initiator:
            continue
        if initiator.form not in initiator.valid_forms:
            return None
        return action(id=initiator.id,form=initiator.form,type=initiator.type)
        
