"""
Write a program to impliment stack data structures.
"""

class Stack :
    def __init__(self) :
        self.data = []
    
    def isEmpty(self) :
        return len(self.data) == 0
    
    def push(self, item) :
        self.data.insert(0,item)

    def traverse(self) :
        return self.data
    
    def remove(self) :
        if self.isEmpty() :
            return "Empty Stack !"
        return self.data.pop(0)
    
    def peak(self) :
        return self.data[0]

stack = Stack()

print("Push Operation =============================")
# push data
stack.push("just")
stack.push("asad")
stack.push("ahad")

print("Traverse Operation =============================")
print(stack.traverse());

print("Pop Operation =============================")
print(stack.remove())

print("Traverse Operation =============================")
print(stack.traverse());

print("Peak Operation =============================")
print(stack.peak())