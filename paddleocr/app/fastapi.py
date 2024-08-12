# app/main.py
from fastapi import FastAPI, File, UploadFile
from .ocr import OCRProcessor
from .utils import pdf_to_images

app = FastAPI()

@app.post("/ocr/")
async def perform_ocr(file: UploadFile = File(...), lang: str = "en"):
    ocr_processor = OCRProcessor(lang=lang)
    
    # Read the uploaded file into memory
    contents = await file.read()
    
    # Convert PDF to images
    images = pdf_to_images(contents)
    
    all_results = []
    for img in images:
        page_result = ocr_processor.process_image(img)
        all_results.extend(page_result)
    
    output = " ".join(all_results)
    
    return {"results": output}