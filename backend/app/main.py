from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FASTAPI()

class Item(electronic):
  name: str
  category: str
  model: str
  serial: int
