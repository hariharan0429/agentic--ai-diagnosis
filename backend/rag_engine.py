import os
from sentence_transformers import SentenceTransformer
import numpy as np

class MedicalRAG:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.documents = []
        self.embeddings = []
        self.load_knowledge()

    def load_knowledge(self):
        folder = "medical_knowledge"
        for file in os.listdir(folder):
            if file.endswith(".txt"):
                with open(os.path.join(folder, file), "r") as f:
                    text = f.read()
                    self.documents.append(text)

        self.embeddings = self.model.encode(self.documents)

    def query(self, query_text):
        query_embedding = self.model.encode([query_text])[0]
        scores = np.dot(self.embeddings, query_embedding)

        best_idx = int(np.argmax(scores))
        return self.documents[best_idx]
