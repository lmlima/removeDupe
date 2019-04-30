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

# List of Year and Source
df = df.groupby(["Title", "Year"]).agg(lambda x: ', '.join(set(x))).reset_index()

# Output
df.to_csv(file_output, index=False, sep=";", columns=["Year","Source","Title"])
