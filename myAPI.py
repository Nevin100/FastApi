from fastapi import FastAPI, Path
#for Post :
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
  name:str
  price:float
  brand:Optional[str] = None

class UpdateItem(BaseModel):
  name:Optional[str] = None
  price:Optional[float] = None
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
    #1st method : explicitly
    inventory[item_id] = {
      "name":item.name,
      "price":item.price
    } 
    
    #2nd method :
    # inventory[item_id] = item
    return inventory[item_id]
  
#Put : 
@app.put("/update-item/{item_id}")
def update_Item(item_id:int, item:UpdateItem):
  if item_id not in inventory:
    return {"Error":"This Id doesn't Exist"}
  
  if item.name!= None:
    inventory[item_id]["name"] = item.name
    
  if item.price!= None:
    inventory[item_id]["price"] = item.price
    
  if item.brand!= None:
    inventory[item_id]["brand"] = item.brand
    
  return inventory[item_id]


#Delete :
@app.delete("/delete-item/{item_id}")
def deleteItem(item_id: int):
  if item_id not in inventory:
    return {"Error":"This Id doesn't Exist"}
 
  del inventory[item_id]
  
  return{
    "Success":"Item Deleted Successfully"
  }
  