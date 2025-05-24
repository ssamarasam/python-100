# working with csv files

import csv

# with open("data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["transaction_id", "product_id", "value"])
#     writer.writerow([1212, 18, 5])
#     writer.writerow([1213, 205, 83])

with open("data.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
