from agents.symptom_agent import SymptomAgent
from agents.hypothesis_agent import HypothesisAgent
from agents.evidence_agent import EvidenceAgent
from agents.revision_agent import RevisionAgent
from agents.strategy_agent import StrategyAgent
from agents.bias_agent import BiasAgent

def run_system(symptoms_text, vitals, labs):
    sym = SymptomAgent()
    hyp = HypothesisAgent()
    evi = EvidenceAgent()
    rev = RevisionAgent()
    strat = StrategyAgent()
    bias = BiasAgent()

    symptoms = sym.run(symptoms_text)
    hypotheses = hyp.run(symptoms)

    evidence_for, evidence_against = evi.run(hypotheses, vitals, labs)
    confidence = rev.run(hypotheses, evidence_for, evidence_against)

    next_step = strat.run(confidence)
    bias_check = bias.run(confidence)

    return {
        "symptoms": symptoms,
        "hypotheses": hypotheses,
        "confidence": confidence,
        "evidence_for": evidence_for,
        "evidence_against": evidence_against,
        "next_step": next_step,
        "bias": bias_check
    }
