class Task:

    def __init__(self, task_id, description, priority):
        self.id = task_id
        self.description = description
        self.priority = priority

    def __str__(self):
        return f"[ID: {self.id}] {self.description} | Приоритет: {self.priority}"


class TaskQueue:

    def __init__(self):
        self.queue = []

    # Добавление задачи
    def enqueue(self, task):

        for existing_task in self.queue:
            if existing_task.id == task.id:
                print(f"Ошибка: задача с id = {task.id} уже существует!")
                return

        self.queue.append(task)
        print("Задача добавлена.")

    # Удаление задачи
    def dequeue(self):

        if self.isEmpty():
            print("Очередь пуста.")
            return None

        return self.queue.pop(0)

    # Первая задача
    def front(self):

        if self.isEmpty():
            print("Очередь пуста.")
            return None

        return self.queue[0]

    # Проверка очереди
    def isEmpty(self):
        return len(self.queue) == 0

    # Вывод задач
    def show_tasks(self):

        if self.isEmpty():
            print("Очередь пуста.")
            return

        print("\nСписок задач:")

        for task in self.queue:
            print(task)


task_queue = TaskQueue()

task1 = Task(1, "Сделать лабораторную работу", 1)
task2 = Task(2, "Подготовить отчет", 2)
task3 = Task(1, "Повторяющийся id", 3)

task_queue.enqueue(task1)
task_queue.enqueue(task2)
task_queue.enqueue(task3)

task_queue.show_tasks()

print("\nПервая задача:")
print(task_queue.front())

print("\nУдаленная задача:")
print(task_queue.dequeue())

task_queue.show_tasks()