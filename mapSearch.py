import turtle
import time
import random
long = 25
width = 25
size = 30
pensize=16
themap = [([0] * long) for i in range(width)]
L = []
Stack=[]
Data = [([0] * long) for i in range(max(long,width))]
star=0
def DeepSearch(coordx,coordy,end):
    stop=1
    if (coordx+1==long-1) and (coordy)==end:
        return
    else:
        for d in [1,2,3,4]:
            if d==1:
                if (themap[coordx-1][coordy]==3) and (Data[coordx-1][coordy]!=1):
                    Data[coordx-1][coordy]=1
                    Stack.append((coordx-1,coordy))
                    stop=0
                    DeepSearch(coordx-1,coordy,end)
            if d==2:
                if (themap[coordx+1][coordy]==3) and (Data[coordx+1][coordy]!=1):
                    Data[coordx+1][coordy]=1
                    Stack.append((coordx+1,coordy))
                    stop=0
                    DeepSearch(coordx+1,coordy,end)
            if d==3:
                if( themap[coordx][coordy-1]==3) and (Data[coordx][coordy-1]!=1):
                    Data[coordx][coordy-1]=1
                    Stack.append((coordx,coordy-1))
                    stop=0
                    DeepSearch(coordx,coordy-1,end)
            if d==4:
                if (themap[coordx][coordy+1]==3) and (Data[coordx][coordy+1]!=1):
                    Data[coordx][coordy+1]=1
                    Stack.append((coordx,coordy+1))
                    stop=0
                    DeepSearch(coordx,coordy+1,end)
        if stop==1:
            del Stack[-1]
            coordx=Stack[-1][0]
            coordy=Stack[-1][1]
            DeepSearch(coordx,coordy,end)
def main():
    for x in range(long):
        for y in range(width):
            if (x % 2 == 1) and (y % 2 == 1):
                themap[x][y] = 1
            else:
                themap[x][y] = 0
    starx = random.choice([1, long - 2])
    while 1:
        stary = random.randint(2, width - 3)
        if themap[starx][stary] == 0:
            break
    L.append((starx, stary + 1))
    L.append((starx, stary - 1))
    themap[starx][stary] = 3
    themap[starx][stary + 1] = 3
    themap[starx][stary - 1] = 3
    stary += 1
    isstop = 0
    while (1):
        ismax = 1
        for y in range(long):
            for u in range(width):
                if themap[y][u] == 1:
                    ismax = 0
                    break
            if ismax == 0:
                break
        if ismax == 1:
            break
        if starx == 1:
            if stary == 1:
                if (themap[starx + 2][stary] != 1) and (themap[starx][stary + 2]) != 1:
                    isstop = 1
            elif stary == width - 2:
                if (themap[starx + 2][stary]) != 1 and (themap[starx][stary - 2]) != 1:
                    isstop = 1
            else:
                if (themap[starx + 2][stary]) != 1 and (themap[starx][stary + 2]) != 1 and (
                themap[starx][stary - 2]) != 1:
                    isstop = 1
        elif starx == long - 2:
            if stary == 1:
                if (themap[starx - 2][stary]) != 1 and (themap[starx][stary + 2]) != 1:
                    isstop = 1
            elif stary == width - 2:
                if (themap[starx - 2][stary]) != 1 and (themap[starx][stary - 2]) != 1:
                    isstop = 1
            else:
                if (themap[starx - 2][stary]) != 1 and (themap[starx][stary + 2]) != 1 and (
                themap[starx][stary - 2]) != 1:
                    isstop = 1
        elif stary == 1:
            if (themap[starx - 2][stary]) != 1 and (themap[starx][stary + 2]) != 1 and (themap[starx + 2][stary]) != 1:
                isstop = 1
        elif stary == width - 2:
            if (themap[starx - 2][stary]) != 1 and (themap[starx][stary - 2]) != 1 and (themap[starx + 2][stary]) != 1:
                isstop = 1
        else:
            if (themap[starx - 2][stary]) != 1 and (themap[starx + 2][stary]) != 1 and (
            themap[starx][stary + 2]) != 1 and (themap[starx][stary - 2]) != 1:
                isstop = 1
        if isstop == 1:
            del L[-1]
            starx = L[-1][0]
            stary = L[-1][1]
            isstop = 0
        direction = random.choice(["up", "down", "left", "right"])
        if direction == "up":
            if starx == 1:
                pass
            elif themap[starx - 2][stary] == 3:
                pass
            else:
                themap[starx - 2][stary] = 3
                themap[starx - 1][stary] = 3
                starx = starx - 2
                L.append((starx, stary))
        elif direction == "down":
            if starx == long - 2:
                pass
            elif themap[starx + 2][stary] == 3:
                pass
            else:
                themap[starx + 2][stary] = 3
                themap[starx + 1][stary] = 3
                starx = starx + 2
                L.append((starx, stary))
        elif direction == "left":
            if stary == 1:
                pass
            elif themap[starx][stary - 2] == 3:
                pass
            else:
                themap[starx][stary - 2] = 3
                themap[starx][stary - 1] = 3
                stary = stary - 2
                L.append((starx, stary))
        elif direction == "right":
            if stary == width - 2:
                pass
            elif themap[starx][stary + 2] == 3:
                pass
            else:
                themap[starx][stary + 2] = 3
                themap[starx][stary + 1] = 3
                stary = stary + 2
                L.append((starx, stary))
    turtle.setup(long * size, width * size, 0, 0)
    turtle.speed(100)
    turtle.hideturtle()
    turtle.pencolor('red')
    for i in range(width):
        for j in range(long):
            turtle.penup()
            turtle.goto(j * size - long * size / 2, width * size / 2 - i * size)
            if themap[i][j] == 0:
                turtle.pendown()
                turtle.fillcolor('black')
                turtle.begin_fill()
                for k in range(4):
                    turtle.forward(size)
                    turtle.right(90)
                turtle.end_fill()
            else:
                turtle.pendown()
                turtle.fillcolor('white')
                turtle.begin_fill()
                for k in range(4):
                    turtle.forward(size)
                    turtle.right(90)
                turtle.end_fill()
    while 1:
        star = random.randint(2, long - 3)
        end = random.randint(2, width - 3)
        if (themap[1][star]==3) and (themap[width-2][end]==3):
            break
    turtle.penup()
    turtle.goto(end * size - long * size / 2, width * size / 2 - (long-1) * size)
    turtle.fillcolor('yellow')
    turtle.begin_fill()
    turtle.pendown()
    turtle.begin_fill()
    for k in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(star * size - long * size / 2, width * size / 2 - 0 * size)
    turtle.pendown()
    turtle.begin_fill()
    for k in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()
    Stack.append((1,star))
    Data[1][star]=1
    coordx=1
    coordy=star
    DeepSearch(coordx,coordy,end)
    turtle.speed(1)
    turtle.penup()
    turtle.pencolor('blue')
    turtle.showturtle()
    turtle.pensize(pensize)
    turtle.goto(star * size - long * size / 2, width * size / 2 - 0 * size-size-size/2)
    turtle.pendown()
    while Stack!=[]:
        turtle.goto(Stack[0][1] * size - long * size / 2+size/2, width * size / 2 - Stack[0][0] * size-size/2)
        del Stack[0]
    time.sleep(30)
main()
