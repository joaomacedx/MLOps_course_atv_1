import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')
class TransformText:
    def __init__(self):
        self.stop_words = set(stopwords.words('portuguese'))

    def transform(self, text: str):
        words = word_tokenize(text.lower())
        words = [word for word in words if word.isalnum()]
        words = [word for word in words if word not in self.stop_words]
        return ' '.join(words)