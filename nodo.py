
class Nodo:

    def __init__(self, id:int, name:str=None):

        self.id = id
        self.name = name
        if self.name == None:
            self.name = f"Nodo_{id}"