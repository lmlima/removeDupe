### 
# Install: pip install pandas
###
import pandas as pd

file_input = "sysmap-raw.csv"
file_output = "sysmap-nodupe.csv"
df = pd.read_csv(file_input, sep=";", dtype="str")
# Trim
df = df.applymap(lambda x: x.strip())
# Same case
df = df.applymap(lambda x: x.capitalize())

df = df.drop_duplicates(subset=['Year', 'Title'], keep="first")
# List of Year and Source
df = df.groupby("Title").agg(lambda x: ', '.join(set(x))).reset_index()

# Output
df.to_csv(file_output, index=False, sep=";")
