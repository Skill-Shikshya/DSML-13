class Sum:
    def __init__(self, *nums):
        self.numbers = nums

    def add(self):
        return sum(self.numbers)

