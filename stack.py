# Стеки
class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):  # Проверка на пустоту
        return self.items == []

    def push(self, item):  # Добавить элемент
        self.items.append(item)


    def pop(self):  # Удаление верхнего элемента
        return self.items.pop()


    def peek(self):  #  Получить верхний элемент буз удаления
        return self.items[-1]


stack = Stack()
print(stack.is_empty())

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.is_empty())

print(stack.peek())