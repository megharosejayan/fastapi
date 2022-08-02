from fastapi import FastAPI

app = FastAPI()

#create an endpoint
@app.get("/")
def home():
    return {"Data":"Test"}


@app.get("/about")
def about():
    return {"Data":"About"}


inventory ={
    1: {
        "name": "Milk",
        "price": 129,
        "brand": "Regular"
        }
    }

#setting up path parameter
@app.get("/get-item/{item_id}")
def get_item(item_id: int): #eg of type hint
    return inventory[item_id]

#setting up multiple path parameters example
@app.get("/get-item/{item_id}/{name}")
def get_item(item_id: int, name: str=None): 
    return inventory[item_id]

