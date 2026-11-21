from fastapi import FastAPI # import the framework

app = FastAPI() # create the main application object


@app.get("/")  #defining an endpoint
# this decorator tells fastapi that the following function should handle
# HTTP GET requests to the root URL "/".

def home():
    return {"message": "Hello Ankit"}

@app.get("/about")
def about():
    return{"message": "I am Ankit Agrawal, MTech Student at IIT Hyderabad, with specialization in Cryptanalysis, Network Security, Malware Analysis and Data Science!"}

# when a client sends a GET request to "/", the above funcnction executes and returns a python dictionary

# fastapi converts the dicitonary to json response


# cmd to run the code
# uvicorn main:app --reload
# uvicron -> starts the ASGI server
# main - > name of the python file
# app -> name of the fastapi instance
# --reload -> automatically restarts the developement server when code is modified