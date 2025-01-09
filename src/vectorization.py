from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np

# Load metadata
metadata = pd.read_csv('data/metadata.csv')

# Preprocess text
metadata['text'] = metadata['title'].fillna(
    '') + " " + metadata['abstract'].fillna('')

# Generate embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(metadata['text'].tolist())

# Save embeddings
np.save('data/cord19_embeddings.npy', embeddings)
