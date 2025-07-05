import csv
from collections import defaultdict

input_file = 'Inventarium_import.csv'

# Поля, що формують унікальність
unique_fields = [
    'current_region',
    'current_district',
    'current_community',
    'current_settlement_type',
    'current_settlement_name',
    'case_signature',
    'inventory_year'
]

seen = defaultdict(list)

with open(input_file, newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')

    for i, row in enumerate(reader, start=2):  # стартуємо з 2 — бо є заголовок
        key = tuple(
            row[field].strip().lower() if row[field] else '' for field in unique_fields
        )
        seen[key].append(i)  # зберігаємо номер рядка

# Виводимо дублікати
for key, lines in seen.items():
    if len(lines) > 1:
        print(f"❗ Дублікат запису у рядках: {lines}")
        print(f"   Значення: {key}")