from functools import reduce
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
grades = [85, 92, 78, 90, 88]
"TASK1"
students = list(map(lambda name, grade: (name, grade), names, grades))
print("После обеденения:", students)
"TASK2"
students = list(map(lambda name, grade: (name, grade), names, grades))
students_sorted = sorted(students, key=lambda x: x[1], reverse=True)
print("После сортировки:", students_sorted)
"TASK3"
total = reduce(lambda a, b: a + b, grades)
average = total / len(grades)
print("Середній бал:", average)
"TASK4"
below_avg = list(filter(lambda s: s[1] < average, students_sorted))
above_avg = list(filter(lambda s: s[1] >= average, students_sorted))
print("Меньше среднього:", below_avg)
print("Выще или средне:", above_avg)
"TASK5"
min_student = min(students, key=lambda x: x[1])
max_student = max(students, key=lambda x: x[1])
print("Самий маленький бал:", min_student)
print("Самый большой бал:", max_student)