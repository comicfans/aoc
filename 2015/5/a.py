import collections

def nice(line):

    for bad in ["ab", "cd", "pq", "xy"]:
        if bad in line:
            return False
    vowels = 0
    double = False
    for idx,c in enumerate(line):
        if c in "aeiou":
            vowels= vowels + 1
        if idx > 0 and line[idx-1] == c:
            double = True

    if vowels < 3:
        return False

    return double

assert nice("ugknbfddgicrmopn");
assert nice("aaa");
assert not nice("jchzalrnumimnmhp");
assert not nice("haegwjzuvuyypxyu");
assert not nice("dvszwmarrgswjxmb");


with open("input.txt","r") as f:
    print(len(list(filter(nice,f))))



def nice2(line):
    if len(line)<4:
        return False

    has_repeat = False
    for i in range(len(line)-2):
        repeat = line[i:i+2]
        if repeat in line[i+2:]:
            has_repeat = True
            break
    if not has_repeat:
        return False

    for i in range(1,len(line)-1):
        if line[i-1] == line[i+1]:
            return True
    return False

assert nice2("qjhvhtzxzqqjkmpb")
assert nice2("xxyxx")
assert not nice2("uurcxstgmygtbstg")
assert not nice2("ieodomkazucvgmuy")

with open("input.txt","r") as f:
    print(len(list(filter(nice2,f))))
