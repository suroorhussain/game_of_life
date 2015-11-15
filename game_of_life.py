def isdead(x, y, grid) :
    if grid[x][y] == 0 :
        return True
    else :
        return False

# def count_live_neighbours(x, y, grid) :
#     count = 0
#     if 

def set_alive(x, y, grid) :
    grid[x][y] = 1
