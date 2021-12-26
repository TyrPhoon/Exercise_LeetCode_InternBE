# Min Stack

class MinStack:

    def __init__(self):
        self.arr = []
    def push(self, val: int) -> None:
        self.arr.append(val)

    def pop(self) -> None:
        self.arr = self.arr[:len(self.arr)-1]

    def top(self) -> int:
        return self.arr[len(self.arr)-1]

    def getMin(self) -> int:
        return min(self.arr)