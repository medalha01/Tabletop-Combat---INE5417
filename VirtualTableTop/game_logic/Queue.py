

class Queue:
    def __init__(self) -> None:
        self.__queue : list = []

    def queue(self):
        return self.__queue

    def empty(self):
        if len(self.__queue) == 0: return True
        return False
    
    def push(self, item):
        self.__queue.insert(0, item)
    
    def remove(self, item):
        if not self.empty():
            return self.__queue.remove(item)
        return None

    def pop(self):
        if not self.empty():
            return self.__queue.pop()
        return None
    
    def top(self):
        if not self.empty():
            return self.__queue[-1]
        return None

