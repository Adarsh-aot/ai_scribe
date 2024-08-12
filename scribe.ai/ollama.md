## Running the Application Locally with Ollama

If you prefer to run the application using a local LLM instead of the Groq API, you can use the `langchain_ollama` library. Follow these steps to set it up:

1. **Install the `langchain_ollama` library**:
    - Uncomment the `langchain_ollama` line in `requirements.txt`:
    ```plaintext
    langchain_ollama==0.1.0
    ```
    - Run the following command to install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. **Modify the `services.py`**:
    - Update the `create_llm` function in `app/services.py` to use `ChatOllama` instead of `ChatGroq`:
    ```python
    from langchain_ollama import ChatOllama

    def create_llm():
        return ChatOllama(
            model="llama3.1",
            base_url="http://localhost:11434"
        )
    ```

3. **Run the Ollama server locally**:
    - Make sure your local LLM server is running at the specified `base_url`. The default setup assumes it’s running on `http://localhost:11434`.

4. **Start the FastAPI server**:
    ```bash
    uvicorn app.main:app --reload
    ```

5. **Access the API documentation**:
    - Open your browser and go to `http://localhost:8000/docs` to explore the interactive API documentation.

---

This section guides users on how to switch from using the Groq API to running the application locally with a local LLM via `langchain_ollama`.