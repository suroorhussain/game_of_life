def isdead(x, y, grid) :
    if grid[x][y] == 0 :
        return True
    else :
        return False

def count_live_neighbours(x, y, grid) :
    count = 0
    for dx in [-1, 0, 1] :
        for dy in [-1, 0, 1] :
            if dx == 0 and dy == 0 :
                continue
            elif x + dx < 0 or y + dy < 0 :
                continue
            else :
                try:
                    count += grid[x + dx][y + dy]
                except IndexError :
                    continue
    return count


def set_alive(x, y, grid) :
    grid[x][y] = 1

def set_dead(x, y, grid) :
    grid[x][y] = 0
