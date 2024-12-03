import re
# write regex to extract mul(number,number)

def part1():
    regex = re.compile(r'mul\((\d+),(\d+)\)')
    
    sum = 0
    with open ("input.txt", 'r') as f:
        for line in f:
            for match in regex.finditer(line):
                sum += int(match.group(1)) * int(match.group(2))
    
    print(sum)

part1()
def part2_line(line):

    regex = re.compile(r'mul\((\d+),(\d+)\)|don\'t\(\)|do\(\)')
    sum = 0
    enable = True
    for match in regex.finditer(line):
        print(match.group(0))
        if match.group(0).startswith('mul'):
            if enable:
                sum += int(match.group(1)) * int(match.group(2))
            continue

        if match.group(0) == "don't()":
            enable = False
            continue

        if match.group(0) == "do()":
            enable = True
            continue
        assert False
    print(f"sum is {sum}-----")
    return sum

def part2():

    sum = 0

    with open ("input.txt", 'r') as f:
        for line in f:
            sum += part2_line(line)
            
    print(sum)
#print(part2_line("don't()do(mul()mul(2,3)do()mul(2,3)mul(6,7)mul(don't()"))
part2()
