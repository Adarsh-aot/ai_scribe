# FastAPI SOAP Note Formatter

This project is a FastAPI application that processes SOAP notes (Subjective, Objective, Assessment, and Plan) and generates a formatted output, such as an email to another doctor. The application leverages a language model (LLM) using the `langchain_groq` library and the `crewai` framework.

## Features

- **SOAP Note Formatting**: Automatically formats SOAP notes into different types of output.
- **Modular Structure**: The application is organized into separate modules for better code maintainability.
- **FastAPI**: Built with FastAPI for high performance and easy-to-use APIs.

## Table of Contents

- [Installation](#installation)
- [Project Structure](#project-structure)
- [Environment Variables](#environment-variables)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Running the Application](#running-the-application)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/ai_scribe.git
    cd your-repo-name
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv env
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```bash
        .\env\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source env/bin/activate
        ```

4. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Set up environment variables**:
    - Create a `.env` file in the root directory and add your API key:
    ```bash
    API=your_api_key_here
    ```

## Project Structure

```plaintext
my_project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── models.py
│   └── services.py
├── .env
├── README.md
└── requirements.txt
```

- **`app/main.py`**: Contains the FastAPI app and endpoint definitions.
- **`app/config.py`**: Handles loading environment variables and configuration.
- **`app/models.py`**: Defines Pydantic models for request validation.
- **`app/services.py`**: Contains functions to create LLM, agents, tasks, and crews.
- **`.env`**: Stores environment variables (API keys, etc.).
- **`requirements.txt`**: Lists the dependencies required by the project.

## Environment Variables

Ensure you have the following environment variables set in your `.env` file:

```plaintext
API=your_api_key_here
```

This `API` key is required for accessing the LLM service.

- For more details on setup locally, see the [set up locally](./ollama.md).

## Usage

### Running the Application

1. **Start the FastAPI server**:
    ```bash
    uvicorn app.main:app --reload
    ```

2. **Access the API documentation**:
   - Open your browser and go to `http://localhost:8000/docs` to explore the interactive API documentation.

### API Endpoints

#### POST `/generate_output/`

Generates a formatted output from the provided SOAP note.

- **Request Body**:
  ```json
  {
      "soap_note": "Patient shows symptoms of severe headache and nausea. Diagnosis is likely migraine. Treatment plan includes pain relievers and rest.",
      "type": "email to other doctor"
  }
  ```

- **Response**:
  ```json
  {
      "result": "Formatted output..."
  }
  ```

