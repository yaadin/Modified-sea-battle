import random



def print_Zone(Zone):
    for row in Zone:
        print(" ".join(row))

def Neigh_bool(Zone, x, y):
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if 0 <= i < len(Zone) and 0 <= j < len(Zone[0]) and (Zone[i][j] == '1' or Zone[i][j] == '2' or Zone[i][j] == '3'):
                return True
    return False

def Location_bool(Zone, ship, coordinates):
    for x, y in coordinates:
        if (
            x < 0
            or x >= len(Zone)
            or y < 0
            or y >= len(Zone[0])
            or Zone[x][y] == '1'
            or Zone[x][y] == '2'
            or Zone[x][y] == '3'
            or Neigh_bool(Zone, x, y)
        ):
            return False
    return True

def place_ship(Zone, ship_size):
    while True:
        direction = random.choice(['horizontal', 'vertical'])
        if direction == 'horizontal':
            x = random.randint(0, len(Zone) - 1)
            y = random.randint(0, len(Zone[0]) - ship_size)
            coordinates = [(x, y+i) for i in range(ship_size)]
        else:
            x = random.randint(0, len(Zone) - ship_size)
            y = random.randint(0, len(Zone[0]) - 1)
            coordinates = [(x+i, y) for i in range(ship_size)]
        if Location_bool(Zone, ship_size, coordinates):
            for i, j in coordinates:
                if ship_size == 1:
                    Zone[i][j] = '1'
                elif ship_size == 2:
                    Zone[i][j] = '2'
                elif ship_size == 3:
                    Zone[i][j] = '3'
            break


def place_ships(Zone):
    place_ship(Zone, 3)
    place_ship(Zone, 2)
    place_ship(Zone, 2)
    for _ in range(4):
        place_ship(Zone, 1)


def create_Zone(Row, Column):
    return [['0' for _ in range(Column)] for _ in range(Row)]

def play(Zone):
    game = True
    ones = 4
    threes = 3
    twos = 4
    while game:
        x = input("write row and column you'd like to check(e.g. 22): ")
        x = list(x)
        x[0] = str(int(x[0]) - 1)
        x[1] = str(int(x[1]) - 1)
        if x == "x":
            break
        if int(x[0]) > 6 or int(x[1]) > 6:
            print("you canoot shoot outside 7x7")
        else:
            print(Zone[int(x[0])][int(x[1])])
            if Zone[int(x[0])][int(x[1])] == "0":
                print("there is no ship")
            elif Zone[int(x[0])][int(x[1])] == "1":
                print("hit and sank")
                Zone[int(x[0])][int(x[1])] = "0"
                ones -= 1
            elif Zone[int(x[0])][int(x[1])] == '3':
                Zone[int(x[0])][int(x[1])] = '0'
                threes -= 1
                if threes == 0:
                    print("hit and sank")
                else:
                    print("hit")
            elif Zone[int(x[0])][int(x[1])] =='2':
                Zone[int(x[0])][int(x[1])] = '0'
                twos -= 1
                if twos == 0:
                    print("hit and sank")
                else:
                    print("hit")
            if ones == 0 and threes == 0 and twos == 0:
                print("You've won!")
                game = False

 
def main():
    Row, Column = 7, 7 
    Zone = create_Zone(Row, Column)
    place_ships(Zone)
    print_Zone(Zone)
    play(Zone)

main()