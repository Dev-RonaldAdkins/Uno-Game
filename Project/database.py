import sqlite3

conn = sqlite3.connect("parts_data.db")
c = conn.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS Parts(
          PartNumber TEXT,
          OriginalPrice REAL,
          APIPrice REAL
          )
          """)

for _, row in part_data.iterrows():
    part_number = row["MFR P/N"]
    original_price = row["PRICE"]
    api_price = get_price_from_api(part_number)
    
    c.execute("INSERT INTO PARTS (PartNumber, OriginalPrice, APIPrice) VALUES (?, ?, ?)",
              part_number, original_price, api_price)
    
conn.commit()
conn.close()