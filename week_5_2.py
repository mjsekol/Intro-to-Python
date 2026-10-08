# return

def get_jedi_rank(force_level):
    if force_level >= 90:
        return "Jedi Master"
    elif force_level >= 70:
        return "Jedi Knight"
    elif force_level >= 40:
        return "Padawan"
    else:
        return "Youngling"

anakin_rank = get_jedi_rank(95)
obiwan_rank = get_jedi_rank(85)
print(f"Anakin's rank is: {anakin_rank}") # prints Anakin's rank based on his force level


print(get_jedi_rank(99)) # prints the rank for a force level of 99
print(get_jedi_rank(85)) # prints the rank for a force level of 85
print(get_jedi_rank(65)) # prints the rank for a force level of 65
print(get_jedi_rank(35)) # prints the rank for a force level of 35