
# report_ocr.py
import pytesseract
from PIL import Image

def extract_battle_data(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return f"Error processing image: {e}"
