import pandas as pd

# Load metadata
metadata = pd.read_csv('data/metadata.csv')

# Explore the data
print(metadata.columns)
print(metadata.head())

# metadata['abstract'] = metadata['abstract'].fillna('').str.lower()
# metadata['title'] = metadata['title'].fillna('').str.lower()
