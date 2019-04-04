# Going to the Cinema
# Level 7kyu
# https://www.codewars.com/kata/reviews/562f93ec2bcdc1c475000071/groups/5ca557a20e9c9600010ece58

import math

def movie(card, ticket, perc):
    agg_cost_sys_a = 0
    agg_cost_sys_b = card
    
    shows_seen = 0
    last_ticket_sys_b = ticket * perc
    
    while (math.ceil(agg_cost_sys_b) >= math.ceil(agg_cost_sys_a)) :
        agg_cost_sys_a = agg_cost_sys_a + ticket
        agg_cost_sys_b = agg_cost_sys_b + last_ticket_sys_b
        last_ticket_sys_b = last_ticket_sys_b * perc
        shows_seen = shows_seen + 1
    
    return shows_seen
