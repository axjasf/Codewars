# Find force of gravity between two objects
# Level 8kyu
# [https://www.codewars.com/kata/reviews/5b65af1485875e82160000d0/groups/5ca3f4bafc099a000195e129]

def convert_mass_to_kg(mass, unit) :
    mass = float(mass)
    unit = str(unit)
    
    if unit == "g" :
        factor = 0.001
    elif unit == "mg" :
        factor = 1 * (10**-6)
    elif unit == "μg" :
        factor = 1 * (10**-9)
    elif unit == "lb" :
        factor = 0.453592
    else : 
        factor = 1
    return float(mass * factor)

def convert_distance_to_meters(distance, unit) :
    distance = float(distance)
    unit = str(unit)
    
    if unit == "cm" :
        factor = 0.01
    elif unit == "mm" :
        factor = 0.001
    elif unit == "μm" :
        factor = 1 * (10**-6)
    elif unit == "ft" :
        factor = 0.3048
    else : 
        factor = 1
    return float(distance * factor)

def solution(arr_val, arr_unit) :
    # Define gravity G
    G = 6.67*(10**-11)
    
    m1 = convert_mass_to_kg(arr_val[0], arr_unit[0])
    m2 = convert_mass_to_kg(arr_val[1], arr_unit[1])
    d = convert_distance_to_meters(arr_val[2], arr_unit[2])
    
    F_grav = (G * m1 * m2) / (d**2)
    return F_grav
