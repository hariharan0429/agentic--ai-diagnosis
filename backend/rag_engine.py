import json

class RAG:
    def __init__(self):
        with open("data/diseases.json", "r") as f:
            self.data = json.load(f)

    def retrieve(self, user_symptoms):
        results = []

        for item in self.data:
            score = len(set(user_symptoms) & set(item["symptoms"]))
            if score > 0:
                results.append((item, score))

        results.sort(key=lambda x: x[1], reverse=True)
        return [r[0] for r in results[:3]]
