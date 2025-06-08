class initiator():
    def __init__(self,check=lambda *args:None,id=-1,valid_forms=[],form="",type=""):
        self.check = check
        self.id = id
        self.valid_forms = valid_forms
        self.form = form
        self.type = type