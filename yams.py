from tableau import Tableau
from des import Des

tableau = Tableau()
des = Des()

while(1):
    print("Lancer de dés")
    lancer = des.lancer()
    print("Lancer obtenu",lancer)
    nbLancers = 0
    continuer = '1'
    while(nbLancers<2 and continuer=='1'):
        continuer = input("Souhaite tu relancer ? 0/1")
        if(continuer == '1'):
            lancer = des.lancer()
            print("Lancer obtenu",lancer)
            nbLancers += 1
    tableau.afficherTableau()
    
    possible = False
    while(possible == False):
        possibilite = input("### Que choisis-tu ? colonne = {0,1,2}, combinaison ={1,2,...,brelan,...,chance} ###")
        if(',' in possibilite):
            colonne, combinaison = possibilite.split(',')
            possible = tableau.choixPossibilites(combinaison, int(colonne))
            if(possible):
                print("Bien !")
                calculPossibilites = tableau.possibilites(lancer)
                tableau.choisirPossibilite(calculPossibilites, combinaison, int(colonne))
                tableau.afficherTableau()
            else:
                print("Impossible de choisi ça !")
        else:
            "Erreur saisie !"
            possible = False
    
