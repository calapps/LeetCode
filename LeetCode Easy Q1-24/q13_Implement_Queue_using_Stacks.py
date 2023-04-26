# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.mainStack = []
        self.balancer = []
        self.size = 0

    def push(self, x):

        if not self.mainStack:
            self.mainStack.append(x)
            self.size += 1
            return 

        if self.mainStack:
            for _ in range(len(self.mainStack)):
                self.balancer.append(self.mainStack.pop())
            self.balancer.append(x)
            for _ in range(len(self.balancer)):
                self.mainStack.append(self.balancer.pop())
            self.size += 1
            return

    def pop(self):
        if self.mainStack:
            self.size -= 1
            return self.mainStack.pop()
        return None 

    def peek(self):
        if self.mainStack:
            return self.mainStack[-1]

    def empty(self):
        if self.size == 0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


# 1,2,3
# [1], [][1,2] => [2,1],
# [2,1], [][1,2,3] => [3,2,1]
# pop and peek would be returning 1 and self.size would return 