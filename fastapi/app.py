#pip install prometheus-fastapi-instrumentator==6.1.0  uvicorn==0.23.2 fastapi==0.104.0

from prometheus_fastapi_instrumentator import Instrumentator
from typing import Union
import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os

# YOUR_ENV = os.environ["ENV_NAME"]

app = FastAPI()

# class for the data want to input 
class User(BaseModel):
    username: str
    email: str 
    avatar: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


# get info on something and query 
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
#curl -X 'GET' \
#  'http://localhost:8000/items/10023?q=query' \
#  -H 'accept: application/json'

# send data 
@app.put("/users")
def update_user( user: User):
    return {"user_name": user.username, "email": user.email}
#curl -X 'PUT' \
#  'http://localhost:8000/users' \
#  -H 'accept: application/json' \
#  -H 'Content-Type: application/json' \
#  -d '{
#  "username": "user1",
#  "email": "a@g.com",
#  "avatar": "avatar"
#}'

# expose /metrics for fastapi
instrumentator = Instrumentator().instrument(app)

@app.on_event("startup")
async def _startup():
    instrumentator.expose(app)

# Serve image
#storage = "/path/to/image"
@app.get("/avatar/{id}")
async def get_user(id):
    return FileResponse(f"{storage}/{id}.jpg")

# run uvicorn 
if __name__ =="__main__":
    uvicorn.run('app:app' , host='0.0.0.0' , port=8000 )