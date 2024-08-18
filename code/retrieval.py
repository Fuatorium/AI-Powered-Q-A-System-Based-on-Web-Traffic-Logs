import faiss
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def load_faiss_index(index_path='faiss_index.bin', data_path='processed_logs.csv'):
    try:
        index = faiss.read_index(index_path)
        df = pd.read_csv(data_path)
        vectorizer = TfidfVectorizer()
        vectorizer.fit(df['Text'])
        return index, vectorizer, df
    except Exception as e:
        print(f"Verileri yüklerken hata oluştu: {e}")
        return None, None, None


def retrieve_relevant_logs(query, vectorizer, faiss_index, df, k=5):
    try:
        query_vector = vectorizer.transform([query]).toarray().astype('float32')
        D, I = faiss_index.search(query_vector, k)
        relevant_logs = df.iloc[I[0]]

        if not relevant_logs.empty:
            return relevant_logs['Text'].tolist()
        else:
            return []
    except Exception as e:
        print(f"Logları ararken hata oluştu: {e}")
        return []


