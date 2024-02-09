import csv

def etn(column):
    result = 0
    for char in column:
        result = result * 26 + (ord(char.upper()) - ord('A') + 1)
    return result-1

def find_column_difference(csv_file):
    a= etn('CP')
    b= etn('DS')
    differences = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        line_number = 1
        for row in reader:
            try:
                if row[a] == row[b] and row[b] and row[a]=='Y':
                    differences.append((line_number, row[a], row[b]))
            except (ValueError, IndexError):
                print(f"Issue parsing line {line_number}: {row}")
            if line_number == 1:
                print((row[a],row[b]))
            line_number += 1
    return differences

csv_file_path = "sample.csv"  # Provide the path to your CSV file
differences = find_column_difference(csv_file_path)

# for diff in differences:
#     print(f"Difference found at line {diff[0]}: Column 5 = {diff[1]}, Column 6 = {diff[2]}")
print(differences)