def cut(sup_limit, inf_limit, number):
    if number > sup_limit:
        return sup_limit
    elif number < inf_limit:
        return inf_limit
    else:
        return number

print(cut(10, 5, 7))