import csv
def load_file(file_name):
    try:
        with open(file_name, mode='r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            data = list(reader)
            return data
    except FileNotFoundError:
        print(f"There is no such file as {file_name}")

print(load_file("sample_data.csv"))