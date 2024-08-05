import csv

def save_data_as_csv_file(file_path, data, headers):
    with open(file_path, "w", encoding="utf-8") as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)


def import_csv_file(file_path):
    row_lines = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["spanish"] = int(row["spanish"])
            row["english"] = int(row["english"])
            row["history"] = int(row["history"])
            row["science"] = int(row["science"])
            row["average"] = float(row["average"])
            row_lines.append(row)
        return row_lines