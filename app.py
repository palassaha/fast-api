from fastapi import FastAPI
import uvicorn
from BankNotes import BankNote
import numpy as np
import pickle
import pandas as pd

app = FastAPI()

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

@app.get('/')
def index():
    return {'meaasge' : 'Hello there!'}

@app.get('/{name}')
def get_name(name: str):
    return {'Welcome': f'{name}'}

@app.post('/predict')
def predict_banknote(data : BankNote):
    data = dict(data)
    variance=data['variance']
    skewness=data['skewness']
    curtosis=data['curtosis']
    entropy=data['entropy']
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    if(prediction[0]>0.5):
        prediction="Fake note"
    else:
        prediction="Its a Bank note"
    print(data, prediction)
    return {
        'prediction': prediction
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)