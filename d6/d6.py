import math
import functools
import re
# total time    t
# time to press p
# time to run   r = t - p
# speed         v = p
# distance      l = v * r = p * (t-p) = -p^2 + tp
# record        m  
# to find        - p^2 + tp > m
#  - p^2 + tp -m  > 0
# x1,x2 =    (-b +- sqrt(b^2 - 4ac))/2a
# a=-1, b = t , c = -m          
# (-t   +-     sqrt( t^2  - 4 * (-1) *(-m) )) / 2 * (-1)
#  (-t +-   sqrt(t^2 - 4m) ) / -2
##  (t +- sqrt(t^2 - 4m)) / 2

input = ["Time:        35     93     73     66",
           "Distance:   212   2060   1201   1044"]

example = ["Time:      7  15   30",
"Distance:  9  40  200"]

def parse_line(line):
    time_line = [int(x) for x in re.split(' +',line[0].split(":")[1].strip())]
    distance_line = [int(x) for x in re.split(' +',line[1].split(":")[1].strip())]
    return list(zip(time_line,distance_line))


def count_res(pair):
    t = pair[0]
    m = pair[1]

    b2_minus_4ac = t*t - 4*m
    if b2_minus_4ac <= 0:
        return 0

    left = (t - math.sqrt(b2_minus_4ac))/2
    right = (t + math.sqrt(b2_minus_4ac))/2

    # left round to right
    # [0  ~  1) => 1
    # [-1 ~  0) => 0

    left_int = math.floor(left)+1
    right_int = math.ceil(right) - 1
    return right_int - left_int + 1

def test1():
    pairs = parse_line(input)
    possible = map(count_res, pairs)
    res = functools.reduce(lambda x,y: x*y, possible)
    print(res)
    

test1()

def test2():
    merged = [x.replace(' ','') for x in input]
    pairs = parse_line(merged)
    possible = map(count_res, pairs)
    print(list(possible)[0])

test2()
