def place_knigths(r):
    #pitäisi tehdä lauta ja laittaa toisiaan uhkaavat hepat graafiin pareiksi

    board = [[0]*18 for _ in range(18)]
    for x in range(1,9):
        board[0][x] = 1
        board[8+x][17] = 1
    # for line in board:
    #     print(line)

    
    for rivi in range(len(r)+1):
        for ruutu in range(len(r)+1):
            if ruutu == "*":                
                if rivi+1 <= len(r) and ruutu+2 <= len(r) and r[rivi+1][ruutu+2] == "*":
                    board[0][0] #ei tää oo hyvä tapa

def count(r):

    board = place_knigths(r)
    pass

if __name__ == "__main__":
    r = ["*.......",
         "..*...*.",
         "........",
         ".*......",
         "...*....",
         ".......*",
         "........",
         "......*."]
    print(r[0][0])
    print(count(r)) # 3