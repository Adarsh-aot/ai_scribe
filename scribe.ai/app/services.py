from crewai import Agent, Crew, Task
from langchain_groq import ChatGroq
# from langchain_ollama import ChatOllama
from .config import API_KEY

# Create an LLM
def create_llm():
    return ChatGroq(
        temperature=0,
        model_name="llama3-70b-8192",
        api_key=API_KEY,
    )
    # Uncomment the below lines to use a local LLM
    # return ChatOllama(
    #     model="llama3.1",
    #     base_url="http://localhost:11434"
    # )

# Create the Soap Note Formatter Agent
def create_soap_note_agent(llm):
    return Agent(
        role='Soap Note Formatter',
        goal='Generate a formatted output ({type}) based on the provided soap note({soap_note})',
        backstory='You are an AI agent responsible for creating a formatted output from a soap note. Your job is to extract the relevant information from soap note and format it according to the specified type.',
        verbose=True,
        llm=llm
    )

# Create the Output Generation Task
def create_generate_output_task(agent):
    return Task(
        description="Generate a formatted output from the soap note",
        expected_output="The generated output in the specified format",
        agent=agent,
        output_file="output.md",
    )

# Create the Crew
def create_output_generation_crew(agent, task):
    return Crew(
        agents=[agent],
        tasks=[task],
        verbose=2
    )