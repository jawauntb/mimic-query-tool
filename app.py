import streamlit as st
import faiss
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

# Load data and embeddings
metadata = pd.read_csv('data/metadata.csv')
embeddings = np.load('data/cord19_embeddings.npy')
model = SentenceTransformer('all-MiniLM-L6-v2')

# Initialize FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# Streamlit app
st.title("CORD-19 Research Query Tool")
query = st.text_input("Enter your research question:")
if query:
    query_embedding = model.encode([query])
    distances, indices = index.search(query_embedding, 5)

    # Display results
    st.write("Top Results:")
    for idx in indices[0]:
        st.write(metadata.iloc[idx]['title'])
