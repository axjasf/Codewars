# Find middle characters in a string
# Level: 7kyu

def get_middle(s):
    length = len(s)
    if length % 2 == 0:
        left = (length / 2) -1
        right = (length / 2) +1
    else:
        left = ((length-1)/2)
        right = left+1
    return s[left:right]
