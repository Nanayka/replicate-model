class Predictor:
    def setup(self):
        from transformers import pipeline
        self.pipe = pipeline("text-generation", model="gpt2")

    def predict(self, prompt: str) -> str:
        result = self.pipe(prompt, max_length=50, num_return_sequences=1)
        return result[0]["generated_text"]