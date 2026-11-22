from fastapi import FastAPI
import json
app = FastAPI()


def load_data():
    with open(r'D:\Sem-05\FastAPI\Projects\student-management\patients.json', 'r') as f:
        data = json.load(f)
    return data

@app.get("/")
def home():
    return {'message':'Patient Management System API'}


@app.get('/about')
def about():
    return{'message': 'A fully functional API to manage your patient records'}



@app.get("/view")
# get operation -> read operation
def view():
    return load_data()


@app.get("/patient/{patient_id}")
def view_patient(patient_id: str):
    #load all patients
    data =  load_data()

    if patient_id in data:
        return data[patient_id]
    else:
        return "patient not found"



