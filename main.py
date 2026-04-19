from core import GeometryGDZ, AlgebraGDZ, PomogalkaGDZ, ReshakGDZ, SourceGDZ


def main():
    exercise = input("Номер задания: ")
    subject = input("1[Геометрия] 2[Русский язык] 3[Алгебра]: ")

    # Проверка валидности номера, введенного пользователем
    exercise_validation = SourceGDZ.is_valid(exercise, subject)

    if subject == "1" and exercise_validation:
        geometry_gdz = GeometryGDZ()
        print(geometry_gdz.get_link(exercise))
        
        geometry_gdz.open(exercise)

    elif subject == "2" and exercise_validation:
        gdz = input("1[Помогалка] 2[Решак]: ")

        if gdz == "1":
            pomogalka_gdz = PomogalkaGDZ()
            print(pomogalka_gdz.get_link(exercise))
            
            pomogalka_gdz.open(exercise)

        elif gdz == "2":
            reshak_gdz = ReshakGDZ()
            print(reshak_gdz.get_link(exercise))
            
            reshak_gdz.open(exercise)

        else:
            print("Неверно выбрано гдз!")

    elif subject == "3" and exercise_validation:
        algebra_gdz = AlgebraGDZ()
        print(algebra_gdz.get_link(exercise))
        
        algebra_gdz.open(exercise)

    else:
        print("Выбран неправильный предмет или Неверно введен номер задания!")


if __name__ == "__main__":
    main()
