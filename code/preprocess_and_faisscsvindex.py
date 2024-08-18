import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import faiss
import numpy as np
import re

with open('apache_logs.txt', 'r') as file:
    logs = file.readlines()

data = []
for line in logs:
    match = re.search(r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(.*?) (.*?) HTTP/1.1"', line)
    if match:
        ip = match.group(1)
        datetime = match.group(2)
        page = match.group(4)
        data.append(f'{ip} {datetime} {page}')

df = pd.DataFrame(data, columns=['Text'])

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(df['Text'])

dimension = vectors.shape[1]  
index = faiss.IndexFlatL2(dimension)  

vectors_np = vectors.toarray().astype('float32')
index.add(vectors_np)

faiss.write_index(index, 'faiss_index.bin')
print("FAISS index başarıyla 'faiss_index.bin' dosyasına kaydedildi.")

df.to_csv('processed_logs.csv', index=False)
print("İşlenmiş log verileri 'processed_logs.csv' dosyasına kaydedildi.")
