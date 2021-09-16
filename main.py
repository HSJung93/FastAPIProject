from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# item_id의 패스 파라매터를 함수로 전달 받는다.
# url의 쿼리형태로 전달된다.
# 자료형을 정해둘 수 있고, 위반 시 json 형태로 오류가 발생한다. 
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

# 패스 파라매터가 겹칠 수 있는 경우 위의 컨트롤러가 우선순위를 가진다.
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

# Enum을 이용하여 값을 미리 선언할 수 있다.
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        # json body에 중첩된 형태(딕셔너리)로 리턴할 수 있다.
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

# path 파라매터가 아니면 query 파라매터로 인식한다. 
# url이 다음과 같이 들어올 경우,
# http://127.0.0.1:8000/items/?skip=0&limit=10
# 선언된 skip과 limit의 값이 python type으로 변환된다. 

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

# None으로 Optional[str]을 선언해둘 수 있다.
# 쿼리 파라매터 또한 형변환이 가능하다.
# http://127.0.0.1:8000/items/foo?short=on
# http://127.0.0.1:8000/items/foo?short=yes

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# path 와 query 파라매터를 여러개 전달하는 경우

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Optional[str] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# required - needy
# default value - skip
# optional - limit
# 세 가지 경우로 파라매터를 받는 경우

@app.get("/conditionals/{conditional_id}")
async def read_user_item(
    conditional_id: str, needy: str, skip: int = 0, limit: Optional[int] = None
):
    conditional = {"conditional_id": conditional_id, "needy": needy, "skip": skip, "limit": limit}
    return conditional