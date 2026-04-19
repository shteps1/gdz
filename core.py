import webbrowser
from abc import ABC, abstractmethod

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


class SourceGDZ(ABC):
    # Константы
    # !Последние упражнения в гдз + 1, т.к range() проверяет до значения т.е Не включительно!
    LAST_EXERCISES = {
        "ALGEBRA": 1341,  # 1340 в учебнике
        "GEOMETRY": 1432,  # 1431 в учебнике
        "RUSSIAN_OLD": 514,  # 513 в учебнике
        "RUSSIAN_NEW": 565,  # 564 в учебнике
    }

    # Базовые ссылки на гдз
    BASE_URLS = {
        "ALGEBRA": "https://gdz.ru/class-8/algebra/makarychev-8/{exercise}-nom/",
        "GEOMETRY": "https://gdz.top/7-klass/geometrija/atanasjan-fgos/{exercise}",
        "POMOGALKA": "https://pomogalka.me/8-klass/russkij-yazyk/pichugov-eremeeva/uprazhnenie-{exercise}/",
        "RESHAK": "https://reshak.ru/otvet/reshebniki.php?otvet={exercise}&predmet=pichugov8",
    }

    @abstractmethod
    def get_link(self, exercise: str) -> None:
        pass

    
    def open(self, exercise: str) -> None:
        webbrowser.open(self.get_link(exercise))

    # Проверка валидности номера, введенного пользователем
    # @abstractmethod
    @staticmethod
    def is_valid(exercise: str, subject: str) -> bool:
        if subject == "1":
            return int(exercise) in range(1, SourceGDZ.LAST_EXERCISES["GEOMETRY"])

        elif subject == "2":
            return int(exercise) in range(1, SourceGDZ.LAST_EXERCISES["RUSSIAN_OLD"])

        elif subject == "3":
            return int(exercise) in range(1, SourceGDZ.LAST_EXERCISES["ALGEBRA"])

        else:
            return False


class GeometryGDZ(SourceGDZ):
    def get_link(self, exercise: str) -> None:
        link = self.BASE_URLS["GEOMETRY"].format(exercise=exercise)
        return link


class AlgebraGDZ(SourceGDZ):
    def get_link(self, exercise: str) -> None:
        link = self.BASE_URLS["ALGEBRA"].format(exercise=exercise)
        return link


class PomogalkaGDZ(SourceGDZ):
    def get_link(self, exercise: str) -> None:
        link = self.BASE_URLS["POMOGALKA"].format(exercise=exercise)
        return link


class ReshakGDZ(SourceGDZ):
    # Парсит номер упражнения из решака
    @staticmethod
    def parse_num_of_exercise(exercise: str) -> str | None:
        try:
            headers = {"user-agent": UserAgent().random}
            URL = "https://reshak.ru/reshebniki/russkijazik/8/pechugov/index.html"
            response = requests.get(URL, headers=headers, timeout=15)
            soup = BeautifulSoup(response.text, "lxml")

            all_exercises = soup.find("div", class_="razdel").find_all("a")
            for ex in all_exercises:
                new_ex = ex.find(string=True).strip()
                old_ex = ex.find("span")

                if old_ex and old_ex.text.strip("()") == exercise:
                    return new_ex

        except requests.exceptions.RequestException as e:
            print(f"Произошла ошибка соединения {e}!")

        except AttributeError as e:
            print(f"Ошибка парсинга {e}!")

    def get_link(self, exercise: str) -> None:
        ex = self.parse_num_of_exercise(exercise)
        link = self.BASE_URLS["RESHAK"].format(exercise=ex)
        return link
