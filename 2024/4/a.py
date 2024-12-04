def read_input(file="input.txt"):
    ret = []
    with open(file,"r") as f:
        for line in f:
            ret.append(line)
    return ret


def search_one(panel,yx,dir,to_search = "XMAS"):

    for idx,char in enumerate(to_search):
        if yx[0]<0 or yx[0]>= len(panel):
            return False
        if yx[1]<0 or yx[1]>= len(panel[yx[0]]):
            return False
        if panel[yx[0]][yx[1]] == char:
            yx = (yx[0]+dir[0], yx[1]+dir[1])
            continue
        return False
    return True

def search_x(panel, yx):
    if not panel[yx[0]][yx[1]]  == 'A':
        return False
    if yx[0]==0 or yx[1] == 0 or yx[0]== len(panel)-1 or yx[1] == len(panel[yx[0]])-1:
        return False
    if not search_one(panel, (yx[0]-1,yx[1]-1), (1,1), "MAS") and not search_one(panel, (yx[0]-1,yx[1]-1), (1,1), "SAM"):
        return False
    if not search_one(panel, (yx[0]-1,yx[1]+1), (1,-1), "MAS") and not search_one(panel, (yx[0]-1,yx[1]+1), (1,-1), "SAM"):
        return False
    return True


def part1():
    input = read_input()
    sum = 0
    for y in range(len(input)):
        for x in range(len(input[y])):
            for dir in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]:
                if search_one(input, (y,x), dir):
                    sum = sum + 1
    print(sum)



part1()

def part2():
    input = read_input("input.txt")
    sum = 0
    for y in range(len(input)):
        for x in range(len(input[y])):
            if search_x(input,(y,x)):
                sum = sum + 1
    print(sum)

part2()



