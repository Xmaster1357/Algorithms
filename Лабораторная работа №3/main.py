# Задача 1 — Система обработки задач (Queue)
# Вариативная часть №9:
# Запретить добавление задач с одинаковым id


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
        self.completed_tasks = 0

    # enqueue(task)
    def enqueue(self, task):
        # Проверка на одинаковый id
        for existing_task in self.queue:
            if existing_task.id == task.id:
                print(f"Ошибка: задача с id = {task.id} уже существует!")
                return

        self.queue.append(task)
        print("Задача добавлена.")

    # dequeue()
    def dequeue(self):
        if self.isEmpty():
            print("Очередь пуста.")
            return None

        self.completed_tasks += 1
        return self.queue.pop(0)

    # front()
    def front(self):
        if self.isEmpty():
            print("Очередь пуста.")
            return None

        return self.queue[0]

    # isEmpty()
    def isEmpty(self):
        return len(self.queue) == 0

    # Вывод всех задач
    def show_tasks(self):
        if self.isEmpty():
            print("Очередь пуста.")
            return

        print("\nСписок задач:")
        for task in self.queue:
            print(task)



# Задача 2 — Проверка выражений (Stack)
# Вариативная часть №9:
# Показывать содержимое стека после каждого шага


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]

    def isEmpty(self):
        return len(self.items) == 0

    def show(self):
        return self.items


def check_brackets(expression):
    stack = Stack()

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    print("\nПроверка строки:", expression)

    for symbol in expression:

        # Открывающая скобка
        if symbol in "([{":
            stack.push(symbol)
            print(f"Добавили '{symbol}' -> Стек: {stack.show()}")

        # Закрывающая скобка
        elif symbol in ")]}":

            if stack.isEmpty():
                print(f"Ошибка: лишняя '{symbol}'")
                return False

            top = stack.pop()
            print(f"Удалили '{top}' -> Стек: {stack.show()}")

            if pairs[symbol] != top:
                print("Ошибка: неправильная последовательность.")
                return False

    if stack.isEmpty():
        print("Строка корректна.")
        return True
    else:
        print("Ошибка: не хватает закрывающей скобки.")
        return False



# Задача 3 — Очередь через два стека
# Вариативная часть №9:
# Проверка на переполнение


class QueueTwoStacks:
    def __init__(self, max_size):
        self.stack1 = []
        self.stack2 = []
        self.max_size = max_size

    # enqueue(x)
    def enqueue(self, x):

        if self.size() >= self.max_size:
            print("Ошибка: очередь переполнена!")
            return

        self.stack1.append(x)
        print(f"Добавлен элемент: {x}")

    # dequeue()
    def dequeue(self):

        if self.front() is None:
            print("Очередь пуста.")
            return None

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    # front()
    def front(self):

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:
            return None

        return self.stack2[-1]

    # Размер очереди
    def size(self):
        return len(self.stack1) + len(self.stack2)

    # Вывод очереди
    def show(self):

        queue_elements = self.stack2[::-1] + self.stack1

        if not queue_elements:
            print("Очередь пуста.")
            return

        print("Элементы очереди:", queue_elements)


# =========================================================
# ДЕМОНСТРАЦИЯ РАБОТЫ ПРОГРАММЫ
# =========================================================

print("=================================================")
print("ЗАДАЧА 1 — Система обработки задач")
print("=================================================")

task_queue = TaskQueue()

task1 = Task(1, "Сделать лабораторную", 1)
task2 = Task(2, "Подготовить отчет", 2)
task3 = Task(1, "Повторяющийся ID", 3)

task_queue.enqueue(task1)
task_queue.enqueue(task2)
task_queue.enqueue(task3)

task_queue.show_tasks()

print("\nПервая задача:")
print(task_queue.front())

print("\nУдаленная задача:")
print(task_queue.dequeue())

task_queue.show_tasks()


print("\n=================================================")
print("ЗАДАЧА 2 — Проверка выражений")
print("=================================================")

check_brackets("([]{})")
check_brackets("([)]")


print("\n=================================================")
print("ЗАДАЧА 3 — Очередь через два стека")
print("=================================================")

queue = QueueTwoStacks(3)

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

# Переполнение
queue.enqueue(40)

queue.show()

print("\nПервый элемент:")
print(queue.front())

print("\nУдаленный элемент:")
print(queue.dequeue())

queue.show()