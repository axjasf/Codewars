# Growth of a population
# Level 7kyu
# https://www.codewars.com/kata/reviews/563b677259afc2b5120000cd/groups/5ca51a2800f2270001f1b0f2
#
# Variables:
#   Start population (*p0*), Growth per year in percentage (*percent*), additional augmented growth per year (*aug*), final population (*p*

def nb_year(p0, percent, aug, p):
    
    current_polulation = p0
    years_to_p = 0
    
    while current_polulation < p :
        current_polulation = current_polulation + (current_polulation * (percent/100)) + aug
        years_to_p += 1
        
    return years_to_p
