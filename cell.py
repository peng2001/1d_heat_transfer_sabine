class Cell:
    # qL is a sympy equation representing heat transfer to the left cell, qR is is a sympy equation representing heat transfer to the right cell
    # convention: heat moving from left to right is positive
    # const is right hand of polynomial for sympy to solve
    def __init__(self, x, T, q, symbolT, const):
        self.x = x
        self.T = T
        self.symbolT = symbolT
        self.q = q