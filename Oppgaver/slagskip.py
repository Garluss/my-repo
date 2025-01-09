#Creates grid 1
grid1 = []
for row in range(100):
    grid1.append("-")

grid1shots = []
for row in range(100):
    grid1shots.append("-")

#Creates grid 2
grid2 = []
for row in range(100):
    grid2.append("-")

grid2shots = []
for row in range(100):
    grid2shots.append("-")

#Resets all spaces on the grid
def reset(grid: str):
    grid.clear()
    for i in range(100):
        grid.append("-")

#Draws the grid of player n. 1
def drawGrid(grid: str):
    y = 0
    print(" ", end=" ")
    for i in range(10):
        print(i, end=" ")
    for i in range(len(grid)):
        if i%10 == 0:
            print("")
            print(y, end=" ")
            print(grid[i], end=" ")
            y += 1
        else:
            print(grid[i], end=" ")
    print("")
    print("")

#Plot uses its own testing to check if the space is viable, 
# ignores the state of the space and places anyways if it is on the grid
def plot(grid: str, x: int, y: int, char: str) -> bool:
    try:
        if int(y) == 0:
            pos = str(x)
        elif int(y) < 0:
            return False
        else:
            pos = str(y) + str(x)
        grid[int(pos)] = str(char)
    except IndexError:
        return False
    except ValueError:
        return False

#Tests if the space is empty and on the grid, returns False if not
def test(grid:str, x:int, y:int) -> bool:
    try:
        pos = str(y) + str(x)
        if int(y) < 0 or int(y) > 9:
            return False
        elif int(x) < 0 or int(x) > 9:
            return False
        elif grid[int(pos)] != "-":
            return False
        else:
            return True
    except IndexError:
        return False
    except ValueError:
        return False

#Plots a ship from a list of different types
def plotShip(grid: str, type: int, x: int, y: int, rot:int):
    if type == 2:
        match rot:
            case 0: shape = [[x,y],[x,y+1]]
            case 90: shape = [[x,y],[x+1,y]]
            case 180: shape = [[x,y],[x,y-1]]
            case 270: shape =[[x,y],[x-1,y]]
            case _: 
                print("Not valid rotation. Try 0, 90, 180, or 270.")
                return False
    elif type == 3:
        match rot:
            case 0: shape = [[x,y],[x,y+1],[x,y+2]]
            case 90: shape = [[x,y],[x+1,y],[x+2,y]]
            case 180: shape = [[x,y],[x,y-1],[x,y-2]]
            case 270: shape =[[x,y],[x-1,y],[x-2,y]]
            case _: 
                print("Not valid rotation. Try 0, 90, 180, or 270.")
                return False
    elif type == 4:
        match rot:
            case 0: shape = [[x,y],[x,y+1],[x,y+2],[x,y+3]]
            case 90: shape = [[x,y],[x+1,y],[x+2,y],[x+3,y]]
            case 180: shape = [[x,y],[x,y-1],[x,y-2],[x,y-3]]
            case 270: shape =[[x,y],[x-1,y],[x-2,y],[x-3,y]]
            case _: 
                print("Not valid rotation. Try 0, 90, 180, or 270.")
                return False
    elif type == 5:
        match rot:
            case 0: shape = [[x,y],[x,y+1],[x,y+2],[x,y+3],[x+1,y+3]]
            case 90: shape = [[x,y],[x+1,y],[x+2,y],[x+3,y],[x+3,y-1]]
            case 180: shape = [[x,y],[x,y-1],[x,y-2],[x,y-3],[x-1,y-3]]
            case 270: shape =[[x,y],[x-1,y],[x-2,y],[x-3,y],[x-3,y+1]]
            case _: 
                print("Not valid rotation. Try 0, 90, 180, or 270.")
                return False
    for i in shape:
        if test(grid,i[0],i[1]) == False:
            print("Not valid placement.")
            return False
    for i in shape:
        plot(grid,i[0],i[1],"O")


#Checks if there is a ship on the square, could implement this into the 'test'-function
def checkShip(grid: str, x: int, y: int):
    if int(y) == 0:
        pos = str(x)
    else:
        pos = str(y) + str(x)
    if grid[int(pos)] == "O":
        return True
    elif grid[int(pos)] == "-":
        return "Empty"
    else:
        return False

def placeShip(grid: str, type: int):
    while True:
        print(f"Place ship with length {type}.")
        x = int(input("X Co-ordinate: "))
        y = int(input("Y Co-ordinate: "))
        rot = int(input("Ship rotation: "))
        if plotShip(grid,type,x,y,rot) != False:
            break

print("Place ships, player 1.")
placeShip(grid1,2)
drawGrid(grid1)
for i in range(2):
    placeShip(grid1,3)
    drawGrid(grid1)
placeShip(grid1,4)
drawGrid(grid1)
placeShip(grid1,5)
drawGrid(grid1)

print("Place ships, player 2.")
placeShip(grid2,2)
drawGrid(grid2)
for i in range(2):
    placeShip(grid2,3)
    drawGrid(grid2)
placeShip(grid2,4)
drawGrid(grid2)
placeShip(grid2,5)
drawGrid(grid2)

def playerTurn(grid: str, gridshots: str): #Affected grid
    print("Previous shots:")
    drawGrid(gridshots)
    x = int(input("X Co-ordinate to shoot: "))
    y = int(input("Y Co-ordinate to shoot: "))
    result = checkShip(grid, x, y)
    if result == True:
        plot(grid,x,y,"X")
        plot(gridshots,x,y,"X")
    elif result == "Empty":
        plot(grid,x,y,"/")
        plot(gridshots,x,y,"/")
    drawGrid(gridshots)

grid2Ships = 0
grid1Ships = 0
gameContinue = True
while gameContinue == True:
    player1 = 1
    player2 = 0
    if player1 == 1:
        print("Your turn to shoot, player 1")
        playerTurn(grid2,grid2shots)
        player1 = 0
        player2 = 1
    elif player2 == 0:
        print("Your turn to shoot, player 2")
        playerTurn(grid1,grid1shots)
        player1 = 1
        player2 = 0
    else:
        print("Error")
        exit()
    for i in grid1:
        if grid1[int(i)] == "O":
            grid1Ships += 1
    for i in grid2:
        if grid2[int(i)] == "O":
            grid2Ships += 1
    if grid1Ships == 0:
        print("Player 2 victory")
        gameContinue = False
    elif grid2Ships == 0:
        print("Player 1 victory")
        gameContinue = False
    else:
        print("No victor")
        gameContinue = False


    
        

