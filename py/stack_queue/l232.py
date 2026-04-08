from random import seed


class MyQueue0:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.size = 0

    def push(self, x: int) -> None:
        self.stack1.append(x)
        self.size += 1

    def pop(self) -> int:
        if self.stack1 is None and self.stack1 is None and self.size == 0:
            return
        for i in self.stack1:
            self.stack2.append(i)
        self.stack1 = []
        temp = self.stack2[0]
        self.stack2 = self.stack2[1:]
        self.size -= 1
        return temp

    def peek(self) -> int:
        if self.stack1 is None and self.stack1 is None and self.size == 0:
            return
        for i in self.stack1:
            self.stack2.append(i)
        self.stack1 = []
        return self.stack2[0]

    def empty(self) -> bool:
        return True if self.size == 0 else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


class MyQueue1:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if self.empty():
            return None

        if self.stack_out:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self) -> int:
        tmp = self.pop()
        self.stack_out.append(tmp)
        return tmp

    def empty(self) -> bool:
        return not (self.stack_in or self.stack_out)
