from fastapi import FastAPI

app: FastAPI = FastAPI(root_path="/product")


@app.get("/")
def get_data():
    return {"message": "Hello From Product Service 02"}
