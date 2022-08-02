from fastapi import FastAPI

app = FastAPI()

#create an endpoint
@app.get("/")
def home():
    return {"Data":"Test"}
