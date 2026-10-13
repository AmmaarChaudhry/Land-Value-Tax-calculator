import pandas as pd
import tkinter as tk
import geopandas as gpd
import numpy as np
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
    print(f"The median price per sqm is: £{price_per_sqm.round()}")
    land_value_per_sqm = price_per_sqm * 0.3
    print(f"The land value per sqm is: £{land_value_per_sqm.round()}")

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



    
def areaDesirability(district_council):
    IMDlowerDF = pd.read_excel(
        "File_10_-_IoD2025_Local_Authority_District_Summaries__lower-tier__v2.xlsx",
        sheet_name="IMD"
    )

    score_col = "IMD - Average score "
    council_col = "Local Authority District name (2024)"

    # Ensure IMD scores are numeric
    IMDlowerDF[score_col] = pd.to_numeric(
        IMDlowerDF[score_col], errors="coerce"
    )

    # Calculate mean and standard deviation across all councils
    mean_score = IMDlowerDF[score_col].mean()
    std_score = IMDlowerDF[score_col].std()

    # Calculate standardised desirability:
    # Reverse the sign because lower deprivation = higher desirability
    IMDlowerDF["desirability"] = -(
        (IMDlowerDF[score_col] - mean_score) / std_score
    )

    # Find the requested council
    matches = IMDlowerDF[
        IMDlowerDF[council_col].str.strip().str.casefold()
        == district_council.strip().casefold()
    ]

    if matches.empty:
        print(f"No results found for district council: {district_council}")
        return None

    return float(matches.iloc[0]["desirability"])


def areaDensity(district_council):
    populationDF = pd.read_csv("population-density-table.csv")

    #convert periods to dates so the latest record is selected correctly
    populationDF["period"] = pd.to_datetime(populationDF["period"])
    populationDF["value"] = pd.to_numeric(
        populationDF["value"], errors="coerce"
    )

    # Keep latest record for each local authority
    latestDF = (
        populationDF
        .sort_values("period")
        .drop_duplicates(subset="areanm", keep="last")
    )

    #calculate the overall median density
    median_density = latestDF["value"].median()

    #finds row for specified local authority
    matches = latestDF[latestDF["areanm"] == district_council]

    if matches.empty:
        print(f"No results found for district council: {district_council}")
        population_density = None
    else:
        population_density = matches.iloc[0]["value"]

    return int(population_density), float(median_density)

#guiFunct()

def landValueConst(district_council):
    
    #di is the density const
    #dmed is the avg density const for all LLAs
    #desirability is the area desirability score
    #clipped_land_const is the land vale constant (* it with price_per_sqm to get land val per sqm) and has been clipped
    di , dmed = areaDensity(district_council)
    desirability = areaDesirability(district_council) * 0.1
    
    if di is None or dmed is None or desirability is None:
        return None
    if di <= 0 or dmed <= 0:
        return None
    
    
    density_ratio = di / dmed
    ln_density_ratio = 0.05 * np.log(density_ratio)
    ln_density_plus_desirability = ln_density_ratio + desirability
    
    land_const = np.exp(ln_density_plus_desirability) *0.4
    clipped_land_const = np.clip(land_const,0.15,0.7)
    
    return clipped_land_const


density, median_density = areaDensity("Southampton")

print(f"Southampton density: {density}")
print(f"Median density: {median_density}")

score = areaDesirability("Southampton")
print(f"Southampton desirability score: {score:.3f}")

land_val_test = landValueConst("Southampton")
print(f"Soton land val const: {land_val_test}")