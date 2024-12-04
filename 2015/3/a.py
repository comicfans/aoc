dir = {
    '<':(-1,0),
    '>':(1,0),
    '^':(0,1),
    'v':(0,-1)
}




def walk(pos,c,visit):
    this_dir = dir[c]
    pos = (pos[0]+this_dir[0],pos[1]+this_dir[1])
    visit.add(pos)
    return pos

def part1():
    pos = (0,0)
    visit = set([pos])
    with open('input.txt','r') as f:
        for line in f:
            for c in line.strip():
                pos = walk(pos, c, visit)

    print(len(visit))


part1()
           

def part2():
    pos01 = [(0,0),(0,0)]
    idx = 0
    visit = set([pos01[0]])
    with open('input.txt','r') as f:
        for line in f:
            for c in line.strip():
                pos01[idx] = walk(pos01[idx], c, visit)
                idx = 1 - idx

    print(len(visit))

part2()


