class SymptomAgent:
    def run(self, text):
        return [s.strip().lower() for s in text.split(",") if s]
