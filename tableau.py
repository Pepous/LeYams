class Tableau():
    def __init__(self) -> None:
        self.combinaisons = ["1","2","3","4","5","6","brelan","carree","full","petite suite","grande suite","yams","chance"]

        self.colonne_g = {key:0 for key in self.combinaisons}
        self.colonne_c = {key:0 for key in self.combinaisons}
        self.colonne_d = {key:0 for key in self.combinaisons}

        self.droit_g = [[key,False] for key in self.colonne_g.keys()]
        self.droit_g[0][1] = True
        self.droit_c = [[key,True] for key in self.colonne_g.keys()]
        self.droit_d = [[key,False] for key in self.colonne_g.keys()]
        self.droit_d[-1][1] = True

    def possibilites(self,lancer):
        chiffres_presents = list(set(lancer))
        possibilites = {key:0 for key in self.combinaisons}
        for chiffre in chiffres_presents:
            possibilites[str(chiffre)] = lancer.count(chiffre)*chiffre
            if(lancer.count(chiffre)>=3):
                possibilites["brelan"] = 3*chiffre
                if(lancer.count(chiffre)>=4):
                    possibilites["carree"] = 4*chiffre
                    if(lancer.count(chiffre)==5):
                        possibilites["yams"] = 50
        if(len(chiffres_presents)>=4):
            possibilites["petite suite"] = 30
            if(len(chiffres_presents)==5):
                possibilites["grande suite"] = 40
        if(len(chiffres_presents)==2 & (lancer.count(chiffres_presents[0])==2 or lancer.count(chiffres_presents[0])==3)):
            possibilites["full"] = 25
        possibilites["chance"] = sum(lancer)
        return possibilites

    def choisirPossibilite(self, possibilites, combinaison, colonne):
        if(colonne == 0):
            self.colonne_g[combinaison] = possibilites[combinaison]
        elif(colonne == 1):
            self.colonne_c[combinaison] = possibilites[combinaison]
        else:
            self.colonne_d[combinaison] = possibilites[combinaison]
    def afficherTableau(self):
        for key in self.colonne_g.keys():
            print(key+(12-len(key))*" ", self.colonne_g[key], self.colonne_c[key], self.colonne_d[key])

    def choixPossibilites(self,possibilite,colonne):
        droit = self.droit_g
        if(colonne == 0):
            droit = self.droit_g
        elif(colonne == 1):
            droit = self.droit_c
        else:
            droit = self.droit_d
        index = self.combinaisons.index(possibilite)
        return droit[index][1]
    
    

