def wave(people):
    return [people[:i] + people[i].upper() + people[i+1:] for i in range(len(people)) if people[i] != ' ']

def wave2(people):
    wave_arr = []
    temp_people = list(people)
    for i in range(len(people)):
        if temp_people[i] != ' ':
            temp = temp_people[i]
            temp_people[i] = temp_people[i].upper()
            wave_arr.append(''.join(temp_people))
            temp_people[i] = temp
    return wave_arr

# print(wave('hello'))
        