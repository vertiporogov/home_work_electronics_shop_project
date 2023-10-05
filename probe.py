import csv
ggg = []
with open('src/items.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        ggg.append(row)

    print(ggg)