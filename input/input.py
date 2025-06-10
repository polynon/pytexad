from screen.screen import option
from input.commands import valid_commands
from input.initiators import initiators

class action():
   def __init__(self,id,form,type,args):
        self.type = type
        self.form = form
        self.id = id
        self.args = args

def better_input(options):
    raw_input = input()
    args = raw_input.split(" ")
    if len(raw_input) < 1:
        return None
    for initiator in initiators:
        initiator = initiator.check(args[0],options)
        if not initiator:
            continue
        if initiator.form not in initiator.valid_forms:
            return None
        return action(id=initiator.id,form=initiator.form,type=initiator.type,args=args[1::])
        
