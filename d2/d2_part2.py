from functools import reduce
import re

#common_str = "([1-9])"

def single_tuple(line):
    number_color = line.strip().split(' ')
    return (number_color[1],int(number_color[0]))

rgb = ["red","green","blue"]
def min_tuple(line):

    key_values = dict(map(single_tuple,line.split(',')))

    for key in rgb:
        if key not in key_values:
            key_values[key] = 0

    return tuple([key_values[key] for key in rgb])

def parse_line(line):
    if not line:
        return 0
    
    game_number = int(line.split(':')[0].split(" ")[1])

    multi_round = line.split(':')[1].split(';')

    min_tuples = map(min_tuple,multi_round)

    all_min = reduce(lambda x,y: (max(x[0],y[0]), max(x[1],y[1]), max(x[2],y[2])), min_tuples)

    return all_min[0] * all_min[1] * all_min[2]


def main():

    it = map(parse_line,open('input','r').read().split("\n"))
    all_sum = reduce(lambda x, y: x+y,  it)

    print(all_sum)

main()
