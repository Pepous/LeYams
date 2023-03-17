from random import randint
class Des():
    def __init__(self):
        self.liste_des = [0 for i in range(5)]
    def lancer(self):
        self.liste_des = [randint(1,6) for i in range(5)]
        return self.liste_des
    