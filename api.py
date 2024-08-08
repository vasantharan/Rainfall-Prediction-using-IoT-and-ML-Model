from fastapi import FastAPI
import numpy as np
import joblib
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputData(BaseModel):
    features: list

md = joblib.load('./prediction_model.joblib')

@app.post('/predict')
def predict(data: InputData):
    x_input = np.array(data.features).reshape(1, -1)
    prediction = md.predict(x_input)
    return {"prediction": prediction[0]}