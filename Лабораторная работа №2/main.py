class BusStop:

    def __init__(self, name, coordinates, time_to_next):
        self.name = name
        self.coordinates = coordinates
        self.time_to_next = time_to_next
        self.next = None


class BusRoute:

    def __init__(self):
        self.head = None
        self.circular = False

    # Добавление остановки
    def add_stop(self, name, coordinates, time_to_next):
        new_stop = BusStop(name, coordinates, time_to_next)

        if self.head is None:
            self.head = new_stop

            if self.circular:
                new_stop.next = self.head

            return

        current = self.head

        while current.next and current.next != self.head:
            current = current.next

        current.next = new_stop

        if self.circular:
            new_stop.next = self.head

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

        prev = None
        current = self.head

        if self.circular:
            tail = self.head

            while tail.next != self.head:
                tail = tail.next

            tail.next = None

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

        if self.circular:
            tail = self.head

            while tail.next:
                tail = tail.next

            tail.next = self.head

    # Создание кольцевого маршрута
    def make_circular(self):
        if self.head is None:
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = self.head
        self.circular = True

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
                file.write(f"Координаты: {current.coordinates}\n")
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
                file.write("Маршрут является кольцевым\n")
            else:
                file.write("Маршрут НЕ является кольцевым\n")

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

print("\nРазворачиваем маршрут...")
route.reverse_route()

print("\nМаршрут после разворота:")
route.print_route()

route.generate_report("route_report.txt")

print("\nОтчет сохранен в route_report.txt")