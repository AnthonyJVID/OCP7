from fastapi import FastAPI


# FastAPI is a framework for creating web APIs
app = FastAPI()

@app.get("/")
def index():
    return "This is a REST API for enabling my ML model to be used by other services."