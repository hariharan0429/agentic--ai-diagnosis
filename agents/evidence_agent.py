class EvidenceAgent:
    def run(self, hypotheses, vitals, labs):
        evidence_for = {}
        evidence_against = {}

        for d in hypotheses:
            evidence_for[d] = []
            evidence_against[d] = []

            if d == "Pneumonia":
                if vitals.get("spo2", 100) < 94:
                    evidence_for[d].append("Low SpO2")
                if labs.get("wbc", 0) > 11000:
                    evidence_for[d].append("High WBC")

            if d == "Pulmonary Embolism":
                if labs.get("d_dimer") == "normal":
                    evidence_against[d].append("Normal D-dimer")

        return evidence_for, evidence_against
