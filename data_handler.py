import csv
def load_file(file_name):
    data_output = []
    try:
        with open(file_name, mode='r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["age"] = int(row["age"])
                row["score"] = int(row["score"])
                data_output.append(row)
    except FileNotFoundError:
        print(f"There is no such file as {file_name}")
        return []
    return data_output

def filter_data(parameters, data):
    filter_output = []
    field = parameters[0]
    operator = parameters[1]
    criteria = parameters[2]
    if field not in data[0]:
        print(f'No such field as {field}')
    if operator == ">" :
        for row in data:
            try:
                if row[field] > int(criteria):
                    filter_output.append(row)
            except ValueError, TypeError:
                print("Invalid comparison")
                break
    elif operator == "<":
        for row in data:
            try:
                if row[field] < int(criteria):
                    filter_output.append(row)
            except ValueError, TypeError:
                print("Invalid comparison")
                break
    elif operator == "=":
        for row in data:
            if str(row[field]).lower() == criteria:
                filter_output.append(row)
    else:
        print(f"Invalid input, the operator {operator} is not valid.")
    return filter_output

def average_field(field, data):
    result = sum(row[field] for row in data) / len(data)
    return result