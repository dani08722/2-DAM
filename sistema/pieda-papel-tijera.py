person1=input("Jugador 1, elige piedra, papel o tijera: ")
person2=input("Jugador 2, elige piedra, papel o tijera: ")
p1wins=0
p2wins=0

while p1wins < 3 and p2wins < 3:
    match person1:
        case "piedra":
            match person2:
                case "piedra":
                    print("Empate")
                case "papel":
                    print("Gana jugador 2")
                    p2wins += 1
                case "tijera":
                    print("Gana jugador 1")
                    p1wins += 1
        case "papel":
            match person2:
                case "piedra":
                    print("Gana jugador 1")
                    p1wins += 1
                case "papel":
                    print("Empate")
                case "tijera":
                    print("Gana jugador 2")
                    p2wins += 1
        case "tijera":
            match person2:
                case "piedra":
                    print("Gana jugador 2")
                    p2wins += 1
                case "papel":
                    print("Gana jugador 1")
                    p1wins += 1
                case "tijera":
                    print("Empate")