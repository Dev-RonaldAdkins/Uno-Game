import pandas as pd

#Load Excel file and specify the sheet name
file_path = "\\file002\data\RFQ's\CUSTOMER ACTIVE\Honeybee\Unknown Program\0923241HONEY - 8C3 PCBA Turnkey\PRICING TEMPLATE\2000890     PRICING     9.23.24 RA"
df = pd.read_excel(file_path)

#Select relevant columns
part_data = df[['MFR P/N', 'PRICE']]
print(part_data.head()) #check first few rows to ensure data loaded properly


