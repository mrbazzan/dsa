
s = "10#adelaaleda4#neet3#you"

def decode(word):
    idx, i = 0, 0
    lst = []
    while idx < len(s):
        count = 0
        if s[idx] == "#":
            count = int(s[i:idx])
            i = idx + 1 + count
            lst.append(s[idx+1:i])
        idx = idx + count + 1
    return lst


print(decode(s))
