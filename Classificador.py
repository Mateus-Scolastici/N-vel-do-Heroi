def Classificador():
    name = input("Digite o nome do herói: ")
    xp = int(input("Digite a quantidade de experiência do herói (ex: 1000): "))
    

    if (xp <= 1000):
        lvl = "Ferro"
    elif (xp <= 2000):
        lvl = "Bronze"
    elif (xp <= 5000):
        lvl = "Prata"
    elif (xp <= 7000):
        lvl = "Ouro"
    elif (xp <= 8000):
        lvl = "Platina"
    elif (xp <= 9000):
        lvl = "Ascendente"
    elif (xp <= 10000):
        lvl = "Imortal"
    else:
        lvl = "Radiante"
    
    print(f"O Heroi de nome {name} esta no nivel {lvl}")

if __name__ == '__main__':
    Classificador()
