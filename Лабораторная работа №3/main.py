class Task:
    def __init__(self, task_id, description, priority):
        self.id = task_id
        self.description = description
        self.priority = priority

    def __str__(self):
        return f"ID: {self.id}, Описание: {self.description}, Приоритет: {self.priority}"


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, task):
        for existing_task in self.items:
            if existing_task.id == task.id:
                print(f"Ошибка: задача с id {task.id} уже существует")
                return

        self.items.append(task)

    def dequeue(self):
        if self.is_empty():
            print("Очередь пуста")
            return None
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            print("Очередь пуста")
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def show(self):
        if self.is_empty():
            print("Очередь пуста")
            return

        for task in self.items:
            print(task)


# Пример использования
queue = Queue()

queue.enqueue(Task(1, "Сделать лабораторную", 1))
queue.enqueue(Task(2, "Подготовить отчет", 2))
queue.enqueue(Task(1, "Повторяющийся id", 3))

print("Первая задача:")
print(queue.front())

print("\nВсе задачи:")
queue.show()

print("\nУдалена задача:")
print(queue.dequeue())

print("\nКоличество задач:")
print(queue.size())