class Queue:
    def __init__(self):
        self.items = []


    def is_empty(self):  # Проверка на пустоту
        return self.items == []


    def enqueue(self, item):  # Добавление элемента в конец очереди (первое место списка)
        self.items.insert(0, item)


    def dequeue(self):  # Удаление первого элемента очереди (последний элемент списка)
        return self.items.pop()


    def size(self):  # Длина - количество элементов в очереди
        return len(self.items)



queue = Queue()
print(queue.is_empty())
queue.enqueue("действие 1")
queue.enqueue("действие 2")
queue.enqueue("действие 3")
queue.enqueue("действие 4")
print(queue.items)
print(queue.is_empty())
print(queue.size())
print(queue.dequeue())
print(queue.size())
print(queue.items)