import csv

input_file = 'Inventarium_import.csv'
output_file = 'insert_records.sql'

with open(input_file, newline='', encoding='utf-8-sig') as csvfile, open(output_file, 'w', encoding='utf-8-sig') as sqlfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        columns = ', '.join(row.keys())
        values = []
        for k in row:
            val = row[k].strip()
            if val == '':
                values.append('NULL')
            else:
                val = val.replace("'", "''")  # екранування одинарних лапок
                values.append("'" + val + "'")
        sql_line = "INSERT INTO records (" + columns + ") VALUES (" + ', '.join(values) + ");\n"
        sqlfile.write(sql_line)