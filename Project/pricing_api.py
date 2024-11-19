import pandas as pd
import requests


#Load Excel file and specify the sheet name
file_path = "\\file002\data\RFQ's\CUSTOMER ACTIVE\Honeybee\Unknown Program\0923241HONEY - 8C3 PCBA Turnkey\PRICING TEMPLATE\2000890     PRICING     9.23.24 RA"
df = pd.read_excel(file_path)

#Select relevant columns
part_data = df[['MFR P/N', 'PRICE']]
print(part_data.head()) #check first few rows to ensure data loaded properly

def get_price_from_api(part_number):
    api_url= f'https://api.octopart.com/v3/parts/match'
    api_key = """eyJhbGciOiJSUzI1NiIsImtpZCI6IjA5NzI5QTkyRDU0RDlERjIyRDQzMENBMjNDNkI4QjJFIiwidHlwIjoiYXQrand0In0.
    eyJuYmYiOjE3MzA3MzI0ODQsImV4cCI6MTczMDgxODg4NCwiaXNzIjoiaHR0cHM6Ly9pZGVudGl0eS5uZXhhci5jb20iLCJjbGllbnRfaWQiOi
    IwMDkwMDQ2Yi1jMTM1LTQ3MDYtOTk1Yi1mZGQ3MjIwNzgzNzciLCJzdWIiOiJBMjUwMTA2Ri04QzEwLTQ4QjItODlEOC1BMzVBREZBODlFMDgiL
    CJhdXRoX3RpbWUiOjE3MzA3MzIxMDYsImlkcCI6Ikdvb2dsZSIsInByaXZhdGVfY2xhaW1zX2lkIjoiZmU5MDYxZDAtOGY5ZC00MjA5LWIxOWUtNzBmNzFmYz
    E0NWIwIiwicHJpdmF0ZV9jbGFpbXNfc2VjcmV0IjoiSzFZUXFBRVlMQzVoS09Bazl3T3RhL0hIY3NYQmVYZnB5Z3lPQ2o2WTJlUT0iLCJqdGkiOiI5OEJENEREREVFMTIwMz
    Y1QkE1Mjc2MzI5RDBCM0YyMCIsInNpZCI6IjM2NDQ5RTVGNDczMUZFODEyQjcwOThCNUYwNzdCRTU4IiwiaWF0IjoxNzMwNzMyNDg0LCJzY29wZSI6WyJvcGVuaWQiLCJ1c2VyLmFjY2VzcyIsInByb2ZpbGUiLCJlbWFpb
    CIsInVzZXIuZGV0YWlscyIsImRlc2lnbi5kb21haW4iLCJzdXBwbHkuZG9tYWluIl0sImFtciI6WyJleHRlcm5hbCJdfQ.NjQ3e4RM8-7HpwE7u5hlcWSrasRh_-5i7MdAUipMhah3tcUoEPnqxuvcmKEzhuGg6fA_7PBjV
    NqFIDNnntb-0AC43xZlBn3ejuVa9WjV1NpuyJ6xELnEaXn6uw42ozLwyqojvzMbG-bnJNL2yMwCu_cFqOINy0w8EjPzUZRm2SlDY-fSCf2Ws5cgBVUpBwnHP7v-O8V1zuYZr4uBpW-t4zqjCeRrTSFIEdznGeRKFEYvtJdG
    -fW_6t_VDxwjXtlz-nLLg9lRfQrIuuw9tHbr34mG2Yp9lgpRyQY4Gsc4Gk25N40r02KFwuXsQR5clrD_eC8koWB8Md2GXEmKq4aXmQ"""
    params = {
        "apikey" : api_key,
        "queries": [{"mpn": part_number}]
    }

    response = requests.post(api_url, json=params)
    data = response.json()

    try:
        price = data["results"][0]["items"][0]["offers"]["prices"]["USD"][0][1]
        return price
    except (IndexError, KeyError):
        return None # return none if price not found

#Apply the function to each part in the DataFrame(df)   
part_data["API Price"] = part_data["MFR P/N"].apply(get_price_from_api)

#print(part_data.head()) #check first few rows to ensure data loaded properly

output_file_path = "\\file002\data\RFQ's\CUSTOMER ACTIVE\Honeybee\Unknown Program\0923241HONEY - 8C3 PCBA Turnkey\PRICING TEMPLATE\updated_parts_data.xlsx" #Path for the ouput Excel file
part_data.to_excel(output_file_path, index=False) #save the DataFrame to Excel file
print(f"Data saved to {output_file_path}")

              