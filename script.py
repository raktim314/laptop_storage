import pandas as pd

laptops = pd.read_csv("laptops.csv", encoding="Latin-1")

def clean_col(col):
    col = col.strip()
    col = col.lower()
    return col

new_col = []
for i in laptops.columns:
    clean_c = clean_col(i)
    new_col.append(clean_c)

laptops.columns = new_col
# print(laptops.columns)

storage_sec = laptops["storage"].str.replace("+","").str.rsplit(n=3,expand=True)

storage_sec.columns = ["A","B","C","D"]

print(storage_sec[76:81])
print(storage_sec["A"])
