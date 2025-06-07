class validaction():
    def __init__(self,go_to_where):
        self.go_to_where = go_to_where

class option():
    def __init__(self,display:str,valid_actions = {}):
        self.display = display
        self.valid_actions = valid_actions

class screen():
    def __init__(self,options:option = [],title = ""):
        self.options = options
        self.title = title