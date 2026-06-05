import random
import string


class URLShortener:
    def __init__(self):
        self.links = {}
        self.clicks = {}

    def generate_code(self, length=4):
        while True:
            code = ''.join(
                random.choices(
                    string.ascii_letters + string.digits,
                    k=length
                )
            )

            if code not in self.links:
                return code

    def add_link(self, long_url):
        code = self.generate_code()
        self.links[code] = long_url
        self.clicks[code] = 0
        return code

    def get_link(self, code):
        if code in self.links:
            self.clicks[code] += 1
            return self.links[code]
        return None

    def exists(self, code):
        return code in self.links

    def get_all_links(self):
        return self.links

    def get_clicks(self, code):
        return self.clicks.get(code, 0)


def main():
    shortener = URLShortener()

    while True:
        print("\n1. Добавить ссылку")
        print("2. Получить ссылку по коду")
        print("3. Проверить код")
        print("4. Показать все ссылки")
        print("5. Показать статистику")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            url = input("Введите длинную ссылку: ")
            code = shortener.add_link(url)
            print(f"Короткий код: {code}")

        elif choice == "2":
            code = input("Введите код: ")
            url = shortener.get_link(code)

            if url:
                print("Ссылка:", url)
            else:
                print("Код не найден")

        elif choice == "3":
            code = input("Введите код: ")

            if shortener.exists(code):
                print("Код существует")
            else:
                print("Код не найден")

        elif choice == "4":
            links = shortener.get_all_links()

            if not links:
                print("Ссылок нет")
            else:
                for code, url in links.items():
                    print(f"{code} -> {url}")

        elif choice == "5":
            for code in shortener.links:
                print(
                    f"{code}: "
                    f"{shortener.get_clicks(code)} переходов"
                )

        elif choice == "0":
            break

        else:
            print("Неверный пункт меню")


if __name__ == "__main__":
    main()