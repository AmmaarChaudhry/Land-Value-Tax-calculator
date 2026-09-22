import pandas as pd
import tkinter as tk

#print(panda.__version__)

"""
Plan:
1) GUI FUNCTION
2) CSV HANDLING FUNCTION
3) LVT CALCULATION FUNCTION
"""
def guiFunct():
    root = tk.Tk()
    root.title("Land Value Tax Calculator")

    tk.Label(root, text="Enter property details and click search!").grid(row=0, column=0)

    tk.Label(root, text="Post Code:").grid(row=1, column=0)
    tk.Label(root, text="Region: ").grid(row=2, column=0)

    button = tk.Button(root, text="Search...", width=25).grid(row=3)

    entry1 = tk.Entry(root)
    entry2 = tk.Entry(root)

    entry1.grid(row=1, column=1)
    entry2.grid(row=2, column=1)


    root.mainloop()



pd.set_option("display.max_columns", None)


dataFrame = pd.read_csv("pp-2025.csv", header=None)

columns = [
    "transaction_id",
    "price",
    "date",
    "postcode",
    "property_type",
    "new_build",
    "duration",
    "paon",
    "saon",
    "street",
    "locality",
    "town_city",
    "district",
    "county",
    "ppd_category",
    "record_status"
]

dataFrame.columns = columns

head = dataFrame.head()

head = head.sort_values(by="price")

print(head)

#print(dataFrame.head())


