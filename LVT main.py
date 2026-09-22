import pandas as pd
import tkinter as tk
import geopandas as gpd

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
    pd.set_option("display.max_rows", None)
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
    
    soton_district = dataFrame[dataFrame["district"] == "SOUTHAMPTON"]
    soton_district = soton_district.head()
    print(soton_district)
    
    #results = dataFrame[dataFrame["county"] == county]
    #print(dataFrame.columns)
    #print(results[["price", "postcode", "street" ,"county"]])
    #print(results["price"].median())

    #head = dataFrame.head()
    #head = head.sort_values(by="price")
    #print(head)
    

def guiFunct():
    root = tk.Tk()
    root.title("Land Value Tax Calculator")

    tk.Label(root, text="Enter property details and click search!").grid(row=0, column=0)

    tk.Label(root, text="Post Code:").grid(row=1, column=0)
    tk.Label(root, text="Region: ").grid(row=2, column=0)
    #tk.Label(root, text=)

    pc_entry = tk.Entry(root)
    county_entry = tk.Entry(root)

    pc_entry.grid(row=1, column=1)
    county_entry.grid(row=2, column=1)
    
    button = tk.Button(root, text="Search...", width=25, command=lambda: csvQuery(pc_entry.get(), county_entry.get()) ).grid(row=3)

    root.mainloop()



def glsTesting():
    properties = gpd.read_file("Land_Registry_Cadastral_Parcels.gml")
    #properties.set_option("display.max_rows", None)
    #print(properties.head())
    #print(properties.columns)
    #print(properties.crs)
    #print(properties[["INSPIREID", "LABEL", "NATIONALCADASTRALREFERENCE"]].head(10).to_string(index=False))
    #print("Rows:", len(properties))
    #print("Unique INSPIRE IDs:", properties["INSPIREID"].nunique())
    #print("Duplicate IDs:", properties["INSPIREID"].duplicated().sum())
    #print(properties["INSPIREID"].dtype)
    
    #properties["area_m2"] = properties.geometry.area
    #print(properties["area_m2"].describe())
    #print(properties["area_m2"].quantile([0.01, 0.05, 0.10, 0.25, 0.50, 0.75, 0.90, 0.95, 0.99]))

    #print(f"Median: {properties['area_m2'].median():,.2f} m²")





    

#glsTesting()
guiFunct()





#print(dataFrame.head())


