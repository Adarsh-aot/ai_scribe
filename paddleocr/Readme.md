# OCR Service with FastAPI

## Introduction

This project is a web service for Optical Character Recognition (OCR) built using FastAPI. The service accepts PDF files, converts them into images, and extracts text from these images using the PaddleOCR library. This is particularly useful for extracting text from scanned documents or any PDF that contains text in an image format.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [API Documentation](#api-documentation)
- [Examples](#examples)
- [Contributors](#contributors)
- [License](#license)

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Adarsh-aot/ai_scribe.git
   cd ai_scribe
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the FastAPI server**:
   ```bash
   uvicorn app.main:app --reload
   ```

## Usage

Once the server is running, you can send a PDF file to the OCR endpoint to extract text.

### Example Request

Use `curl` to send a request to the API:

```bash
curl -X POST "http://127.0.0.1:8000/ocr/" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@yourfile.pdf" -F "lang=en"
```

### Response

The API will return a JSON object with the extracted text:

```json
{
  "results": "Extracted text from the PDF..."
}
```

## Features

- **PDF to Image Conversion**: Converts each page of a PDF document to an image.
- **OCR Processing**: Extracts text from images using PaddleOCR.
- **Multi-language Support**: The OCR can process text in different languages (default is English).

## Dependencies

- **FastAPI**: The web framework used to build the API.
- **PaddleOCR**: The OCR engine used for text extraction.
- **PyMuPDF (Fitz)**: Used for PDF to image conversion.
- **Pillow**: A Python Imaging Library used for image processing.

## Configuration

The OCR language can be configured through the API request by setting the `lang` parameter. By default, it is set to English (`en`).

## API Documentation

### POST `/ocr/`

This endpoint accepts a PDF file and returns the extracted text.

- **Parameters**:
  - `file`: The PDF file to be processed.
  - `lang`: The language for OCR processing (default: "en").

- **Response**:
  - `results`: A string containing the extracted text.

## Examples

### Python Example

Here is an example of using Python's `requests` library to interact with the API:

```python
import requests

files = {'file': open('yourfile.pdf', 'rb')}
data = {'lang': 'en'}
response = requests.post("http://127.0.0.1:8000/ocr/", files=files, data=data)

print(response.json()['results'])
```

