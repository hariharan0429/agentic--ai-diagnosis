class RevisionAgent:
    def run(self, hypotheses, evidence_for, evidence_against):
        updated = {}

        for d, score in hypotheses.items():
            score += 0.1 * len(evidence_for[d])
            score -= 0.1 * len(evidence_against[d])
            updated[d] = max(0, min(score, 1))

        return updated
