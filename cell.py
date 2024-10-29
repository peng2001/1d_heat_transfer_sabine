class Cell:
    # qL is a sympy equation representing heat transfer to the left cell, qR is is a sympy equation representing heat transfer to the right cell
    # convention: heat moving from left to right is positive
    def __init__(self, x, T, q, symbolT):
        self.x = x
        self.T = T
        self.symbolT = symbolT
        self.q = q