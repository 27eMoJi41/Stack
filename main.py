class Stack:
    def __init__(self,size) -> None:
        self.arr = []
        self.capacity = size

    def push(self,x):
        if len(self.arr) == self.capacity:
            print("Overflow")

        else:
            print(f"Inserting {x}")
            return self.arr.append(x)

    def pop(self):
        if len(self.arr) == 0 :
            print("Stack Empty")
            
        else:
            return self.arr.pop()
        
    def print_stack(self):
        for i in range(len(self.arr)):
            print(self.arr[i],end=" ")
            
if __name__  == "__main__":
    stack = Stack(5)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.pop()
    stack.print_stack()


    
    