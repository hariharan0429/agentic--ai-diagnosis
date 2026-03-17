class StrategyAgent:
    def run(self, confidence):
        if not confidence:
            return "Add more symptoms"

        top = max(confidence, key=confidence.get)

        if top == "Pneumonia":
            return "Next step: Chest X-ray"

        if top == "Pulmonary Embolism":
            return "Next step: CT scan / D-dimer"

        return "Ask more details"
