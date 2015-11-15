import game_of_life

test_data = [[0,0,1,1], [0,0,1,0], [1,0,0,0]]

def test_isdead_true() :
    dead = game_of_life.isdead(0,0,test_data)
    assert dead == True

def test_isdead_false() :
    dead = game_of_life.isdead(0, 2, test_data)
    assert dead == False

# def test_count_live_neighbours() :
#     count = game_of_life.count_live_neighbours(0, 2, test_data)
#     assert count == 2

def test_set_alive() :
    game_of_life.set_alive(0, 0, test_data)
    assert test_data[0, 0] == 1
