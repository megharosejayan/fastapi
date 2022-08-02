from fastapi import FastAPI,Path,Query
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

#create an endpoint
@app.get("/")
def home():
    return {"Data":"Test"}


@app.get("/about")
def about():
    return {"Data":"About"}


inventory ={}
  

#setting up path parameter
@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description="The ID of the item you would like to view", gt=0, lt=2)): #Path() adds enforcements to actual path parameter,if no @arameter passed, default to None
    return inventory[item_id]

#querry parameter
# @app.get("/get-by-name")
# def get_item(*,name: Optional[str] = None, test: int): #querry parameter becomes optional  by None(default)
#     for item_id in inventory:
#         if inventory[item_id]["name"]== name:
#             return inventory[item_id]
#     return {"Data":"Not found"}

#querry and path parameter
# @app.get("/get-by-name/{item_id}")
# def get_item(*,item_id: int,name: Optional[str] = None, test: int): 
#     for item_id in inventory:
#         if inventory[item_id]["name"]== name:
#             return inventory[item_id]
#     return {"Data":"Not found"}

#query
@app.get("/get-by-name")
def get_item(name: str = Query(None, title="Name", description="Name of item.", max_length=10, min_length=2)): 
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {"Data":"Not found"}

@app.post("/create-item/{item_id}")
def create_item(item_id: int,item: Item):
    if item_id in inventory:
        return {"Error":"Item already exists"}

    #inventory[item_id] = {"name": item.name, "brand": item.brand, "price":item.price}
    inventory[item_id]=item
    return inventory[item_id]

#setting up multiple path parameters example
# @app.get("/get-item/{item_id}/{name}")
# def get_item(item_id: int, name: str=None): 
#     return inventory[item_id]



