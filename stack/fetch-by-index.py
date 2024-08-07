"""
Write a python program to fetch the item of stack of 3rd index
"""

class FetchByIndex :
    def __init__(self) :
        self.stack = []

    def fetch(self, data) :
        self.stack = data
        return self.stack[-3]

fetchByIndex = FetchByIndex()

result = fetchByIndex.fetch(['bmw', 'audi', 'porsche', 'farrari'])

print("Your Stack is: ", result)