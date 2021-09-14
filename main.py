from fastapi import FastAPI

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