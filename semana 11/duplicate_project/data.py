import csv
from actions import Student
def save_data_as_csv_file(file_path, data, headers):
    with open(file_path, "w", encoding="utf-8") as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)


def import_csv_file(file_path):
    objects_list = []

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            new_object = Student(
                student_name = row["student_name"],
                student_grade = row["student_grade"],
                spanish_score = int(row["spanish_score"]),
                english_score = int(row["english_score"]),
                history_score = int(row["history_score"]),
                science_score = int(row["science_score"]),
                average_score = float(row["average_score"])
            )
            objects_list.append(new_object)
        return objects_list