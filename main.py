from base import GeometryGDZ, RussianGDZ


def main():
    exercise = int(input("Введите номер задание: "))
    subject = int(input("Выберите предмет 1[Геометрия] 2[Русский язык]: "))
    gdz = int(input("Выберите гдз 1[Помогалка] 2[Решак]: "))
    
    geometry_gdz = GeometryGDZ()
    russian_gdz = RussianGDZ()
    
    # Проверка валидности номера, введенного пользователем
    geometry_exercise_validation = geometry_gdz.is_valid(exercise)
    russian_exercise_validation = russian_gdz.is_valid(exercise)

    if subject == 1 and geometry_exercise_validation:
        geometry_gdz.open(exercise=exercise)

    elif subject == 2 and russian_exercise_validation:
        russian_gdz.open(exercise=exercise, gdz=gdz)

    else:
        print("Выбран неправильный предмет или Неверно введен номер задания")


if __name__ == "__main__":
    main()
