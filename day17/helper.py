class tetris:
    def canMoveDown(self):
        for y, x in self.cords:
            if self.matrix[y+1][x] or y+1 == 0:
                return False
        return True

    def canMoveRight(self):
        for y, x in self.cords:
            if x == 6 or self.matrix[y][x+1]:
                return False
        return True

    def canMoveLeft(self):
        for y, x in self.cords:
            if x == 0 or self.matrix[y][x-1]:
                return False
        return True

    def moveLeft(self):
        if self.canMoveLeft():
            for cord in self.cords:
                cord[1] -= 1

    def moveRight(self):
        if self.canMoveRight():
            for cord in self.cords:
                cord[1] += 1

    def moveDown(self):
        if self.canMoveDown():
            for cord in self.cords:
                cord[0] += 1
            return True
        else:
            return False

    def getNewHeight(self):
        return min([y for y, x in self.cords]) - 4


    def markMatrix(self):
        for y, x in self.cords:
            self.matrix[y][x] = 1


class four_line(tetris):
    def __init__(self, matrix, height) -> None:
        self.matrix = matrix
        self.cords = [[height, x] for x in range(2, 6)]

class plus_sign(tetris):
    def __init__(self, matrix, height) -> None:
        self.matrix = matrix
        self.cords = [[height-1, 2], [height, 3], [height-1, 3], [height-2, 3], [height-1, 4]]

class reverse_l(tetris):
    def __init__(self, matrix, height) -> None:
        self.matrix = matrix
        self.cords = [[height, 2], [height, 3], [height, 4], [height-1, 4], [height-2, 4]]

class vertical_line(tetris):
    def __init__(self, matrix, height) -> None:
        self.matrix = matrix
        self.cords = [[height, 2], [height-1, 2], [height-2, 2], [height-3, 2]]

class block(tetris):
    def __init__(self, matrix, height) -> None:
        self.matrix = matrix
        self.cords = [[height, 2], [height-1, 2], [height, 3], [height-1, 3]]
