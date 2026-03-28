import webbrowser
import requests

from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# Последние упражнения в гдз + 1, т.к range проверяет до значения(Не включительно)
LAST_EXERCISES = {
    "GEOMETRY": 1432,  # 1431 в учебнике
    "RUSSIAN_OLD": 514,  # 513 в учебнике
    "RUSSIAN_NEW": 565,  # 564 в учебнике
}

# Базовые ссылки на гдз
BASE_URLS = {
    "geometry": "https://gdz.top/7-klass/geometrija/atanasjan-fgos/",
    "pomogalka": "https://pomogalka.me/8-klass/russkij-yazyk/pichugov-eremeeva/uprazhnenie-{ex}/",
    "reshak": "https://reshak.ru/otvet/reshebniki.php?otvet={ex}&predmet=pichugov8",
}


def open_geometry_gdz(user_ex):
    if int(user_ex) in range(1, LAST_EXERCISES["GEOMETRY"]):
        webbrowser.open(BASE_URLS["geometry"] + user_ex)

    else:
        print("Вы ввели неверный номер!")


def open_russian_gdz(user_ex):

    gdz_rus = input("Выберите предмет: 1[Pomogalka]  2[Reshak]:  ").strip()

    if gdz_rus == "1":
        open_pomogalka(user_ex)

    elif gdz_rus == "2":
        open_reshak(user_ex)

    else:
        print("Неверно выбран гдз!")


def open_pomogalka(user_ex):
    if int(user_ex) in range(1, LAST_EXERCISES["RUSSIAN_NEW"]):
        webbrowser.open(BASE_URLS["pomogalka"].format(ex=user_ex))


def open_reshak(
    user_ex,
):
    student_book = input("Выберите версию учебника: 1[старый]  2[новый]:  ")
    headers = {"user-agent": UserAgent().random}

    URL = "https://reshak.ru/reshebniki/russkijazik/8/pechugov/index.html"
    response = requests.get(URL, headers=headers, timeout=15)
    soup = BeautifulSoup(response.text, "lxml")

    try:
        if student_book == "1" and int(user_ex) in range(
            1, LAST_EXERCISES["RUSSIAN_OLD"]
        ):
            all_exercises = soup.find("div", class_="razdel").find_all("a")
            for exercise in all_exercises:
                ex = exercise.find(string=True).strip()
                old_ex = exercise.find("span")

                if old_ex:
                    if old_ex.text.strip("()") == user_ex:
                        webbrowser.open(BASE_URLS["reshak"].format(ex=ex))

        elif student_book == "2" and int(user_ex) in range(
            1, LAST_EXERCISES["RUSSIAN_NEW"]
        ):
            all_exercises = soup.find("div", class_="razdel").find_all("a")
            for exercise in all_exercises:
                ex = exercise.find(string=True).strip()

                if ex == user_ex:
                    webbrowser.open(BASE_URLS["reshak"].format(ex=ex))

        else:
            print("Вы выбрали неверную версию учебника!")

    except requests.exceptions.RequestException as e:
        print(f"Произошла ошибка соединения {e}!")
    except AttributeError as e:
        print(f"Произошла ошибка {e}!")


def main():

    user_inputted_exercise = input("Введите упражнение: ").strip()
    subject = input("Введите предмет: 1[Геометрия]  2[Русский]:  ").strip()

    # Выбираем предмет и проверяем есть ли упражнение, введенное пользователем в гдз

    if subject == "1":
        open_geometry_gdz(user_inputted_exercise)

    elif subject == "2":
        open_russian_gdz(user_inputted_exercise)

    else:
        print("Неверно выбран предмет")


if __name__ == "__main__":
    print("ЧТОБЫ ВЫЙТИ CTRL + C")
    try:
        main()
    except KeyboardInterrupt:
        print("Выход...")
