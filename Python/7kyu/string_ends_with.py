# Find out, if a string ends with a specific ending
# Level: 7kyu
# https://www.codewars.com/kata/reviews/5463ab67541c67d9b0000064/groups/546439056be3378e7a000367

def solution(string, ending):
    return string[-len(ending):] == ending
