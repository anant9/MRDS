import re
from langdetect import detect
from deep_translator import GoogleTranslator

def clean_text(text):
    text = re.sub(r"http\S+|@\S+|#\S+", "", text)
    text = re.sub(r"[^\w\s]", "", text)
    return text.strip()

def clean_and_translate(text):
    text = clean_text(text)
    if detect(text) != "en":
        text = GoogleTranslator(source='auto', target='en').translate(text)
    return text