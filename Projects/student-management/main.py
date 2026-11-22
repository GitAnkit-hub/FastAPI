from fastapi import FastAPI, Path, HTTPException, Query
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


# path paramter
# @app.get("/patient/{patient_id}")
# def view_patient(patient_id: str):
#     #load all patients
#     data =  load_data()

#     if patient_id in data:
#         return data[patient_id]
#     else:
#         return "patient not found"



# path paramter + path function

# @app.get("/patient/{patient_id}")
# def view_patient(patient_id: str = Path(..., description='ID of the patient in the DB', example='P001')):
#     #load all patients
#     data =  load_data()

#     if patient_id in data:
#         return data[patient_id]
#     else:
#         return "patient not found"



# An HTTP exception you can raise in your own code to show errors to the client.

# This is for client errors, invalid authentication, invalid data, etc. Not for server errors in your code.
# addition of HTTP method
#     
@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., description='ID of the patient in the DB', example='P001')):
    #load all patients
    data =  load_data()

    if patient_id in data:
        return data[patient_id]
    else:
        raise HTTPException(status_code=404, detail='Patient not found')



# Query Paramters  + Query function
@app.get("/sort/")
def sort_patient(sort_by:str = Query(..., description='sort on the basis of height, weight and BMI', ), order: str = Query('asc', description = 'sort in ascending or descending order')):

# sort_by is required paramter denoted by ...
# order is optional paramter if not given -> ordered in 'ascending order'    

    

    valid_field = ['height', 'weight', 'bmi']
    if sort_by not in valid_field:
        raise HTTPException(status_code = 404, detail =f'Invalid Field, select from {valid_field}')

    if order not in ['asc', 'desc']:
        raise HTTPException(status_code = 404, detail='Invalid order, select between asc and desc')

    #load all patients
    data =  load_data()
    sort_order = True if order == 'desc' else False
    sorted_data = sorted(data.values(), key =lambda x:x.get(sort_by), reverse=sort_order)    
    
    return sorted_data