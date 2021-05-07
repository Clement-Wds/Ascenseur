#Classe Ascenseur
class Ascenseur:
    #Commande GoUp
    def goUp(self):
        print("\nl'Ascensseur Monte\n")

    #Commande GoDown
    def goDown(self):
        print("\nl'Ascensseur descend\n")

choice = 0

#Création objet Ascenseur Nord
ascenseurNord = Ascenseur()

while choice != "3":
    print('---ASCENSEUR---')
    print('1 : MONTER')
    print('2 : DESCENDRE')
    print('3 : Arrêter le programme')
    choice = input()

    if choice == "1":
        ascenseurNord.goUp()

    if choice == "2":
        ascenseurNord.goDown()

    if choice == "3":
        print('\nFIN DU PROGRAMME')