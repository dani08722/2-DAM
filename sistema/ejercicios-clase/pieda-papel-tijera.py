
p1wins=0
p2wins=0
print("-----------------------------------------------")
print("Bienvenido al piedra, papel o tijera")
print("-----------------------------------------------\n\n")
while p1wins < 3 and p2wins < 3:

    person1=input("Jugador 1, elige [1] piedra, [2] papel o [3] tijera: ")
    person2=input("Jugador 2, elige [1] piedra, [2] papel o [3] tijera: ")
    match person1:
        case "1":
            match person2:
                case "1":
                    print("Empate")
                case "2":
                    print("Gana jugador 2")
                    p2wins += 1
                case "3":
                    print("Gana jugador 1")
                    p1wins += 1
        case "2":
            match person2:
                case "1":
                    print("Gana jugador 1")
                    p1wins += 1
                case "2":
                    print("Empate")
                case "3":
                    print("Gana jugador 2")
                    p2wins += 1
        case "3":
            match person2:
                case "1":
                    print("Gana jugador 2")
                    p2wins += 1
                case "2":
                    print("Gana jugador 1")
                    p1wins += 1
                case "3":
                    print("Empate")