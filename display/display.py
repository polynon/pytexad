from screen.screen import screen
from screen.screen import option

blankL = lambda *args:""

class displaylayout():
    def __init__(self,row_length=1,clear_display=True,option_afix=blankL,option_prefix=blankL,screen_afix=blankL,screen_prefix=blankL):
        self.row_length:int = row_length
        self.clear_display:bool = clear_display
        self.option_afix:callable = option_afix
        self.option_prefix:callable = option_prefix
        self.screen_afix:callable = screen_afix
        self.screen_prefix:callable = screen_prefix

def display(display_layout:displaylayout,screen:screen,*args) -> str:
    display_text = ""
    if display_layout.clear_display == True:
        display_text += "\033c"
    display_text += display_layout.screen_prefix(screen,args)

    for i,option in enumerate(screen.options):
        display_text += display_layout.option_prefix(screen,i,option,args) +option.display +display_layout.option_afix(screen,i,option,args)
        if i+1 == len(screen.options):
            break
        if (i+1)%display_layout.row_length == 0:
            display_text += '\n'

    display_text += display_layout.screen_afix(screen,args)
    return display_text