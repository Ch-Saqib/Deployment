from fastapi import FastAPI

app: FastAPI = FastAPI(root_path="/product")


@app.get("/")
def get_data():
    return {"message": "Hello World From Product Service 02"}
