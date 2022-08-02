from fastapi import FastAPI,Path
from typing import Optional
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
def get_item(item_id: int = Path(None, description="The ID of the item you would like to view", gt=0, lt=2)): #Path() adds enforcements to actual path parameter,if no @arameter passed, default to None
    return inventory[item_id]

#querry parameter
@app.get("/get-by-name")
def get_item(*,name: Optional[str] = None, test: int): #querry parameter becomes optional  by None(default)
    for item_id in inventory:
        if inventory[item_id]["name"]== name:
            return inventory[item_id]
    return {"Data":"Not found"}


#setting up multiple path parameters example
# @app.get("/get-item/{item_id}/{name}")
# def get_item(item_id: int, name: str=None): 
#     return inventory[item_id]

#

