import functools

def pred(ser):
    assert len(ser)>=2

    if len(set(ser)) == 1:
        return ser[0]

    deltas = [ser[i+1] - ser[i] for i in range(len(ser)-1) ]
    next_delta = pred(deltas)
    return ser[len(ser)-1] + next_delta

example = [
"0 3 6 9 12 15",
"1 3 6 10 15 21",
"10 13 16 21 30 45"
]

def parse_lines(lines):
    return map(lambda x: [int(v) for v in x.strip().split(' ')],lines)

def test1():
    lines = open('input.txt').readlines()
    parsed = parse_lines(lines)
    res = map(pred, parsed)
    sum = functools.reduce(lambda x,y:x+y, res)
    print(sum)

def pred2(ser):
    assert len(ser)>=2

    if len(set(ser)) == 1:
        return ser[0]

    deltas = [ser[i+1] - ser[i] for i in range(len(ser)-1) ]
    prev_delta = pred2(deltas)
    return ser[0] - prev_delta 


def test2():
    lines = open('input.txt').readlines()
    parsed = parse_lines(lines)
    res = map(pred2, parsed)
    sum = functools.reduce(lambda x,y:x+y, res)
    print(sum)


test2()
