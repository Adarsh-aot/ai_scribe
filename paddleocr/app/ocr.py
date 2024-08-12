# app/ocr.py
from paddleocr import PaddleOCR
import numpy as np

class OCRProcessor:
    def __init__(self, lang="en"):
        self.ocr = PaddleOCR(use_angle_cls=True, lang=lang)
    
    def process_image(self, img):
        img_array = np.array(img)
        result = self.ocr.ocr(img_array, cls=True)
        
        page_result = []
        for res in result:
            for line in res:
                text = line[1][0]
                page_result.append(text)
        
        return page_result