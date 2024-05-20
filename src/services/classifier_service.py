import os
import pickle
from transformations.transform_text import TransformText

current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, '..', 'classifier_modeling', 'modelo_classificador.pkl')
vectorizer_path = os.path.join(current_dir, '..', 'classifier_modeling', 'vectorizer.pkl')
class ClassifierService:
    def __init__(self):
        self.transformer = TransformText()
        with open(model_path, 'rb') as model_file:
            self.loaded_model = pickle.load(model_file)
        with open(vectorizer_path, 'rb') as vectorizer_file:
            self.loaded_vectorizer = pickle.load(vectorizer_file)
    
    def classify_text(self, text: str):
        cleaned_text = self.transformer.transform(text)
        vectorized_text = self.loaded_vectorizer.transform([cleaned_text])
        prediction = self.loaded_model.predict(vectorized_text)
        return prediction[0]