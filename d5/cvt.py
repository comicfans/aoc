from bisect import bisect_left

def map_to_pos(maps, seed):
    res = seed
    for m in maps:
        k = bisect_left(m, res, key = lambda x: x[0])
        if k == len(m) or m[k-1][0]!= res: 
            k-=1
        if k < 0:
            continue
        if m[k][0] + m[k][2]>= res:
            res = res - m[k][0] + m[k][1]
    return res

def map_to_range(map, start, length):
    pass

def parseMap(lines):
    seeds = None
    maps = []

    lines.append(" fake map:")
    for l in lines:
        line = l.strip()
        if len(line) == 0:
            continue

        if line.startswith("seeds"):
            seeds = [int(num) for num in line[len("seeds:"):].strip().split(' ')]
            continue

        if line.endswith(" map:"):
            if len(maps)>0:
                maps[len(maps)-1].sort(key=lambda x:x[0])
            maps.append([])
            continue

        dst_src_len= [int(num) for num in line.strip().split(' ')]
        maps[len(maps)-1].append([dst_src_len[1], dst_src_len[0], dst_src_len[2]])

    maps.pop()
    return (seeds, maps)


def test1():
    example=["seeds: 79 14 55 13"
            ,""
            ,"seed-to-soil map:"
            ,"50 98 2"
            ,"52 50 48"
            ,""
            ,"soil-to-fertilizer map:"
            ,"0 15 37"
            ,"37 52 2"
            ,"39 0 15"
            ,""
            ,"fertilizer-to-water map:"
            ,"49 53 8"
            ,"0 11 42"
            ,"42 0 7"
            ,"57 7 4"
            ,""
            ,"water-to-light map:"
            ,"88 18 7"
            ,"18 25 70"
            ,""
            ,"light-to-temperature map:"
            ,"45 77 23"
            ,"81 45 19"
            ,"68 64 13"
            ,""
            ,"temperature-to-humidity map:"
            ,"0 69 1"
            ,"1 0 69"
            ,""
            ,"humidity-to-location map:"
            ,"60 56 37"
            ,"56 93 4"]
    res1= parseMap(example)
    seeds = res1[0]
    maps = res1[1]
    pos = map(lambda x:map_to_pos(maps,x), seeds)
    res = min(pos)
    print(res)
    return res



def test2():
    with open('input.txt') as f:
        lines = f.readlines()
        res1 = parseMap(lines)
        seeds = res1[0]
        maps = res1[1]
        pos = map(lambda x:map_to_pos(maps,x), seeds)
        res = min(pos)
        assert(res == 318728750)
        print(res)

def test3():
    with open('input.txt') as f:
        lines = f.readlines()
        res1 = parseMap(lines)
        start_range = res1[0]

        maps = res1[1]
        pair_number = len(start_range)/2

        start_range_pair= [(start_range[idx*2],start_range[idx * 2 + 1]) for idx in range(int(pair_number))]

        seeds = [list([i + start for i in range(r)]) for (start, r) in start_range_pair]


        pos = map(lambda x:map_to_pos(maps,x), seeds)
        res = min(pos)
        print(res)

#test2()
#test2()
test3()
