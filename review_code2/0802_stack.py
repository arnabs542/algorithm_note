# leetcode 225
# implement stack using queue
from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = deque([])
        self.queue2 = deque([])
        # if T, pop from queue2, if F, pop from queue1; after pop, change flag
        # if T, top from queue2, if F, top from queue1; after top, NOT change flag
        # if T, push to queue1, if F, push to queue2
        self.flag = True
        
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if self.flag:
            self.queue2.append(x)
        else:
            self.queue1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.flag:
            while len(self.queue2) > 1:
                self.queue1.append(self.queue2.popleft())
            self.flag = not self.flag
            return self.queue2.popleft()
        else:
            while len(self.queue1) > 1:
                self.queue2.append(self.queue1.popleft())
            self.flag = not self.flag
            return self.queue1.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.flag:
            while len(self.queue2) > 1:
                self.queue1.append(self.queue2.popleft())
            return self.queue2[0]
        else:
            while len(self.queue1) > 1:
                self.queue2.append(self.queue1.popleft())
            return self.queue1[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if self.queue1 or self.queue2:
            return False
        else:
            return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# leetcode 232
# implement queue using stacks
class MyQueue232:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # firstly store the pushed item
        self.stack1 = []
        
        # push the stack1 into stack2 when call peek or pop
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)
        return

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.stack2:
            return self.stack2.pop()
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack2:
            return self.stack2[-1]
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.stack1 or self.stack2:
            return False
        else:
            return True

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# leetcode 155
# implement min function with O(1) and stacks
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_elements = []
        self.global_min = float('inf')

    def push(self, x: int) -> None:
        # if empty
        if not self.stack:
            self.global_min = x
            self.min_elements.append(x)
            self.stack.append(x)
        else:
            
            if x < self.global_min:
                self.global_min = x
                
            self.stack.append(x)  
            self.min_elements.append(self.global_min)

    def pop(self) -> None:
        self.min_elements.pop()
        if self.min_elements:
            self.global_min = self.min_elements[-1]
        else:
            self.global_min = float('inf')
            
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_elements[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()