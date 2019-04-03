# Is n divisible by x and y
# Level: 8kyu
# https://www.codewars.com/kata/reviews/5589fda1a0db8600f9000064/groups/558a6ebaa4a715ced00000b3

def is_divisible(n,x,y):
    return ((n % x == 0) and (n % y == 0))
