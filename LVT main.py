import pandas as pd

#print(panda.__version__)

"""
asd
"""
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


