from backend.rag_engine import MedicalRAG

class HypothesisAgent:
    def __init__(self):
        self.rag = MedicalRAG()

    def run(self, symptoms):
        query = " ".join(symptoms)
        knowledge = self.rag.query(query).lower()

        hypotheses = {}

        if "pneumonia" in knowledge:
            hypotheses["Pneumonia"] = 0.3

        if "embolism" in knowledge:
            hypotheses["Pulmonary Embolism"] = 0.2

        return hypotheses
