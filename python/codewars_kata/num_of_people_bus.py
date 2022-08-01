def number(bus_stops):
    return sum(stop[0]-stop[1] for stop in bus_stops)

if __name__ == '__main__':
    print(number([[10,0], [3,5], [5,8]]))