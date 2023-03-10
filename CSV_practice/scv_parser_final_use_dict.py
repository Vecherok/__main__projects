import csv

with open('common_pricelist.csv', 'r', newline='', encoding='windows-1251') as provider:
    reader_provider = csv.DictReader(provider, delimiter=';')
    fieldnames = reader_provider.fieldnames

    with open('export-products-09-03-23_13-16-14.csv', 'r', newline='', encoding="UTF-8") as myne:
        # reader_myne = csv.DictReader(myne)
        csv_myne = [x for x in myne.readlines()]

        with open('test.csv', 'w+', newline='', encoding="UTF-8") as newfile:
            writer = csv.DictWriter(newfile, fieldnames=fieldnames, extrasaction='ignore')
            writer.writeheader()

            for line_provider in reader_provider:
                name_provider = line_provider['Наименование'].strip()
                for line_myne in csv_myne:
                    if name_provider in line_myne:
                        writer.writerow(line_provider) 


