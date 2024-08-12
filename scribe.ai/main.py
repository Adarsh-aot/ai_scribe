from fastapi import FastAPI, HTTPException
from app.models import SoapNoteRequest
from app.services import create_llm, create_soap_note_agent, create_generate_output_task, create_output_generation_crew
app = FastAPI()

@app.post("/generate_output/")
async def generate_output(request: SoapNoteRequest):
    try:
        llm = create_llm()
        agent = create_soap_note_agent(llm)
        task = create_generate_output_task(agent)
        crew = create_output_generation_crew(agent, task)
        
        result = crew.kickoff({
            "soap_note": request.soap_note,
            "type": request.type
        })
        
        return {"result": result}       
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))