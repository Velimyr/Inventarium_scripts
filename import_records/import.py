import csv

input_file = 'd:\\Repository\\Inventarium_scripts\\import_records\\Inventarium_import.csv'
output_file = 'd:\\Repository\\Inventarium_scripts\\import_records\\insert_records.sql'

# Поля, які мають бути числовими (без лапок)
numeric_fields = {'latitude', 'longitude', 'inventory_year','mark_type'}

with open(input_file, newline='', encoding='utf-8-sig') as csvfile, open(output_file, 'w', encoding='utf-8-sig') as sqlfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    rows = []
    columns = None

    for row in reader:
        if columns is None:
            columns = ', '.join(row.keys())

        values = []
        for k in row:
            val = row[k].strip()
            if val == '':
                values.append('NULL')
            elif k in numeric_fields:
                values.append(val)  # без лапок
            else:
                val = val.replace("'", "`")  # заміна одинарної лапки на бектик
                values.append(f"'{val}'")   # текстове значення в лапках

        rows.append('(' + ', '.join(values) + ')')

    if rows:
        sqlfile.write(f'INSERT INTO records ({columns})\nVALUES\n')
        sqlfile.write(',\n'.join(rows) + ';\n')
