from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Item(BaseModel):
    item_name: str
    item_price: float

app = FastAPI()

items =[]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/create_item")
def create_item(item: Item):
    new_item = {
        "item_name": item.item_name,
        "item_price": item.item_price
    }
    items.append(new_item)
    return items

@app.get("/items", response_model=list[Item])
def get_items(limit: int =10):
    return items[0:limit]

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int, q: str = None):
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    
