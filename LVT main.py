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
    
def csvDistrictQuery(district):
    print("Querying...")
    print("")
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
    district_data = dataFrame[dataFrame["district"] == district]
    print(district_data["price"].median())
    district_price_median = district_data["price"].median()
    median_district_plot = glsTesting()
    price_per_sqm = district_price_median / median_district_plot
    print(f"The median price per sqm is: {price_per_sqm.round()}")

def guiFunct():
    root = tk.Tk()
    root.title("Land Value Tax Calculator")
    tk.Label(root, text="Enter property details and click search!").grid(row=0, column=0) 
    tk.Label(root, text="District/LLA name").grid(row=1, column=0)
    district_entry = tk.Entry(root)
    district_entry.grid(row=1,column=1)
    button = tk.Button(root, text="Search...", width=25, command=lambda: csvDistrictQuery(district_entry.get().upper()) ).grid(row=3)
    root.mainloop()



def glsTesting():
    properties = gpd.read_file("Land_Registry_Cadastral_Parcels.gml")
    properties["area_m2"] = properties.geometry.area
    #print(f"Median: {properties['area_m2'].median():,.2f} m²")
    print(properties["area_m2"].median().round())
    median_polygon_area = properties["area_m2"].median().round()
    return median_polygon_area





    

guiFunct()