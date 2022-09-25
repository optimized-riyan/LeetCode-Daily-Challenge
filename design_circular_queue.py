'''
In a circular queue, we use a wraparound technique where if the queue becomes full till the end, 
we set the "back" variable back to index 0.
'''

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k                  # Size
        self.queue = [0] * k        
        self.front = 0              # Front of queue
        self.back = 0               # Back of queue
        self.wraparound = False     # To check if "back" has been wrapped around already

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        b = self.back
        self.queue[b] = value
        b += 1
        self.back = b
        if b == self.k:             # If last index is reached, we set b to 0
            self.back = 0
            self.wraparound = True
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        f = self.front
        f += 1
        self.front = f
        if f == self.k:
            self.front = 0          # If front reaches the end, we wraparound front as well
            self.wraparound = False
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.back - 1) % self.k]

    def isEmpty(self) -> bool:
        if self.back == self.front and not self.wraparound:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.back == self.front and self.wraparound:
            return True
        else:
            return False