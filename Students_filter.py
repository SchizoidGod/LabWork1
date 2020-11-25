groupmates = [
  {
    "name": "Тимофей",
    "surname" : "Белов",
    "exams": "['Математика', 'Информатика','История']",
    "marks": [4, 3, 5]
  },
  {
    "name": "Павел",
    "surname" : "Шакуров",
    "exams": "['Математика', 'Информатика','История']",
    "marks": [3, 2, 3]
  },
  {
    "name": "Тимур",
    "surname" : "Асланов",
    "exams": "['Математика', 'Информатика','История']",
    "marks": [3, 5, 4]
  },
  {
    "name": "Дарья",
    "surname" : "Летова",
    "exams": "['Математика', 'Информатика','История']",
    "marks": [5, 5, 5]
  }
]

def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10),
u"Экзамены".ljust(40), u"Оценки".ljust(10))
    for student in students:
        print(student["name"].ljust(15),
student["surname"].ljust(10), str(student["exams"]).ljust(30),
str(student["marks"]).ljust(20))
print_students(groupmates)
