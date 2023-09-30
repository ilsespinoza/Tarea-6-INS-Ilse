a = input("Enter cells: ")
lista = list(a)

def matrix():
    p = 9 * "-"
    print(p)
    print("|", lista[0], lista[1], lista[2], "|")
    print("|", lista[3], lista[4], lista[5], "|")
    print("|", lista[6], lista[7], lista[8], "|")
    print(p)

matrix()

def who_wins():
    
    while True:
        
        if lista[0] == lista[1] == lista[2] != " " and not lista[3] == lista[4] == lista[5] and not lista[6] == lista[7] == lista[8]:
            print(lista[0], "wins")
            break
        elif lista[3] == lista[4] == lista[5] != " " and not lista[0] == lista[1] == lista[2] and not lista[6] == lista[7] == lista[8]:
            print(lista[3], "wins")
            break
        elif lista[6] == lista[7] == lista[8] != " " and not lista[0] == lista[1] == lista[2] and not lista[3] == lista[4] == lista[5]:
            print(lista[6], "wins")
            break