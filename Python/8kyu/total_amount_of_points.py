# Total amount of points in a series of 10 games
# 3 if won, 1 if draw, 0 if lost
# https://www.codewars.com/kata/reviews/5bb9109b16a8f195ea001643/groups/5ca41dd24674b100018a3d6a

def points(games):
    score = 0
    for game in games :
        if int(game[0]) > int(game[2]) :
            score = score + 3
        elif int(game[0]) == int(game[2]) :
            score = score + 1
    return score
