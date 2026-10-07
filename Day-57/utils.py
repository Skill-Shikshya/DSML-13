import re
import nltk
import joblib
import numpy as np
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS


class SentimentPredictor:
    def __init__(self, model_path=None, labels=None):
        self.model_path = model_path
        self.labels = labels
        self.lemmatizer = nltk.stem.WordNetLemmatizer()

        self.classifier = None
        self.vectorizer = None

        self.load_model()

    def text_processor(self, text: str) -> str:
        """Clean and preprocess input text."""

        text = text.lower()
        # HTML Tags
        text = re.sub(r"<.+?>", "", text)
        # URLs
        text = re.sub(r"[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)", "", text)
        # Punctuation and special characters
        text = re.sub(r"[^\w\d\s]", " ", text)
        text = text.strip()
        # Stopwords
        words = [word for word in text.split() if word not in ENGLISH_STOP_WORDS]
        # Remove short words
        words = [word for word in words if len(word) > 2]
        text = " ".join(words)

        # Lemmatization
        text = self.lemmatizer.lemmatize(text)

        return text

    def load_model(self):
        """Load classifier and vectorizer from the joblib file."""

        try:
            package = joblib.load(self.model_path)

            self.classifier = package["classifier"]
            self.vectorizer = package["vectorizer"]

        except Exception as e:
            raise RuntimeError(f"Cannot load model files: {e}") from e

    def get_embeddings(self, tokens):
        """Generate the mean embedding for the given tokens."""

        vectors = [
            self.vectorizer[word] for word in tokens if word in self.vectorizer
        ]

        if not vectors:
            raise ValueError("No valid words found in the vectorizer.")

        return np.mean(vectors, axis=0)

    def predict(self, user_input: str) -> str:
        """Predict sentiment for the given input."""

        processed_text = self.text_processor(user_input)

        embeddings = np.array([
            self.get_embeddings(processed_text.split())
        ])

        predicted_sentiment = self.classifier.predict(embeddings)

        return self.labels[predicted_sentiment[0]].capitalize()

    def run(self, user_input : str):
        """Main application entry point."""
        try:
            sentiment = self.predict(user_input)
            print(f"Predicted Sentiment: {sentiment}")
            return sentiment
        
        except Exception as e:
            print(f"Prediction failed: {e}")
            


# if __name__ == "__main__":
#     predictor = SentimentPredictor()
#     predictor.run()
