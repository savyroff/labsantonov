#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Данные о студентах группы
Запуск: python mygroup.py
"""

groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Елена",
        "surname": "Козлова",
        "exams": ["Информатика", "АиГ", "Web"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Дмитрий",
        "surname": "Морозов",
        "exams": ["История", "ЭЭиС", "КТП"],
        "marks": [3, 3, 4]
    },
    {
        "name": "Анна",
        "surname": "Волкова",
        "exams": ["Философия", "ИС", "Web"],
        "marks": [5, 5, 4]
    },
    {
        "name": "Максим",
        "surname": "Соколов",
        "exams": ["Информатика", "История", "КТП"],
        "marks": [4, 4, 3]
    }
]

def calculate_average(marks):
    """Вычисляет средний балл студента"""
    return sum(marks) / len(marks)

def print_students(students):
    """Выводит информацию о всех студентах"""
    print("\n" + "=" * 80)
    print(u"Имя".ljust(15), u"Фамилия".ljust(15), u"Экзамены".ljust(35), u"Оценки".ljust(20), u"Ср. балл".ljust(10))
    print("-" * 95)
    for student in students:
        avg = calculate_average(student["marks"])
        print(student["name"].ljust(15), 
              student["surname"].ljust(15), 
              str(student["exams"]).ljust(35), 
              str(student["marks"]).ljust(20),
              f"{avg:.2f}".ljust(10))
    print("=" * 80)

def filter_students_by_average(students, threshold):
    """Фильтрует студентов по среднему баллу"""
    filtered = []
    for student in students:
        avg = calculate_average(student["marks"])
        if avg > threshold:
            filtered.append(student)
    return filtered

def main():
    print("\n" + "=" * 50)
    print("Информация о студентах группы")
    print("=" * 50)

    # Вывод всех студентов
    print_students(groupmates)

    # Фильтрация по среднему баллу
    try:
        threshold = float(input("\nВведите минимальный средний балл для фильтрации: "))
        filtered_students = filter_students_by_average(groupmates, threshold)

        if filtered_students:
            print(f"\nСтуденты со средним баллом выше {threshold}:")
            print_students(filtered_students)
        else:
            print(f"\nНет студентов со средним баллом выше {threshold}")
    except ValueError:
        print("\n✗ Ошибка: введите корректное число")

if __name__ == "__main__":
    main()
