import model
from fastapi import FastAPI

model = model.make_model()
app = FastAPI()


@app.get("/")
def hello():
    return "Hello world"
