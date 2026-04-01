import webbrowser
from abc import ABC, abstractmethod

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


class SourceGDZ(ABC):
    # Константы
    # Последние упражнения в гдз + 1, т.к range проверяет до значения(Не включительно)
    LAST_EXERCISES = {
        "GEOMETRY": 1432,  # 1431 в учебнике
        "RUSSIAN_OLD": 514,  # 513 в учебнике
        "RUSSIAN_NEW": 565,  # 564 в учебнике
    }

    # Базовые ссылки на гдз
    BASE_URLS = {
        "geometry": "https://gdz.top/7-klass/geometrija/atanasjan-fgos/",
        "pomogalka": "https://pomogalka.me/8-klass/russkij-yazyk/pichugov-eremeeva/uprazhnenie-{exercise}/",
        "reshak": "https://reshak.ru/otvet/reshebniki.php?otvet={exercise}&predmet=pichugov8",
    }

    @abstractmethod
    def open(self, exercise: str) -> None:
        pass

    @abstractmethod
    def is_valid(self, exercise: str):
        pass


class GeometryGDZ(SourceGDZ):
    # Проверка валидности номера, введенного пользователем
    def is_valid(self, exercise: str) -> bool:
        if exercise in range(1, SourceGDZ.LAST_EXERCISES["GEOMETRY"]):
            return True

        else:
            return False

    def open(self, exercise: str) -> None:
        webbrowser.open(f"{SourceGDZ.BASE_URLS['geometry']}{exercise}")


class RussianGDZ(SourceGDZ):
    # Проверка валидности номера, введенного пользователем
    def is_valid(self, exercise: str) -> bool:
        if int(exercise) in range(1, SourceGDZ.LAST_EXERCISES["RUSSIAN_OLD"]):
            return True

        else:
            return False

    def open(self, exercise: str, gdz: str) -> None:
        pomogalka = Pomogalka()
        reshak = Reshak()
        if gdz == "1":
            pomogalka.open(exercise)

        elif gdz == "2":
            reshak.open(exercise)


class Pomogalka(RussianGDZ):
    def open(self, exercise: str) -> None:
        webbrowser.open(SourceGDZ.BASE_URLS["pomogalka"].format(exercise=exercise))


class Reshak(RussianGDZ):
    # Парсит номер упражнения из решака
    def parse_num_of_exercise(exercise: str) -> str:

        headers = {"user-agent": UserAgent().random}
        URL = "https://reshak.ru/reshebniki/russkijazik/8/pechugov/index.html"
        response = requests.get(URL, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, "lxml")

        try:
            all_exercises = soup.find("div", class_="razdel").find_all("a")
            for ex in all_exercises:
                new_ex = ex.find(string=True).strip()
                old_ex = ex.find("span")

                if old_ex:
                    if old_ex.text.strip("()") == exercise:
                        return new_ex

        except requests.exceptions.RequestException as e:
            print(f"Произошла ошибка соединения {e}!")

        except AttributeError as e:
            print(f"Произошла ошибка {e}!")

    def open(self, exercise: str) -> None:
        ex = Reshak.parse_num_of_exercise(exercise)
        webbrowser.open(SourceGDZ.BASE_URLS["reshak"].format(exercise=ex))
