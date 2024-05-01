def parse_input(lines):
    first_line = lines[0].strip()
    from_left_right = {}
    for line in lines[2:]:
        l = line.strip()
        if l.strip() == "":
            continue
        fromv = l.split(" ")[0]
        left = l.split('(')[1].split(',')[0]
        right = l.split(',')[1].strip().split(')')[0]
        from_left_right[fromv] = (left, right)

    return (first_line,from_left_right)

example = ["LLR",
"",
"AAA = (BBB, BBB)",
"BBB = (AAA, ZZZ)",
"ZZZ = (ZZZ, ZZZ)"]

def test1():
    lines = None
    with open('input.txt') as f:
        lines = f.readlines()
    parsed = parse_input(lines)

    dir = parsed[0]
    path = parsed[1]

    step = 0
    current = 'AAA'


    while True:

        if current == 'ZZZ':
            break

        idx = 0 if dir[step  %  len(dir)] == 'L' else 1

        key = (current,idx,step % len(dir))
        print(key)
        walked.add(key)

        current = path[current][idx]
        step = step + 1
        prev_select = idx

    print(step)

#test1()

def walk_az(dir,path,current):
    step = 0

    while True:

        if current.endswith('Z'):
            break

        idx = 0 if dir[step  %  len(dir)] == 'L' else 1


        current = path[current][idx]
        step = step + 1
        prev_select = idx

    return step


example2 = [
"LR",
"",
"11A = (11B, XXX)",
"11B = (XXX, 11Z)",
"11Z = (11B, XXX)",
"22A = (22B, XXX)",
"22B = (22C, 22C)",
"22C = (22Z, 22Z)",
"22Z = (22B, 22B)",
"XXX = (XXX, XXX)"
]
def test2():
    lines = open('input.txt').readlines()
    parsed = parse_input(lines)

    dir = parsed[0]
    path = parsed[1]

    starts= filter(lambda x: x.endswith('A'),path.keys())
    steps = map(lambda x:walk_az(dir,path,x), starts)
    res = math.lcm(*steps)
    print(res)

