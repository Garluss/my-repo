import pandas as pd
import csv

file = "ecommerce_sales.csv"

data_original = pd.read_csv(file)
data = data_original


# Correct Category for product sorter
# product_categories = {"T-shirt":"Clothing","Doll":"Toys","Laptop":"Electronics","Blender":"Home Goods","Smartphone":"Electronics","Fiction Book":"Books","Non-Fiction Book":"Books"}
# r = 0
# for i in data["Product"]:
#     if i in product_categories:
#         data.loc[r, "ProductCategory"] = product_categories[i]
#     r += 1

# data.to_csv("sales_sorted.csv", encoding='utf-8', index=False, header=True)

while True:
    print("Filter by date.")
    y = input("Enter year: ")
    if len(y) < 3:
        if int(y) > 25:
            y = "19" + y
        else:
            y = "20" + y
    m = input("Enter month: ")
    if len(m) < 2:
        m = "0" + m
    d = input("Enter day: ")
    if len(d) < 2:
        d = "0" + d
    date = y + "-" + m + "-" + d
    entries = data.loc[data["OrderDate"] == date]
    if entries.empty:
        print("No entries found.")
    else:
        print(entries)