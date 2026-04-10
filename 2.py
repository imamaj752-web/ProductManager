def calculate_average_grades(grades_dict):
    averag_grades = {}
    for student, scores in grades_dict.items():
        averag_grades[student] = sum(scores) / len(scores)
    return averag_grades
grades = {
    'Alice': [100, 90, 80],
    'Bob': [60, 70, 80],
    'Charlie': [80, 80, 80],
    'Dave': [70, 70, 70],
    'Eve': [60, 60, 60],
    'Frank': [50, 50, 50],
    'Gina': [40, 40, 40],
    'Hannah': [30, 30, 30],
    'Igor': [20, 20, 20],
    'Jenny': [10, 10, 10]
}
result = calculate_average_grades(grades)
print(result)
""TASK2""
def count_digits(digits_string):
    digft_counts = {}
    for char in digits_string:
        digit = int(char)
        digft_counts[digit] = digft_counts.get(digit, 0) + 1
    return digft_counts