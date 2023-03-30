from pydantic import BaseModel
from typing import Union

from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Factors(BaseModel):
    strategicCentrality: int
    feasibiltyOfIt: int
    processBreadth: int
    seniorManagementCommitment: int
    perfomanceManagement: int
    processFunctionality: int
    processResource: int
    structureFeasibility: int
    culturalCapacity: int
    managementWillingness: int
    valueChain: int
    riskPropensity: int


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/bpc/")
async def type_identifier(item: Factors):
    averageContigency = (item.strategicCentrality + item.feasibiltyOfIt + item.processBreadth + item.seniorManagementCommitment + item.perfomanceManagement +
                         item.processFunctionality + item.processResource + item.structureFeasibility + item.culturalCapacity + item.managementWillingness + item.valueChain) / 11
    radical_score = (averageContigency + item.riskPropensity) / 2
    if (radical_score < 2.5):
        return {
            "BPC": "evolutionary"
        }
    if (radical_score > 2.5):
        return {
            "BPC": "revolutionary"
        }
    if (radical_score == 2.5):
        return {
            "BPC": "decidion makers decide based on their risk propensity..."
        }
