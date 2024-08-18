from retrieval import load_faiss_index, retrieve_relevant_logs
from generation import generate_response_from_logs

def rag_model(query, api_key, k=5):
    faiss_index, vectorizer, df = load_faiss_index()
    relevant_logs = retrieve_relevant_logs(query, vectorizer, faiss_index, df, k)
    if not relevant_logs:
        return "İlgili log kaydı bulunamadı."
    response = generate_response_from_logs(relevant_logs, api_key)
    return response

if __name__ == "__main__":
    query = "1 Ağustos tarihinde index.html sitesine erişen kullanıcılarının IP adreslerinin varsa 5 tanesinin listesini iletebilir misin?"
    api_key = "*SECRET*"
    response = rag_model(query, api_key)
    print("Yanıt:", response)
