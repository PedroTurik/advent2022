class Blizzard:
    def __init__(self, y, x, selector, direction, size) -> None:
        self.pos = [y,x]
        self.selector = selector
        self.direction = direction
        self.size = size

    def move(self):
        self.pos[self.selector] = (self.pos[self.selector] + self.direction)%self.size
    

with open('input.txt') as f:
    board = [[x for x in row.strip()] for row in f.readlines()]

Y = len(board)
X = len(board[0])

blizzards = []

for y in range(Y):
    for x in range(X):
        if board[y][x] != '.':
            blizzards.append(Blizzard(y, x, 1, 1, X))

print(len(blizzards))