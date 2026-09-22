import pandas as pd
import tkinter as tk

#print(panda.__version__)

"""
Plan:
1) GUI FUNCTION
2) CSV HANDLING FUNCTION
3) LVT CALCULATION FUNCTION
"""

def csvQuery(postcode, county):
    print("Querying...")
    print(postcode + "," + county)
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
    

def guiFunct():
    root = tk.Tk()
    root.title("Land Value Tax Calculator")

    tk.Label(root, text="Enter property details and click search!").grid(row=0, column=0)

    tk.Label(root, text="Post Code:").grid(row=1, column=0)
    tk.Label(root, text="Region: ").grid(row=2, column=0)

    pc_entry = tk.Entry(root)
    county_entry = tk.Entry(root)

    pc_entry.grid(row=1, column=1)
    county_entry.grid(row=2, column=1)
    
    button = tk.Button(root, text="Search...", width=25, command=lambda: csvQuery(pc_entry.get(), county_entry.get()) ).grid(row=3)

    root.mainloop()




guiFunct()





#print(dataFrame.head())


