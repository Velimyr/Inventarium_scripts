import csv
import json
from collections import defaultdict

csv_file_path = 'ua-admin-map.csv'
output_json_path = 'nested_structure_final.json'

def tree():
    return defaultdict(tree)

data_tree = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))

with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        oblast = row['oblast_name'].strip()
        raion = row['raion_name'].strip()
        hromada = row['hromada_name'].strip()

        settlement_name = row['settlement_name'].strip()
        settlement_code = row['settlement_code'].strip()
        settlement_type = row['settlement_type'].strip()

        coord_str = row['map_position'].strip() or row['map_position2'].strip()
        if coord_str and ',' in coord_str:
            try:
                lat_str, lon_str = coord_str.split(',')
                lat = float(lat_str.strip())
                lon = float(lon_str.strip())
            except ValueError:
                lat = lon = None
        else:
            lat = lon = None

        settlement_obj = {
            "name": settlement_name,
            "code": settlement_code,
            "type": settlement_type,
            "lat": lat,
            "lon": lon
        }

        # Тепер це список, можна просто додавати, перевіряючи дублікати
        settlements_list = data_tree[oblast][raion][hromada]
        if not any(s["code"] == settlement_code for s in settlements_list):
            settlements_list.append(settlement_obj)

# Перетворення defaultdict → dict
def convert(d):
    if isinstance(d, defaultdict):
        return {k: convert(v) for k, v in d.items()}
    return d

with open(output_json_path, 'w', encoding='utf-8') as jsonfile:
    json.dump(convert(data_tree), jsonfile, ensure_ascii=False, indent=2)

print(f'✅ JSON збережено як {output_json_path}')
