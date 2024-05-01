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

test1()
