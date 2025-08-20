from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field

app = FastAPI()


reports = []


class Report(BaseModel):
    location: str
    description: str
    severity: int
    

@app.get("/")
def root():
    return {"message": "Women Safety Reports API is running ✅"}

@app.post("/reports")
def add_report(report: Report):
    report_id = len(reports) + 1
    new_report = {
        "id": report_id,
        "location": report.location,
        "description": report.description,
        
    }
    reports.append(new_report)
    return new_report

@app.get("/reports")
def get_reports( ):
   
    return reports