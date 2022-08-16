def cakes(recipe, available):
    count = []
    for k in recipe:
        if k not in available:
            return 0
        count.append(available[k] // recipe[k])
    return min(count)
