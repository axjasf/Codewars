# Are the amount of x's and o's in a string equal, case independent?
# Level: 7kyu

def xo(s):
    x_count = 0
    o_count = 0
    for c in s.upper():
        if c == "X":
            x_count = x_count + 1
        if c == "O":
            o_count = o_count +1
    return (x_count == o_count)
