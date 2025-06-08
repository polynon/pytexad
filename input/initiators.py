import re
from input.initiator import initiator

def select_check(raw_input,options):
    regexed = re.search("^[0-9]+",raw_input)
    if not regexed:
        return None
    id = int(regexed.group()) -1
    if (id < 0) or (id > len(options) -1):
        return None
    return initiator(id=id,valid_forms=options[id].valid_actions,form=raw_input[id+1::],type="action")

from input.commands import valid_commands
def command_check(raw_input,*args):
    if raw_input[0] != ':':
        return None
    return initiator(type='command',form=raw_input[1::],valid_forms=valid_commands)

initiators = [
    initiator(check=select_check),
    initiator(check=command_check)
    ]
        