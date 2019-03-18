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

# Replace 'TB' with 000 and rm 'GB'
storage_sec = laptops["storage"].str.replace("GB","").str.replace("TB", "000")

# split out into two columns for storage
laptops[['storage_1', 'storage_2']] = laptops['storage'].str.split("+", expand=True)

for i in ['storage_1', 'storage_2']:
	i_capacity = i + "_capacity_gb"
	i_type = i + "_type"
	# create new cols for capacity and type
	laptops[[i_capacity, i_type]] = laptops[i].str.split(n=1, expand=True)
	# make capacity numeric (can't be integer because of missing values)
	laptops[i_capacity] = laptops[i_capacity].astype(float)
	laptops[i_type] = laptops[i_type].str.strip()

# remove unneeded columns
laptops.drop(['storage', "storage_1", "storage_2"], axis=1, inplace=True)
print(laptops)
