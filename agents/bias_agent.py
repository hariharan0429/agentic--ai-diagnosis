class BiasAgent:
    def run(self, confidence):
        values = sorted(confidence.values(), reverse=True)

        if len(values) > 1 and values[0] > 0.7 and values[1] < 0.2:
            return "Warning: Premature conclusion"

        return "No bias detected"
