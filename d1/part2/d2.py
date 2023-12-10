from functools import reduce
import re

common_str = "([1-9]|one|two|three|four|five|six|seven|eight|nine)"
#common_str = "([1-9])"

value_map = {'one':1,
              'two':2,
              'three':3,
              'four':4,
              'five':5,
              'six':6,
              'seven':7,
              'eight':8,
              'nine':9}

num_map = dict([(str(i), i) for i in [1,2,3,4,5,6,7,8,9]])

all_map = {**num_map , **value_map}

last_re = re.compile(".*"+common_str)
def parse_line(line):
    if line == '':
        return 0
    first = re.search(common_str,line)
    last = re.search(last_re,line)

    first_n = all_map[first.group(1)]
    last_n = all_map[last.group(1)]

    return first_n * 10 + last_n


def main():

    it = map(parse_line,open('input','r').read().split("\n"))
    all_sum = reduce(lambda x, y: x+y,  it)
    print(all_sum)


main()
