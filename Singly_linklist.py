class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = Node('head')
        self.size = 0

    def __str__(self):
        current_node = self.head.next
        output = ""
        while current_node:
            output += str(current_node.value)+' '
            current_node = current_node.next
        return output

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def peek(self):
        if self.isEmpty():
            return Exception('peek from empty stack ')
        return self.head.next.value

    def insert(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value


if __name__ == "__main__":
    stack = Stack()
    stack.insert(4)
    stack.insert(9)
    stack.insert(10)
    stack.insert(8)
    print(f"Stack: {stack}")

    print(stack.pop(), stack.pop(), stack.pop())

    print(f"Stack: {stack}")
