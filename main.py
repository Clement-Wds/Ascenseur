def main():
    print('---ASCENSEUR---')
    print('1 : MONTER')
    print('2 : DESCENDRE')
    choice = input()
    if choice == 1:
        goUp()
    elif choice == 2:
        goDown()
    else: 
        print('Veuillez entrez une valeur valide')



def goUp():
    print('l\'ascenseur monte')

def goDown():
    print('l\'ascenseur descend')

main()
goUp()