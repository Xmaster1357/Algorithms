import os

# 1. СЛОЙ МОДЕЛЕЙ

class BusStop:
    # Узел двусвязного списка, представляющий автобусную остановку.
    def __init__(self, name: str, coordinates: tuple[float, float], time_to_next: float):
        self.name = name
        self.coordinates = coordinates
        self.time_to_next = time_to_next # Время в пути до следующей остановки
        self.next = None
        self.prev = None

    def __str__(self):
        return f"[{self.name} {self.coordinates}]"


# 2. СЛОЙ ЛОГИКИ

class BusRoute:
    # Двусвязный кольцевой список для управления маршрутом.
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_stop(self, name: str, coordinates: tuple[float, float], time_to_next: float):
        # Добавление остановки. Обработка кольцевой связи.
        new_stop = BusStop(name, coordinates, time_to_next)

        if self.size == 0:
            self.head = new_stop
            self.tail = new_stop
            new_stop.next = new_stop
            new_stop.prev = new_stop
        else:
            new_stop.prev = self.tail
            new_stop.next = self.head
            self.tail.next = new_stop
            self.head.prev = new_stop
            self.tail = new_stop
        
        self.size += 1

    def calculate_total_time(self) -> float:
        # Расчет времени полного круга маршрута
        if self.size == 0:
            return 0.0
            
        total_time = 0.0
        current = self.head
        for _ in range(self.size):
            total_time += current.time_to_next
            current = current.next
        return total_time

    def get_location_after_n_stops(self, start_stop_name: str, n: int) -> BusStop:
        # Определение, где будет автобус через N остановок. Обработка выхода за границы.
        if self.size == 0:
            raise ValueError("Маршрут пуст.")
        if n < 0:
            raise ValueError("Количество остановок (N) не может быть отрицательным.")

        # Находим стартовую остановку
        current = self.head
        found = False
        for _ in range(self.size):
            if current.name == start_stop_name:
                found = True
                break
            current = current.next
            
        if not found:
            raise ValueError(f"Остановка '{start_stop_name}' не найдена.")

        # Оптимизация для больших N, чтобы избежать лишних кругов
        steps = n % self.size
        for _ in range(steps):
            current = current.next
            
        return current

    def reverse_route(self):
        # Построение обратного маршрута. Разворачиваем указатели.
        if self.size <= 1:
            return

        old_times = {}
        curr = self.head
        for _ in range(self.size):
            old_times[curr] = curr.time_to_next
            curr = curr.next

        curr = self.head
        for _ in range(self.size):
            new_time = old_times[curr.prev]
            
            curr.next, curr.prev = curr.prev, curr.next
            curr.time_to_next = new_time
            
            curr = curr.prev

        # Обновляем голову и хвост
        self.head, self.tail = self.tail, self.head



# 3. СЛОЙ ВВОДА-ВЫВОДА

class RouteReportGenerator:
    # Класс для экспорта данных маршрута.
    @staticmethod
    def save_to_text_file(route: BusRoute, filename: str):
        with open(filename, 'w', encoding='utf-8') as f:
            if route.size == 0:
                f.write("Маршрут пуст. Нет данных для отчета.\n")
                return

            f.write("=" * 40 + "\n")
            f.write(" ОТЧЕТ ПО АВТОБУСНОМУ МАРШРУТУ \n")
            f.write("=" * 40 + "\n\n")
            f.write(f"Тип маршрута: Кольцевой\n")
            f.write(f"Всего остановок: {route.size}\n")
            f.write(f"Время полного круга: {route.calculate_total_time()} мин.\n\n")
            f.write("Детализация остановок:\n")
            f.write("-" * 40 + "\n")

            current = route.head
            for i in range(route.size):
                f.write(f"{i + 1}. {current.name}\n")
                f.write(f" Координаты: {current.coordinates}\n")
                f.write(f" Время до следующей: {current.time_to_next} мин.\n")
                f.write("-" * 40 + "\n")
                current = current.next


# Блок с тестами
if __name__ == "__main__":
    # Инициализация маршрута
    route = BusRoute()
    
    # 1. Добавление остановок
    route.add_stop("Университет", (55.75, 37.61), 5.0)
    route.add_stop("Библиотека", (55.76, 37.62), 7.0)
    route.add_stop("Студгородок", (55.77, 37.63), 10.0)
    route.add_stop("Метро", (55.78, 37.64), 8.0)
    
    # 2. Расчет общего времени
    print(f"Общее время круга: {route.calculate_total_time()} мин.")
    assert route.calculate_total_time() == 30.0

    # 3. Где будет автобус через N остановок
    stop_after = route.get_location_after_n_stops("Университет", 5)
    print(f"Через 5 остановок автобус будет на: {stop_after.name}")
    assert stop_after.name == "Библиотека"

    # 4. Построение отчета
    report_file = "bus_route_report.txt"
    RouteReportGenerator.save_to_text_file(route, report_file)
    print(f"Отчет успешно сохранен в файл '{report_file}'.")

    # 5. Разворот маршрута
    print("\nРазворачиваем маршрут...")
    route.reverse_route()
    
    print(f"Новая начальная остановка: {route.head.name}")
    assert route.head.name == "Метро"
    
    print(f"Следующая после Университета: {route.tail.next.name}")
    assert route.tail.next.name == "Метро"

    print(f"Следующая после Метро: {route.head.next.name}")
    assert route.head.next.name == "Студгородок"
    
    # Сохранение реверсивного отчёта
    RouteReportGenerator.save_to_text_file(route, "bus_route_report_reversed.txt")