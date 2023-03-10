import csv
# import pandas as pd
# from numpy import array_split as ArSp

with open('export-products-09-03-23_13-16-14.csv', 'r', newline='', encoding="windows-1251") as myne:
    csv_myne = [x.split('\n') for x in myne.readlines()]


with open('common_pricelist.csv', 'r', newline='', encoding='windows-1251') as provider:
    csv_provider =[x.split("\n") for x in provider.readlines()]
    # reader_provider = csv.reader(provider)

with open('test.csv', 'w+', newline='', encoding="UTF-8") as newfile:
    writer = csv.writer(newfile)
    # [writer.writerow(csv_provider) for x in csv_provider if x == 0]

        # reader_myne = csv.reader(myne)
    for elem_myne in csv_myne:
        
        if len(str(elem_myne)) > 10:
            name_elem_myne = str(elem_myne[0].split(";")[1])
            for elem_provider in csv_provider:
            
                # print(csv_provider)
                if name_elem_myne in str(elem_provider) and len(name_elem_myne) > 15:
                    writer.writerow((elem_provider[0]).split(';'))
                    print(elem_provider[0].split(';'))
                    print(repr(name_elem_myne))
            # if elem_prov.find(elem_myne) != -1:
            #     print(name_elem_myne)
            # print(name_myne)        


