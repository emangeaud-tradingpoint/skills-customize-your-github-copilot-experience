from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None


items = [
    {"name": "Notebook", "description": "Paper notebook for class notes"},
    {"name": "Keyboard", "description": "Mechanical keyboard"},
]


@app.get("/")
def read_root():
    # TODO: Return a JSON welcome message.
    raise HTTPException(status_code=501, detail="Not implemented")


@app.get("/items")
def read_items():
    # TODO: Return the list of items.
    raise HTTPException(status_code=501, detail="Not implemented")


@app.post("/items")
def create_item(item: Item):
    # TODO: Add the new item to the list and return it.
    raise HTTPException(status_code=501, detail="Not implemented")