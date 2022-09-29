def move_locations(locations, movedFrom, movedTo):
    n = len(movedFrom)
    for i in range(n):
        locations[locations.index(movedFrom[i])] = movedTo[i]
    return locations

print(sorted(move_locations([1,7,6,8], [1,7,2], [2,9,5])))