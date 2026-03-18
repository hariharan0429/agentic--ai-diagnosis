from backend.rag_engine import RAG
from backend.llm_engine import generate_reasoning

rag = RAG()

def run_system(user_input):

    symptoms = [s.strip().lower() for s in user_input.split(",")]

    diseases = rag.retrieve(symptoms)

    confidence = {}
    evidence = {}

    for d in diseases:
        match = len(set(symptoms) & set(d["symptoms"]))
        conf = round(match / len(d["symptoms"]), 2)

        confidence[d["disease"]] = conf
        evidence[d["disease"]] = {
            "matched_symptoms": list(set(symptoms) & set(d["symptoms"]))
        }

    reasoning = generate_reasoning(diseases)

    return {
        "input_symptoms": symptoms,
        "confidence": confidence,
        "evidence": evidence,
        "next_step": diseases[0]["next_step"] if diseases else "More data needed",
        "reasoning": reasoning
    }
