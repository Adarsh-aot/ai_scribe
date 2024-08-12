from pydantic import BaseModel

class SoapNoteRequest(BaseModel):
    soap_note: str
    type: str