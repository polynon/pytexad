from display.display import displaylayout

vertical_basic = displaylayout(option_prefix=lambda screen,i,*args: f"({i+1})",screen_prefix=lambda screen,*args: f"{screen.title}\n")