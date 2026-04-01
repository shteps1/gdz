import webbrowser
from abc import ABC, abstractmethod


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
        "reshak": "https://reshak.ru/otvet/reshebniki.php?otvet={ex}&predmet=pichugov8",
    }

    # def __init__(self, subject: int, exercise: int, student_book_version: int, gdz: int) -> None:
    #     self.subject = subject
    #     self.exercise = exercise
    #     self.student_book_version = student_book_version
    #     self.gdz = gdz

    @abstractmethod
    def open(self, exercise: int) -> None:
        pass

    @abstractmethod
    def is_valid(self, exercise: int):
        pass


class GeometryGDZ(SourceGDZ):
    # Проверка валидности номера, введенного пользователем
    def is_valid(self, exercise: int) -> bool:
        if exercise in range(1, SourceGDZ.LAST_EXERCISES["GEOMETRY"]):
            return True
            
        else: 
            return False
        
    def open(self, exercise: int) -> None:
        webbrowser.open(f"{SourceGDZ.BASE_URLS['geometry']}{exercise}")


class RussianGDZ(SourceGDZ):
    # Проверка валидности номера, введенного пользователем
    def is_valid(self, exercise: int) -> bool:
        if exercise in range(1, SourceGDZ.LAST_EXERCISES["RUSSIAN_OLD"]):
            return True
            
        else: 
            return False
            
    def open(self, exercise: int, gdz: int) -> None:
        pomogalka = Pomogalka()
        reshak = Reshak()
        if gdz == 1:
            pomogalka.open(exercise)
            
        elif gdz == 2:
            reshak.open(exercise)

    # def choose(self) -> bool:
    #     student_book_version = input("Выберите версию учебника 1[Старый] 2[Новый]: ")
    #     gdz = input("Выберите гдз 1[] 2[]: ")


class Pomogalka(RussianGDZ):
    def open(self, exercise: int):
        webbrowser.open(SourceGDZ.BASE_URLS["pomogalka"].format(exercise=exercise))
        
class Reshak(RussianGDZ):
    def open(self, exercise: int):
        webbrowser.open(SourceGDZ.BASE_URLS["reshak"].format(exercise=exercise))
