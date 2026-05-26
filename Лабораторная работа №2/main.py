class BusStop:

    def __init__(self, name, coordinates, time_to_next):
        self.name = name
        self.coordinates = coordinates
        self.time_to_next = time_to_next

        self.next = None
        self.prev = None


class BusRoute:

    def __init__(self):
        self.head = None
        self.tail = None
        self.circular = False

    # Добавление остановки
    def add_stop(self, name, coordinates, time_to_next):

        new_stop = BusStop(name, coordinates, time_to_next)

        if self.head is None:
            self.head = new_stop
            self.tail = new_stop

            if self.circular:
                self.head.next = self.head
                self.head.prev = self.head

            return

        new_stop.prev = self.tail
        self.tail.next = new_stop
        self.tail = new_stop

        if self.circular:
            self.tail.next = self.head
            self.head.prev = self.tail

    # Удаление последней остановки
    def remove_last_stop(self):

        if self.head is None:
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        self.tail = self.tail.prev
        self.tail.next = None

        if self.circular:
            self.tail.next = self.head
            self.head.prev = self.tail

    # Подсчет общего времени маршрута
    def total_route_time(self):

        if self.head is None:
            return 0

        total = 0
        current = self.head

        while True:

            total += current.time_to_next
            current = current.next

            if current is None or current == self.head:
                break

        return total

    # Где будет автобус через N остановок
    def get_stop_after_n(self, n):

        if self.head is None:
            return "Маршрут пуст"

        current = self.head

        for _ in range(n):

            if current.next is None:
                return "Маршрут закончился"

            current = current.next

        return current.name

    # Построение обратного маршрута
    def reverse_route(self):

        if self.head is None:
            return

        current = self.head
        self.head, self.tail = self.tail, self.head

        while current:

            current.next, current.prev = (
                current.prev,
                current.next
            )

            current = current.prev

            if self.circular and current == self.head:
                break

        if self.circular:
            self.tail.next = self.head
            self.head.prev = self.tail

    # Реализация кольцевого маршрута
    def make_circular(self):

        if self.head is None:
            return

        self.circular = True

        self.tail.next = self.head
        self.head.prev = self.tail

    # Подробный отчет
    def generate_report(self, filename):

        with open(filename, "w", encoding="utf-8") as file:

            if self.head is None:
                file.write("Маршрут пуст\n")
                return

            file.write("ОТЧЕТ ПО МАРШРУТУ\n")
            file.write("=" * 40 + "\n")

            current = self.head
            stop_number = 1

            while True:

                file.write(f"Остановка #{stop_number}\n")
                file.write(f"Название: {current.name}\n")
                file.write(
                    f"Координаты: {current.coordinates}\n"
                )
                file.write(
                    f"Время до следующей: "
                    f"{current.time_to_next} мин\n"
                )

                file.write("-" * 40 + "\n")

                current = current.next
                stop_number += 1

                if current is None or current == self.head:
                    break

            file.write(
                f"\nОбщее время маршрута: "
                f"{self.total_route_time()} мин\n"
            )

            if self.circular:
                file.write(
                    "Маршрут является кольцевым\n"
                )
            else:
                file.write(
                    "Маршрут не является кольцевым\n"
                )

    # Вывод маршрута
    def print_route(self):

        if self.head is None:
            print("Маршрут пуст")
            return

        current = self.head

        while True:

            print(
                f"{current.name} "
                f"{current.coordinates} "
                f"-> {current.time_to_next} мин"
            )

            current = current.next

            if current is None or current == self.head:
                break


route = BusRoute()

route.add_stop("Центр", (55.75, 37.61), 10)
route.add_stop("Парк", (55.76, 37.62), 7)
route.add_stop("Университет", (55.77, 37.63), 12)

print("Маршрут:")
route.print_route()

print("\nОбщее время маршрута:")
print(route.total_route_time(), "мин")

print("\nЧерез 2 остановки автобус будет на:")
print(route.get_stop_after_n(2))

print("\nСоздаем кольцевой маршрут...")
route.make_circular()

print("\nУдаляем последнюю остановку...")
route.remove_last_stop()

print("\nМаршрут после удаления:")
route.print_route()

print("\nРазворачиваем маршрут...")
route.reverse_route()

print("\nМаршрут после разворота:")
route.print_route()

route.generate_report("route_report.txt")

print("\nОтчет сохранен в route_report.txt")