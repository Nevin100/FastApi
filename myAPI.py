from fastapi import FastAPI, Path
#for Post :
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
  name:str
  price:float
  brand:Optional[str] = None

inventory={
  1:{
    "name":"Milk",
    "price":3.99,
    "brand":"Regular"
  }
}

MSIT={
  1:{
   "Name":"Nevin Bali",
   "SGPA":9.847 
  }
}


# First Api endpoint
@app.get("/")
def index():
  return {"name": "First Data"}

# path Parameters 
@app.get("/get-items/{item_id}")
def getItems(item_id : int):
  return inventory[item_id]

#Self Practice :
@app.get("/Msit-items/{item_id}")
def getItems(item_id : int = Path( description="This is my first endpoint test")):
  return MSIT[item_id]

#Query Parameters : 
#http://127.0.0.1:8000/get-by-name?name=Milk
@app.get("/get-by-name")
def getName(name: str):
  for item_Id in inventory:
    if inventory[item_Id]["name"] == name:
      return inventory[item_Id]
    
  return {"Data": "Not Found"}
  
# @Types of Http Methods : 
  
#Post : 
@app.post("/create-item/{item_id}")
def createItem(*, item: Item, item_id: int):
  if item_id in inventory:
    return {"Error":"This Id already Existed"}
  
  else:
    inventory[item_id] = {
      "name":item.name,
      "price":item.price
    }
    return inventory[item_id]