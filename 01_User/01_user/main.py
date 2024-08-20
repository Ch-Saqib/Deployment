from fastapi import FastAPI

app: FastAPI = FastAPI(root_path="/user")


@app.get("/")
def get_data():
    return {"message": "Hello From User Services 01"}
