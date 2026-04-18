from core import GeometryGDZ, AlgebraGDZ, PomogalkaGDZ, ReshakGDZ, SourceGDZ


def main():
    exercise = input("Введите номер задание: ")
    subject = input("Выберите предмет 1[Геометрия] 2[Русский язык] 3[Алгебра]: ")

    # Проверка валидности номера, введенного пользователем
    exercise_validation = SourceGDZ.is_valid(exercise, subject)

    if subject == "1" and exercise_validation:
        geometry_gdz = GeometryGDZ()
        geometry_gdz.open(exercise=exercise)

    elif subject == "2" and exercise_validation:
        gdz = input("Выберите гдз 1[Помогалка] 2[Решак]: ")

        if gdz == "1":
            pomogalka = PomogalkaGDZ()
            pomogalka.open(exercise)

        elif gdz == "2":
            reshak = ReshakGDZ()
            reshak.open(exercise)

        else:
            print("Неверно выбрано гдз!")

    elif subject == "1" and exercise_validation:
        algebra_gdz = AlgebraGDZ()
        algebra_gdz.open(exercise=exercise)

    else:
        print("Выбран неправильный предмет или Неверно введен номер задания!")


if __name__ == "__main__":
    main()
