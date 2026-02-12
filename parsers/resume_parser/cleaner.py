import re

def clean_text(text):
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r'[^\w\s@.,]', '', text)
    return text.strip()

def normalize_text(text):
    return text.title()