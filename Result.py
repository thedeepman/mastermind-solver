class Result:
    reds = 0
    whites = 0
    permutation = []

    def __init__(self, permutation, reds=0, whites=0):
        self.permutation = permutation
        self.reds = reds
        self.whites = whites