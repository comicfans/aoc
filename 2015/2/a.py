def need(str):
    whl = [int(x) for x in str.split('x')]
    areas = [whl[0] * whl[1], whl[1]* whl[2], whl[0]*whl[2]]
    all = sum(areas)
    min_area = min(areas)

    return all * 2 + min_area



with open("input.txt",'r') as f:
    print(sum(map(need, f)))


def need2(str):
    whl = sorted([int(x) for x in str.split('x')])
    all = whl[0]*2 + whl[1] * 2
    mul = whl[0] * whl[1] * whl[2]

    return all + mul

with open("input.txt",'r') as f:
    print(sum(map(need2, f)))
